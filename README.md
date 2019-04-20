# TeXcountLogger
Logs output of texcount to a csv file for advanced word counting analysis

The python script will first run a texcount on your document. It will then search the output for total word count and section wordcounts. The counts will be written to a csv file along with the date.

Run daily from the command line:

    python TeXcountLogger.py yourtexfile.tex

Example output to terminal:

    File: thesis.tex
    Todays date: 2019-04-20
    ----------------------------------------
    Part                               Words
    ----------------------------------------
    Date                          2019-04-20
    Total                               1176
    ch1-intro.tex                        805
    ch2-litreview.tex                     39
    ch3-methods.tex                      332
    ch4.tex                                0
    ch5.tex                                0

As you can see, I have a long way to go on my thesis.

## Requirements:
  * python3
  * texcount
