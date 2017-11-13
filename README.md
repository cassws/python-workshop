# Resources for Python 101 workshop ([link to Github)](https://github.com/zoews/PythonWorkshop)

## Workshop tools

[repl.it](https://repl.it/) - tool for writing and compiling Python directly in the browser (select *Python3* when using)

## Using raw data in Repl.it

To use the Buffy data in the workshop today, you'll need to create a new file on Repl.it:
* Click on the New File icon. The first time you click, this will generate a name for your main working Python file (main.py)
* Click a second time. You can name this file buffy.py (in Python, additional files are called *modules*)
* Copy the text from [buffyRawScript.py](https://github.com/zoews/PythonWorkshop/blob/master/buffyScriptRaw.py) and paste it into your new *buffy.py* file.
* Now navigate back to main.py. In order to use the data from buffy.py in your main file, simply add the following code to the top of your file: `from buffy import script` *Note: when importing from Python modules, you ignore the '.py' ending and simply write the filename without the extension*

## Outline

* Introductions: What questions do you have about programming?
* Why solve problems with code?
---
* Intro to Python 3
* Get started with Repl.it
* "Hello, world!"
* Data types: String, integers
* Control structures: if/then
---
* Working with raw data: Buffy!
* Importing a module (see above)
* Exploring text data
* String operations
* Iteration, the accumulator pattern
* Who talks more, Buffy or Willow?
---
* Accumulating with dictionaries
* Ranking character's dialogue time
* Most frequent words?
* (Explore more: Natural Language Processing)
* Extra challenges
* Star Trek script, or continue with Buffy
---
* Visualizing data (extra topics)

## Keep learning! Further resources

[Codecademy](https://www.codecademy.com/) - Free learning platform for coding. Browser-based learning (like repl.it), strong Python support.

[Programming Historian](https://programminghistorian.org/) - Peer-reviewed tutorials exploring a variety of beginner and intermediate topics (Python, web scraping, mapping, data manipulation). Written primarily for humanists but a strong resource for researchers and learners of all backgrounds.