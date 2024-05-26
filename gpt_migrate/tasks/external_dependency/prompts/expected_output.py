from textwrap import dedent 

OUTPUT_FORMAT = dedent("""\
The output should be a comma-separated list of {targetlang} libraries you would want to have installed in a {targetlang} project based 
on the {sourcelang} provided above. If there are no outside libraries, answer only NONE. If there are libraries, please list them in 
the following format:

dep1,dep2,dep3...

Please do not include any other information in your answer. The content of your output will be directly read into a file and any 
deviation will cause this process to fail.
""")
