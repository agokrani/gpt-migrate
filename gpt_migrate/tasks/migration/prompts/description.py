from textwrap import dedent

DESCRIPTION = dedent("""\
As a principal software engineer at Google with particular expertise migrating codebases from {sourcelang} to {targetlang}. Your task 
is to do a migration from {sourcelang} to {targetlang}. You are allowed to use the following external libraries, but no other external 
libraries: {external_deps}. You will be given the current target directory structure of the {targetlang} project, the source directory 
structure of the existing {sourcelang} project, and the contents of the {sourcelang} file. Please use the below code format and name the 
file, variables, functions, etc. to be consistent with the existing {sourcelang} file where possible. The only exception is if this is 
an entrypoint file and {targetlang} requires a certain naming convention, such as main.ext etc. For the filename, include the full 
relative path if applicable. If the {sourcelang} code imports internal libraries from a given location, take special care to preserve 
this topology in the code you write for the {targetlang} project and use the functions in the internal libraries accordingly. Any port 
listening should be on 8080. Please ensure that all functions and variables are available to other files that may call them.


Current target directory structure, which is under active development and may have files added later which you can import from:
```\n{target_directory_structure}\n```


Existing source directory structure:
```\n{source_directory_structure}\n```


Existing {sourcelang} file, {sourcefile}:
```\n{sourcefile_content}\n```


Available internal functions in {targetlang}, their signatures and descriptions:
```\n{targetlang_function_signatures}\n```
""")