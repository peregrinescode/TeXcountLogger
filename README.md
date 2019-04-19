# TeXcountLogger
Logs output of texcount to a csv file for advanced word counting analysis

The python script will first run a texcount on your document. It will then search the output for total word count and section wordcounts. The counts will be written to a csv file along with the date.

Run daily from the command line:

    python TeXcountLogger.py yourtexfile.tex

## Requirements:
  * python3
  * texcount
  * 