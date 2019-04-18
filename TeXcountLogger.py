#!/usr/bin/env python3
#coding:utf-8
"""
  Author:  ross warren <ross.warren@pm.me>
  Purpose: A python script which logs latex word count in csv
  Created: 18/04/19
"""

import os
import sys
import argparse
import subprocess
from datetime import date


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file', help="The tex file which you want to log", type=argparse.FileType('r'))
    parser.add_argument('-l', '--logfile', help="The file name of the output csv",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    try:
        texcount = subprocess.run(['texcount', args.file.name], capture_output=True)

    except FileNotFoundError:
        print('Please install texcount.')
        sys.exit()

    count = texcount.stdout.decode().split('\n')

    print(count[0])  # Print file that is being counted

    totalwords = [x for x in count if not x.find('Words in text: ')][0].split()[3]
    print('Total words:', totalwords)
    print('Today\'s date: ', date.today())
    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))