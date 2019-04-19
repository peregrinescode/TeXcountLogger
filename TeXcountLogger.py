#!/usr/bin/env python3
# coding:utf-8
"""
  Author:  ross warren <ross.warren@pm.me>
  Purpose: A python script which logs latex word count in csv
  Created: 18/04/19
"""

import os
import sys
import argparse
import subprocess
import csv
from datetime import date


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file', help="The tex file which you want to log", type=argparse.FileType('r'))
    # parser.add_argument('-l', '--logfile', help="The file name of the output csv",
    #                     default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    try:
        texcount = subprocess.run(['texcount', '-inc', args.file.name], capture_output=True)

    except FileNotFoundError:
        print('Please install texcount.')
        sys.exit()

    count = texcount.stdout.decode().split('\n')

    print(count[0])  # Print file that is being counted

    countlog = []  # list for storing all counts
    countlog.append(['Date', str(date.today())])
    
    # Append the total word count to the log
    totalwords = [x for x in count if not x.find('Words in text: ')][-1].split()[3]
    countlog.append(['Total', totalwords])

    # Append word count for chapters
    sections = [x for x in count if not x.find('Included file: ')]
    for sec in sections:
        part = sec.split('/')[-1]
        wordcount = count[count.index(sec) + 2].split()[-1]
        countlog.append([part, wordcount])

    # Print word counts to terminal
    dash = '-' * 40  # for nice print output
    print('Todays date:', countlog[0][1])
    print(dash)
    print('{:<20s}{:>20s}'.format('Part', 'Words'))
    print(dash)
    for counts in countlog:
        print('{:<20s}{:>20s}'.format(counts[0], counts[1]))

    # Write to file
    with open(r'TeXcountLog', 'a') as log:
        writer = csv.writer(log)
        writer.writerow(countlog)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
