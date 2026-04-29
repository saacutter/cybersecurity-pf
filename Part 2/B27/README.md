While developing blog post functionality for my website, I ran into an issue. These blog posts were written in markdown, which all have frontmatter (metadata written in YAML) describing some attributes of the blog post such as the title, a slug (used for URLs), creation date, and (optionally) a modification date. This frontmatter has the following structure:
```
---
filename: sample.md
title: Sample Frontmatter
slug: sample-frontmatter
created: 2026-04-29
---
```
![sample](sample_post.png)

This information is used to automatically compile the blog post into HTML so that posts could be viewed by the website. This is achieved using Jinja templates, which allow these attributes to be used to create the page's structure.
```
{% extends "base.html" %}

{% block title %}{{ post.title }}{% endblock %}

{% block body %}
<div class="centered">
    <header>
        <h1>{{ post.title }}</h1>
        <div class="centered" style="display: flex; gap: 1em;">
            <div class="v-centered post-details">
                <i class="fa-solid fa-calendar"></i>
                <time datetime="{{ post.created }}">{{ post.created.strftime('%d %B, %Y') }}</time>
                {% if "modified" in post and post.modified.strftime('%d %B, %Y') != post.created.strftime('%d %B, %Y') %}(last updated <time datetime="{{ post.modified }}">{{ post.modified.strftime('%d %B, %Y') }})</time>{% endif %}
            </div>
            &bull;
            <div class="v-centered post-details">
                <i class="fa-solid fa-clock"></i>
                <p>{{ post.reading }}</p>
            </div>
        </div>
    </header>
    <hr style="width: 70%; border: 1px solid black;">
    <article class="centered post">
        {{ post.content }}
    </article>
</div>
{% endblock %}
```

The posts are compiled at every deployment using a Python script, using the `mistune` library to convert the markdown to HTML.
```
# This is not the entire process. Unnecessary things have been cut

# Walk the entire directory
for root, dirs, files in os.walk("blog/"):
    for file in files:
        # Read the contents of the post
        path = os.path.join(root, file)
        with open(path, "r") as read_file:
            content = read_file.read()

        # If the post has frontmatter use it, otherwise create it
        if content.startswith("---"):
            frontmatter, content = [x for x in content.split("---", 2) if x != ""]
            frontmatter = yaml.safe_load(frontmatter)
        else:
            frontmatter = {}

         # Add the frontmatter attributes to the post's state
        mtime = datetime.datetime.fromtimestamp(os.path.getctime(path))
        post = {}
        post["filename"] = file
        post["title"] = frontmatter.get("title", post["filename"].replace(".md", ""))
        post["slug"] = frontmatter.get("slug", post["title"].lower().replace(" ", "-"))
        post["created"] = frontmatter.get("created", mtime)
        post["updated"] = frontmatter.get("updated", "")

        # If the post has been updated, set the updated date to the most recent modification date
        if mtime > post["created"] and post["updated"] == "": post["updated"] = mtime

        # Write the updated yaml to the file
        with open(path, "w") as write_file:
            write_file.write("---\n")
            yaml.safe_dump(post, write_file, default_flow_style=False, sort_keys=False)
            write_file.write("---\n")
            if not content.startswith("\n"): write_file.write("\n")
            write_file.write(content)
```


This reads all markdown files in the `blog` directory, extracts the frontmatter and content, and writes it back to the post if it was missing (allowing for this information to be omitted initially as defaults would be used instead). However, there was an unintended consequence using this approach - if a blog post was ever modified (which would occur after every deployment since the frontmatter always gets written back) then the post's updated time would be updated every deployment regardless of whether it has been updated or not since it uses the actual file's metadata to determine whether it has been updated or not. Obviously, this is not the behaviour that I wanted out of this feature. Although I could have just removed the modification time attribute out of the frontmatter, I really wanted blog posts to have the last modified date. After some thinking about how I could resolve this issue, I realised that I could just use hashing (taught in lecture 2 of this unit). Hashing is used to convert an arbitrary length message to a fixed size one using an algorithm. Although not typically used for this purpose, it can be used to verify that a message (in this case the blog content) hasn't changed between deployments.

Hashes have various properties, but the ones most integral to this application are determinism (i.e. that the same input will always produce the same output), collision resistance (i.e. it is infeasible to find two inputs which produce the same hash), and the avalanche effect (i.e. a difference in the message will produce an entirely different output). This is perfect for this application, as it means that the post's previous contents don't also need to be stored somewhere (as this would take up too much space and make the markdown files unreadable) since the same post should always produce the same hash and it is unlikely that changing a post will result in the same hash previously calculated. Therefore, if the hash of the file is added to the file's frontmatter, then the file's modification time can be updated only if the computed hash is different to the saved hash. Using this idea, the Python script can be modified to calculate the SHA-256 hash (which could be any hash but SHA-256 is reliable and maintains the desired properties of hashes while still being relatively lightweight) of the post's contents:
```
# This is not the entire process. Unnecessary things have been cut

# Walk the entire directory
for root, dirs, files in os.walk("blog/"):
    for file in files:
        # Read the contents of the post
        path = os.path.join(root, file)
        with open(path, "r") as read_file:
            content = read_file.read()

        # If the post has frontmatter use it, otherwise create it
        if content.startswith("---"):
            frontmatter, content = [x for x in content.split("---", 2) if x != ""]
            frontmatter = yaml.safe_load(frontmatter)
        else:
            frontmatter = {}

        # Add the frontmatter attributes to the post's state
        mtime = datetime.datetime.fromtimestamp(os.path.getctime(path))
        post = {}
        post["filename"] = file
        post["title"] = frontmatter.get("title", post["filename"].replace(".md", ""))
        post["slug"] = frontmatter.get("slug", post["title"].lower().replace(" ", "-"))
        post["created"] = frontmatter.get("created", mtime)
        post["updated"] = frontmatter.get("updated", "")
        post["hash"] = frontmatter.get("hash", "")

        # If the post has been updated, set the updated date to the most recent modification date
        if (mtime > post["created"] and post["updated"] == "") or mtime > post["updated"]:
            # Calculate the SHA-256 hash of the file
            with open(path, "rb") as byte_file:
                file_bytes = byte_file.read()
            file_bytes = file_bytes.split(b"---", 2)[2] # Take only the post's contents
            file_hash = hashlib.sha256(file_bytes).hexdigest()

            # If the hashes don't match, then update the modification time
            if post["hash"] == "" or post["hash"] != file_hash:
                post["updated"] = mtime
                post["hash"] = file_hash

        # If the frontmatter did not change then don't write to the file
        if frontmatter == post: continue

        # Write the updated yaml to the file
        with open(path, "w") as write_file:
            write_file.write("---\n")
            yaml.safe_dump(post, write_file, default_flow_style=False, sort_keys=False)
            write_file.write("---\n\n")
            write_file.write(content.lstrip("\n"))
```

Note that the hash only uses the post's contents rather than the entire file's contents - this is because, while testing, there were issues with posts which had their frontmatter updated before the hash was inserted/updated. As the modified time was not being reset after calculating the hash, it was storing the old modification time was being compared causing a new hash to be created. As the hash was previously using old information, the new hash was different and the program thought that the file had been modified (which, while true, was only metadata in most cases). Instead, the hash of the post contents was used since this is what the modified time was intended to represent changing (and it also means post metadata can be changed without resetting the post's modification date which is another ability I wanted). As a result, the post content's calculated hash can be used to determine if it has been adjusted meaning that the script can now accurately adjust the post's modification time. This approach is similar to file integrity checksums, which hash a file's contents to ensure that it hasn't been modified or tampered with. The full file, which includes some modifications not seen here, is available in the directory for this activity on my GitHub repository.

This has showcased how hashing can be used in practical real-world applications beyond being limited to security. This application highlights the limitations of relying on file metadata to check if a file has been modified.

# References
D. Namdev. "How To Detect File Changes Using Python". GeeksforGeeks. Accessed: Apr. 29, 2026. [Online]. Available: https://www.geeksforgeeks.org/python/how-to-detect-file-changes-using-python/