# 2017 Research Statement

Here you will find my research statement that I used while on the job market
in 2017, as I was finishing up my postdoc at UNC Chapel Hill. It was part of my
application packet that resulted in me taking my current position here at
Tennessee. I am providing it here as a sample LaTeX file and to show you some
properties of Git.

In particular, note that another .gitignore is included in this subdirectory
along with my .tex file and .bib file. This .gitignore says only to ignore all
files in the directory figures within this directory (that is, 
research_statement_2017/figures). That is because figure files for a document
are often large, and they are also not something that I necessarily want to track
changes for - the tracking wouldn't be meaningful anyway, since they are not 
text-based files. That is why you don't see any folder here at all called "figures": 
it has been ignored.

Additionally, you do not see any .log, .bbl, etc. files from my LaTeX compiling.
They were ignored in the .gitignore in the main folder of the repo. The lesson here: 
git will ignore anything contained in a .gitignore either in the current directory 
*or* a directory higher up in the repo! I don't need to repeat things to ignore 
as I create new folders under the current one.

Finally, the .gitignore in the base repo directory is a template one that GitHub 
provided me. It does a pretty good job. One thing to note is that it doesn't ignore 
the pdf files that are produced from LaTeX. You can add this manually, but I chose 
not to here so that you can see this is a working LaTeX file drawing on real (but 
untracked) figure files, producing real output.