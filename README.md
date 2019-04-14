# small-projects
Small scripts I've written for specific problems I'm having or just to practice programming skills

These probably should be their own repos or gists. Perhaps I'll separate these out in the future.

## bash_scripts
Contains a couple bash scripts.

### rpl_spaces.sh
Given an input directory, this change the filenames in that subdirectory so spaces become underscores. This is recursive.

### single_letter.sh
Given a input word, this returns a list of words that could be made by changing a single letter in that word. E.g. 'real' becomes 'teal', 'meal', 'deal', 'ream', etc.

## compsci_notes
Contains some of my notes taken on different tools/languages.

## doc_gen_tool
This is a tool for generating documents programatically (e.g. from a database).  This has two main components:

### forget.py
This script populates tags inside of strings according to a tag dictionary, where tags are in the form [[tag##default]], and the dictionary is in the form {tag : value}. If the dictionary does not contain a tag, the default value is used instead. You can think of this as a "filling out a form" tool. The forms/ directory is where we look for forms saved in a file.

### tagg.py
This script runs python code inside of tags in a string. Tags are in the form {{code_to_run}}. Functions to be used with this must be listed in funcs.py

## project_euler_solved.py
My [Project Euler](https://projecteuler.net/) scripts.

## sudoku.py
A tool for solving sudokus, a term which here means 'a structure in which no cell can share a value with any other cell within the same section'. Example case is at the bottom.
