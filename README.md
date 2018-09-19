# small-projects
Small scripts I've written for specific problems I'm having.


## single_letter.sh
Given a input word, this returns a list of words that could be made by changing a single letter in that word. E.g. 'real' becomes 'teal', 'meal', 'deal', 'ream', etc.

## doc_gen_tool
This is a tool for generating documents programatically (e.g. from a database).  This has two main components:

### forget.py
This script populates tags inside of strings according to a tag dictionary, where tags are in the form [[tag##default]], and dictionaries are in the form {tag : value}. If the dictionary does not contain a tag, the default value is used instead. You can think of this as a "filling out a form" tool.

### tagg.py
This script runs python code inside of tags in a string. Tags are in the form {{code_to_run}}. Functions to be used with this must be listed in funcs.py
