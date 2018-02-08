# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2018 Pierre Bouillon

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

import pathlib
from pathlib import Path

import sys
from sys import stderr

import time
from time import time

# Increase current block
OP_INC    = '+'
# Decrease current block
OP_DEC    = '-'
# Switch to next block
OP_NEXT   = '>'
# Switch to previous block
OP_PREV   = '<'
# Get user's input
OP_INP    = ','
# Print current block 
OP_PRINT  = '.'
# First loop delimiter
OP_LOOP_B = '['
# Go to the first delimiter if current block != 0
OP_LOOP_E = ']'

# Primary BF instructions
OPS = [
    OP_INC   ,
    OP_DEC   ,
    OP_NEXT  ,
    OP_PREV  ,
    OP_INP   ,
    OP_PRINT ,
    OP_LOOP_B,
    OP_LOOP_E
]

# BF extension
EXTENSION = '.bf'
# Max loop repetition
MAX_LOOP  = 200
# Numbers of blocks
SIZE      = 30

class Interpetor:
    """References Interpretor

    Attributes:
        __max_loop : max loop repetition
        __tab_size : blocks in the 'memory' table
        __code     : BF code
        __vals     : blocks for execution
        __tokens   : token parsed
    """
    def __init__(self, limit=MAX_LOOP, size=SIZE):
        """Initialize the interpretor

        limit and size are optionnal
        """
        self.__max_loop = limit
        self.__tab_size = size

        self.__code   = []
        self.__vals   = [0 for x in range(self.__tab_size)]
        self.__tokens = []

    def __str__(self):
        """Show blocks state
        """
        tostr = 'Memory tab :\n| '
        for x in self.__vals:
            tostr += str(x) + ' | '
        return tostr

    def __abort(self, msg, errcode) :
        errmsg = 'Error: ' + msg
        print (errmsg, file=stderr)
        exit (errcode)

    def __execute(self):
        """Run the tokenized code
        """
        index      = step    = loop = 0
        beg_ind    = end_ind = -1
        prog_print = ''

        while step < len(self.__tokens):
            token = self.__tokens[step]

            # Currrent token is +
            if token == OP_INC:
                self.__vals[index] += 1
            # Currrent token is -
            elif token == OP_DEC:
                self.__vals[index] -= 1
            # Currrent token is >
            elif token == OP_NEXT:
                print('index is now: {}'.format(index))
                index += 1
                if index >= self.__tab_size:
                    index = 0
            # Currrent token is <
            elif token == OP_PREV:
                print('index is now: {}'.format(index))
                index -= 1
                if index < 0 :
                    index = self.__tab_size - 1
            # Currrent token is ,
            elif token == OP_INP:
                entry = input()
                self.__vals[index] = ord(entry)
            # Currrent token is ,
            elif token == OP_PRINT:
                content = ''
                for v in self.__vals:
                    if v != 0:
                        content += chr(v)
                prog_print += content
            # Currrent token is [
            elif token == OP_LOOP_B:
                beg_ind = step 
                end_ind = [i for i,x in enumerate(self.__tokens) if x == OP_LOOP_E][0]
            # Currrent token is ]
            elif token == OP_LOOP_E:
                if loop == self.__max_loop:
                    self.__abort('looped too many times', 1)
                if self.__vals[index] == 0:
                    step += 1
                    beg_ind = end_ind = -1
                else:
                    step = beg_ind
                    loop += 1
                    continue
            step += 1
        print (prog_print)

    def __tokenize(self):
        """Get all tokens
        """
        l_b = l_e = 0
        for c in self.__code:
            if c not in OPS:
                self.__abort ('Unknown symbol:' + c , 1)
            self.__tokens.append(c)
        for t in self.__tokens:
            if t == OP_LOOP_B:
                l_b += 1
            if t == OP_LOOP_E:
                l_e += 1
            if l_e > l_b:
                self.__abort ('loop closed before opened', 1)
        if l_e != l_b:
            self.__abort ('missing brackets', 1)

    def run(self, code='', file=''):
        """Run the BF code
        """
        beg = time()

        if file and code:
            print ('WARNING: reading file instead of the code')

        if file:
            source = Path(file)
            if source.exists() :
                if not source.is_file():
                    self.__abort ('Source is not a file', 1)
                if file[len(file) - 3 :] != EXTENSION:
                    self.__abort ('Source is not a BF file', 1)
                with source.open() as f:
                    self.__code = f.read()
                # clearing code
                self.__code = ''.join(
                    [c for c in self.__code if c in OPS]
                )
            else:
                self.__abort ('File does not exists', 1)
        else :        
            self.__code = code

        print(self.__code)

        self.__tokenize()
        self.__execute()
        print ('Finished in {} ms.'.format(time() - beg))
