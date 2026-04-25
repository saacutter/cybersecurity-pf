## Introduction
To complete this activity, I began by going through a list of recently published CVEs. This was done using NIST's National Vulnerability Database, which provides a helpful search tool with filtering capabilities making it easy to locate recently published vulnerabilities. After some scrolling, I came across a few CVEs which looked interesting but I wanted to use one where the vulnerability had publicly accessible code that I could reference for the LLMs to actually fix since that would give the most varied response (at least in theory). Eventually I settled on CVE-2026-35363, which was published on April 22 2026 and impacted the `rm` implementation found in the uutils coreutils library. 

The uutils coreutils library is a reimplementation of the GNU coreutils written in Rust, primarily being used to replace the C-based GNU coreutils in Linux-based operating systems. This vulnerability was found by Canonical, who audited the uutils coreutils implementations for security flaws before they could be used to replace the GNU coreutils currently used by Ubuntu. This audit led to 113 issues being identified, of which this was one of them. Although many of these issues were resolved before Ubuntu 26.04 LTS was released (and hence are currently being used as of writing this), the `cp`, `mv`, and `rm` commands are still using the GNU coreutils implementations with plans to replace them with the uutils coreutils implementations in Ubuntu 26.10.

The bug identified with CVE-2026-35363 is a lack of proper safeguard mechanisms for the uutils coreutils implementation of `rm`. Specificially, it is vulnerable to CWE-22 (improper limitation of a pathname to a restricted directory) making it vulnerable to path traversal attacks. The `rm` command should, normally, prevent the current directory (or the parent directory) from being removed. However, this implementation only prevent specific paths from being removed (i.e. `.` and `..`). It did not consider semantically equivalent paths, like `./` or `.././`, which could be used to delete all contents within the current directory. The reason this wasn't discovered earlier is because the command did report that it received an invalid input, but deleted everything in the specified directory regardless. 

The three LLMs chosen were ChatGPT (using GPT-5.2), Claude (using Sonnet 4.6 Adaptive), and Gemini (using Gemini 3 Flash). In each case, the free tier was used (using the models available as of April 25 2026) to minimise the difference in model quality between vendors (i.e. it uses the "baseline" models for each to give a true representation of their capabilities) in addition to it being infeasible to pay for three different subscriptions to access higher tier models. Although this will give a baseline benchmark for LLMs, it should be noted that using higher tier models could give more effective output.

The following prompt was given to all models with no alterations.
> Consider CVE-2026-35363. This is a vulnerability that affects the `rm` utility of uutils coreutils, a Rust reimplementation of the GNU coreutils. The following is a description of the issue:
> ```
> A vulnerability in the rm utility of uutils coreutils allows the bypass of safeguard mechanisms intended to protect the current directory. While the utility correctly refuses to delete . or .., it fails to recognize equivalent paths with trailing slashes, such as ./ or .///. An accidental or malicious execution of rm -rf ./ results in the silent recursive deletion of all contents within the current directory. The command further obscures the data loss by reporting a misleading 'Invalid input' error, which may cause users to miss the critical window for data recovery.
> ```
>
> This issue is identified by issue #9749 on the GitHub page for this library, with the following description:
> ```
> Component
> rm -rf
> 
> Description
> An issue with rm -rf: when deleting with rm -rf ., consistent with GNU rm, it refuses to delete the current directory, reports an error directly, and does not delete any contents.
> 
> rm -rf .
> rm: refusing to remove '.' or '..' directory: skipping '.'
> However, when using rm -rf ./ or rm -rf .///, it reports an error as if the deletion failed (it should be consistent with rm -rf ., refusing directly without deleting anything), but in reality the contents of the current directory have already been deleted:
> 
> rm: cannot remove './': Invalid input
> This is because the clean_trailing_slashes function collapses ./// into "./":
> 
> fn clean_trailing_slashes(path: &Path) -> &Path {
>     ...
>         // Checks if element at the end is a '/'
>         if path_bytes[idx] == dir_separator {
>             for i in (1..path_bytes.len()).rev() {
>                 if path_bytes[i - 1] != dir_separator {
>                     idx = i;
>                     break;
>                 }
>             }
>             #[cfg(unix)]
>             return Path::new(OsStr::from_bytes(&path_bytes[0..=idx]));
>             ...
>         }
>     }
>     path
> }
> However, the path_is_current_or_parent_directory function only matches ".", "..", etc. It does not match equivalent paths like "./" or "../".
> 
> /// Checks if the path is referring to current or parent directory, if it is referring to current or any parent directory in the file tree e.g '/../..', '../..'
> fn path_is_current_or_parent_directory(path: &Path) -> bool {
>     let path_str = os_str_as_bytes(path.as_os_str());
>     let dir_separator = MAIN_SEPARATOR as u8;
>     if let Ok(path_bytes) = path_str {
>         return path_bytes == ([b'.'])
>             || path_bytes == ([b'.', b'.'])
>             || path_bytes.ends_with(&[dir_separator, b'.'])
>             || path_bytes.ends_with(&[dir_separator, b'.', b'.'])
>             || path_bytes.ends_with(&[dir_separator, b'.', dir_separator])
>             || path_bytes.ends_with(&[dir_separator, b'.', b'.', dir_separator]);
>     }
>     false
> }
> ```
>
> How would you fix this particular vulnerability, and why would you make that change?

Note: the code generated by each model will not be copied here. The chats have been provided for your own viewing, where the exact code generated can be seen. This will also not be tested because the codebase is too large to reasonably test the changes, and I don't know Rust well enough to be able to run the command properly. Instead, the conclusions each model comes to will be summarised and compared which should hopefully be enough.

### [ChatGPT (GPT-5.2)](https://chatgpt.com/share/69ec35c1-2c74-839e-8fa2-288cdefbc70d)
ChatGPT identified that the cause of the bug was a lack of proper safety checks. To fix this bug, it recommended a few different options:
- Normalising the path components before checking
- Explicitly include semantically equivalent paths in `path_is_current_or_parent_directory`

The normalising approach uses the `Path` module in Rust's standard library, which has a `components` method which automatically normalises paths. This would allow it to handle all equivalent representations of the same directory, ensuring that this function doesn't silently fail.

The explicit path inclusion approach involves adding paths like `./` and `../` to the function, but it is noted that this is a weaker approach that will keep missing edge cases (as these paths can be arbitrarily long, such as `././[...]./`).

### [Claude (Sonnet 4.6 Adaptive)](https://claude.ai/share/7e50c827-5c7d-4b5b-967f-08524e29c423)
Claude identified that the cause of the bug was `clean_trailing_slashes` strips trailing slahes but leaves one which is then used with `path_is_current_or_parent_directory`. It proposes a few different options to fix this bug:
- Strip all trailing slahes in `clean_trailing_slashes`
- Add the missing `./` and `../` patterns to `path_is_current_or_parent_directory`

The stripping trailing slashes approach involves removing all trailing slashes from the path string so that the path always ends in a non `/` character. This proposes this because it will normalise the provided paths, which then gets caught by `path_is_current_or_parent_directory`.

The adding missing patterns approach involves just adding 2 missing paths - `./` and `../`. It suggests this approach because the `path_is_current_or_parent_directory` should recognise any path that refers to the current or parent directory, even if the input isn't normalised.

It recommends using both of these approaches together because each approach misses something if it is implemented alone.

### [Gemini (Gemini 3 Flash)](https://gemini.google.com/share/eb2352e5b683)
Gemini identified the cause of the bug was the safeguard being too literal and the input path not being properly cleaned/normalised. The fix it proposes is to normalise the path or update the `path_is_current_or_parent_directory` function to be aware of the trailing `/` character. Gemini proposes this fix because it fixes the logical flaw and makes behaviour consistent with GNU coreutils.

### Comparison
At the time of writing, no change has been made to this vulnerability yet. However, pull request #11005 has been created to address the problem, which proposes the following solution:
```rs
fn path_is_current_or_parent_directory(path: &Path) -> bool {
    let Ok(bytes) = os_str_as_bytes(path.as_os_str()) else {
        return false;
    };

    // Strip all trailing separators
    let trimmed = match bytes.iter().rposition(|&b| !is_separator(b)) {
        Some(i) => &bytes[..=i],
        None => return false, // all separators or empty
    };

    // Extract the last component (after the last separator)
    let last = match trimmed.iter().rposition(|&b| is_separator(b)) {
        Some(i) => &trimmed[i + 1..],
        None => trimmed,
    };

    last == b"." || last == b".."
}
```

This is different to what each LLM proposed, and instead strips all the trailing `/` characters and checks that the last component is `.` or `..`. Although this is effectively just normalising the path, the closest answer to this solution was provided by Claude.

The least surprising thing about the answers provided by each LLM is that the primary solution was to normalise the path, which the proposed solution also does. Additionally, each LLM makes reference to the potential data loss vulnerability created from the output generated when paths like `./` are passed. However, only ChatGPT and Claude provide an alternative solution. This alternative solution is the same between them, and involves explicitly adding missing paths to the final check. However, ChatGPT specifically makes note that this is a weak solution while Claude says that both solutions should be used together rather than choosing between one or the other. 

An interesting thing that deviates between the models is their justification for their proposal. Both Claude and Gemini justify why they chose to implement their solution in the way they chose, which use reasonably sound logic. Gemini in particular gives several justifications for its reasoning, though every reason is semi-related (which can be forgiven). However, ChatGPT justifies why its implementation works. Although this is just a semantic difference since it ends up essentially being the same, its still an interesting shift regardless.

### References
National Institute of Standards and Technology. "NVD Vulnerability Search". Accessed: Apr. 24, 2026. [Online]. Available: https://nvd.nist.gov/vuln/search#/nvd/home?vulnRevisionStatusList=Published&sortOrder=3&sortDirection=2&resultType=records

National Institute of Standards and Technology. "CVE-2026-35363 Detail". Accessed: Apr. 25, 2026. [Online]. Available: https://nvd.nist.gov/vuln/detail/CVE-2026-35363

R. Sharma. "An update on rust-coreutils". Canonical Ltd. Accessed: Apr. 25, 2026. [Online]. Available: https://discourse.ubuntu.com/t/an-update-on-rust-coreutils/80773

The MITRE Corporation. "CVE-2026-35363". Accessed: Apr. 25, 2026. [Online]. Available: https://www.cve.org/CVERecord?id=CVE-2026-35363

The MITRE Corporation. "CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')". Accessed: Apr. 25, 2026. [Online]. Available: https://cwe.mitre.org/data/definitions/22.html

The Rust Team. "Module path". Accessed: Apr. 25, 2026. [Online]. Available: https://doc.rust-lang.org/std/path/index.html