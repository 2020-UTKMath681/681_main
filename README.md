# Welcome to Math/EEB 681!

This repo provides some basic files to get you started in git and Python.
More may be posted here later on. It also provides an example markdown file
(this file) and an example .gitignore geared toward LaTeX. There are .gitignore
templates available through GitHub - these will appear as options whenever you
create a new repo on GitHub or if you try to create a file called ".gitignore"
on the GitHub site. They are pretty decent lists of the kind of compiled files
that you will want to ignore in various languages.

There is also a license file - again, you can get a selection of these by creating
a new repo on GitHub. This one is GPL3, which is pretty popular for software
that you want to only be used in open source projects (unless someone is going to
give you $$$ for a different license).

## Markdown reference

If you look at the source of this file, you can see how basic markdown works.
It's a really simple way of making a text file with headings, lists, etc.

### Common libraries for Python scientific work
- numpy
- scipy
- matplotlib
- pandas
- networkx
- pytorch

### Links
Like Markdown? It's pretty easy!! Here is a link to the basic syntax: 
[Markdown Guide](https://www.markdownguide.org/basic-syntax/)

Github uses a version of Markdown that provides the usual syntax *plus* an additional
set of features. This superset of Markdown is called **GitHub Flavored Markdown**. 
It includes things like language-specific syntax highling for code blocks:  
```python
"""This is a short program that gives you spam and eggs on demand."""

def foo():
    print("Spam and eggs!")

if __name__ == "__main__":
    foo()
```  
and also task lists, tables, etc. Check it out at [Github: mastering markdown](https://guides.github.com/features/mastering-markdown/).

Also, as you have probably noticed, a Markdown file called README will automatically
be rendered and displayed on Github. Cool!!!

## SageMath

SageMath is a very popular mathematics software system, particularly in the pure
math world. It interfaces with GAP (Groups, Algorithms, Programming), a very
popular system for computational discrete algebra with particular emphasis on
computational group theory, and also FLINT (Fast Library for Number Theory). 
...and guess what? *SageMath is built on Python*, with much of its power deriving 
from NumPy, SciPy, matplotlib, and Python's symbolic library, Sympy. The 
interactive shell in SageMath is basically IPython, and the syntax of SageMath is 
Python. Thus, if you know Python, you really know the guts of how SageMath works 
and could get started using it immediately. I think of it as Python (plus friends) packaged for
mathematicians as a free, open-source alternative environment to Maple or
Mathematica. But from an educational standpoint, you get more flexibilty and 
programming knowledge learning Python directly, rather than confining yourself 
only to the SageMath envirnoment. Then, if there is something you want to do 
that isn't in SageMath, well, you know Python... and from an industry point of 
view, saying you know Python is better than saying you know SageMath.
(Maybe a bit of opinion and shameless promotion mixed in to this viewpoint...
tell your pure math friends to take Math 681! Muhahahaha!)

Regardless, it's a good tool to know about. You can find it here:  
[SageMath](https://www.sagemath.org/)
