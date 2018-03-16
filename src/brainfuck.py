# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2018 Pierre Bouillon [https://pierrebouillon.tech/]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse
from argparse import ArgumentParser

import cli
from cli import CLI

import interpreter
from interpreter import Interpreter

import time
from time import clock

PROG_DESC = """
    Brainfuck interpreter written in Python3.X
    See https://github.com/pBouillon/pynterpreter.git
"""


def parse_args():
    """Parse provided args

    Add -c option
    Add -f option
    
    Returns:
        (dict) : {opt: val}
    """
    parser = ArgumentParser(description=PROG_DESC)

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-c',
        '--code',
        help='Raw BF code'
    )
    group.add_argument(
        '-f',
        '--file',
        help='Path to BF source'
    )

    return vars(parser.parse_args())


def show_elapsed(beg):
    """Print time elapsed since `beg`
    
    Parameter:
        beg (int) : 
    """
    print('Finished in {0:.3f} ms.'.format(clock() - beg))


if __name__ == '__main__':
    beg = clock()

    args = parse_args()
    code = args['code']
    source = args['file']

    pyint = Interpreter()

    # execute raw code
    if code:
        out = pyint.run(code=code)
        print('Output:\n\t' + out)
        show_elapsed(beg)

    # execute code from file
    elif source:
        out = pyint.run(file=source)
        print('Output:\n\t' + out)
        show_elapsed(beg)

    # cli
    else:
        CLI.run(pyint)
