from textwrap import dedent

GOAL=dedent("""\
Your goal is to write code. This code must be as simple and easy to understand, while still fully expressing 
the functionality required. Please note that the code should be complete and fully functional. No placeholders. However, only write 
what you are asked to write. For instance, if you're asked to write a function, only write the function; DO NOT include import 
statements. We will do those separately.

Please strictly follow this styling guideline with no deviations. Variables will always be snake_case; either capital or lowercase. 
Functions will always be camelCase. Classes will always be PascalCase. Please follow this guideline even if the source code does not 
follow it.""")