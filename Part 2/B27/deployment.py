from os import walk, makedirs
from os.path import join, getctime
import datetime
from jinja2 import Environment, FileSystemLoader
from mistune import create_markdown
from yaml import safe_load, safe_dump
from hashlib import sha256

def main():
    POSTS = {}
    ENV = Environment(loader=FileSystemLoader("templates"))
    ENV.globals['datetime'] = datetime # Make the datetime module available to templates
    ENV.globals['posts'] = POSTS # Make posts available to templates globally

    # Walk the entire directory
    for root, dirs, files in walk("blog/"):
        for file in files:
            # Read the contents of the post
            path = join(root, file)
            with open(path, "r") as read_file:
                content = read_file.read()

            # If the post has frontmatter use it, otherwise create it
            if content.startswith("---"):
                frontmatter, content = [x for x in content.split("---", 2) if x != ""]
                frontmatter = safe_load(frontmatter)
            else:
                frontmatter = {}

            # Add the frontmatter attributes to the post's state
            mtime = datetime.datetime.fromtimestamp(getctime(path))
            post = {}
            post["root"] = root
            post["filename"] = file
            post["title"] = frontmatter.get("title", post["filename"].replace(".md", ""))
            post["slug"] = frontmatter.get("slug", post["title"].lower().replace(" ", "-"))
            post["created"] = frontmatter.get("created", mtime)
            post["modified"] = frontmatter.get("modified", "")
            post["hash"] = frontmatter.get("hash", "")
            post["content"] = content

            # If the ctime is greater than the utime, set the ctime to the utime and remove the utime
            utime = post["modified"]
            if utime != "" and ctime > utime:
                post["created"] = utime
                post["modified"] = mtime if mtime > utime else ""

            # If the creation or modification times are further than the current date, set it to the most recent modification datetime
            if ctime > datetime.datetime.now(): post["created"] = mtime
            if utime != "" and utime > datetime.datetime.now(): post["modified"] = mtime

            # If the post has been updated, set the modification date to the most recent modification date
            if post["hash"] == "" or (utime == "" and mtime > post["created"]) or (utime != "" and mtime > utime):
                # Calculate the SHA-256 hash of the file
                with open(path, "rb") as byte_file:
                    file_bytes = byte_file.read()
                file_bytes = file_bytes.split(b"---", 2)[2] if file_bytes.startswith(b"---") else file_bytes # Take only the post's contents
                file_hash = sha256(file_bytes.lstrip(b"\n")).hexdigest() # Has to strip the starting newline characters because it would make it seem like a new file if any post didn't have frontmatter

                # If the hashes don't match, then update the modification time
                if post["hash"] == "" or post["hash"] != file_hash:
                    if post["hash"] != "": post["modified"] = mtime
                    post["hash"] = file_hash

            # If the post has an empty modification field, ignore it
            if post["modified"] == "" or post["created"] == post["modified"]: del post["modified"]

            # Calculate the reading time of the post (using an average WPM of 200)
            time = len(post["content"].split(" ")) // 200 + 1 # minimum time of 1 minute
            post["reading"] = f"{time} minute(s)" if time < 60 else f"{time / 60:.2f} hours"

            # Append the (updated) post to the list of posts
            POSTS.append(post.copy())

            # If the frontmatter did not change then don't write to the file
            if frontmatter == post: continue

            # Write the updated yaml to the file (excluding the content)
            del post["content"]
            del post["reading"]
            with open(path, "w") as write_file:
                write_file.write("---\n")
                safe_dump(post, write_file, default_flow_style=False, sort_keys=False)
                write_file.write("---\n\n")
                write_file.write(content.lstrip("\n"))

    # Create the markdown renderer
    markdown = create_markdown(plugins=['strikethrough', 'footnotes', 'table', 'url', 'task_lists', 'abbr', 'mark', 'insert', 'superscript', 'subscript', 'math', 'spoiler'], escape=False, hard_wrap=True)

    # Store the post template in memory
    post_template = ENV.get_template("post.html")

    # Render every post
    for post in POSTS:
        print(f"The {post["title"]} page is now being created.")

        # Render the post
        html, state = markdown.parse(post["content"])
        post["content"] = html

        # Render the post using the template
        output = post_template.render(post=post)

        # Create the path of the output render
        path = join("public", "blog", post["slug"])
                
        # Write the render to a file
        with open(f"{path}.html", "w") as file:
            file.write(output)
                
        print(f"\033[0;32mThe page for the {post["title"]} post has successfully been created.\033[0m")

if __name__ == '__main__':
    main()