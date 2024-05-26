from textwrap import dedent

OUTPUT_FORMAT=dedent("""\
We will be using the output you provide as-is to create new files, so please be precise and do not include any other text. Your output 
needs to be ONE file; if your output contains multiple files, it will break the system. Your output should consist ONLY of the file name, 
language, and code, in the following format:

file_name.ext

```language\nCODE\n```
""")