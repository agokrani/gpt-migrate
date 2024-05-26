from textwrap import dedent

DESCRIPTION = dedent("""\
As a principal software enginneer at Google with particular expertise migrating codebases from {sourcelang} to {targetlang}, your task 
is to respond with a comma-separated list of {targetlang} libraries you would want to have installed in a {targetlang} project based on 
the following {sourcelang} file:

```
{sourcefile_content}
```
You are allowed to use search and scrape tool to lookup/read the documentation, if you are unsure about the libraries. The libraries 
should be of the {targetlang} based on the given {sourcelang} file.
""")