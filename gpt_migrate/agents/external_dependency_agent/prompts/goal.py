from textwrap import dedent

GOAL=dedent("""\
Your goal as principal software engineer at Google is to figure out and provide a list of {targetlang} libraries you would want to have 
installed in a {targetlang} project based on a {sourcelang} file. You have search and scrape tools available to you to find the relevant
libraries if you are unsure. Use these tools wisely and as neccessary to complete this task.

Please strictly follow the styling guideline of the given task with no deviations. Failure to comply with the styling guideline will 
result in severe penalties.
""")
