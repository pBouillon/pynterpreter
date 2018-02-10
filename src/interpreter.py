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

import bf_instructions
from bf_instructions import EXTENSION
from bf_instructions import OP_DEC
from bf_instructions import OP_INC
from bf_instructions import OP_INP
from bf_instructions import OP_LOOP_B
from bf_instructions import OP_LOOP_E
from bf_instructions import OP_NEXT
from bf_instructions import OP_PREV
from bf_instructions import OP_PRINT
from bf_instructions import OPS

import errors
from errors import ERR_CODE_NOT_FILE
from errors import ERR_CODE_NOT_SOURCE
from errors import ERR_CODE_FILE_MISSING
from errors import ERR_CODE_BRACK_INCORR
from errors import ERR_CODE_BRACK_MISSING
from errors import ERR_LOOP_TOO_MANY_TIME
from errors import ERR_DICT

import exceptions
from exceptions import EXC_DICT
from exceptions import EXC_CODE_CELL
from exceptions import EXC_CODE_LOOP
from exceptions import InitializationException

import pathlib
from pathlib import Path

import sys
from sys import maxsize
from sys import stderr

import time
from time import time

# Max loop repetition
MAX_LOOP  = 200
# Numbers of blocks
SIZE      = 16

class Interpreter:
    """References Interpreter

    Attributes:
        __max_loop : max loop repetition
        __tab_size : blocks in the 'memory' table
        __code     : BF code
        __vals     : blocks for execution
        __tokens   : token parsed
    """
    def __init__ (self, limit=MAX_LOOP, size=SIZE):
        """Initialize the interpreter

        limit and size are optionnal
        """
        self.__max_loop = limit
        self.__tab_size = size

        self.__code   = []
        self.__vals   = [0 for _ in range(self.__tab_size)]
        self.__tokens = []

        self.__check_interpreter()

    def __str__ (self):
        """Show blocks state
        """
        tostr = '\n-----\nMemory tab :\n| '
        for x in self.__vals:
            tostr += str(x) + ' | '
        tostr += '\n-----'
        return tostr

    def __abort (self, errcode : int) :
        """
        """
        errmsg = 'Error: ' + ERR_DICT[errcode]
        print (errmsg, file=stderr)
        exit (errcode)

    def __check_interpreter(self) :
        """Ensure that the values are correctly set
        """
        if not 0 < self.__max_loop < maxsize:
            raise InitializationException (
                EXC_DICT[EXC_CODE_LOOP], 
                EXC_CODE_LOOP
            )

        if not 0 < self.__tab_size < maxsize:
            raise InitializationException (
                EXC_DICT[EXC_CODE_CELL], 
                EXC_CODE_CELL
            )

    def __execute (self):
        """Run the tokenized code
        """
        index      = step    = loop = 0
        beg_ind    = end_ind = -1
        prog_output = ''

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
                index += 1
                if index == self.__tab_size:
                    index = 0

            # Currrent token is <
            elif token == OP_PREV:
                index -= 1
                if index == -1 :
                    index = self.__tab_size - 1

            # Currrent token is ,
            elif token == OP_INP:
                entry = input()
                self.__vals[index] = ord(entry)

            # Currrent token is ,
            elif token == OP_PRINT:
                content = chr(self.__vals[index])
                prog_output += content

            # Currrent token is [
            elif token == OP_LOOP_B:
                beg_ind = step 
                end_ind = [i for i,x in enumerate(self.__tokens) if x == OP_LOOP_E][0]
            
            # Currrent token is ]
            elif token == OP_LOOP_E:
                if loop == self.__max_loop:
                    self.__abort (ERR_LOOP_TOO_MANY_TIME)
                if self.__vals[index] == 0:
                    beg_ind = end_ind = -1
                    loop = 0
                else:
                    step = beg_ind
                    loop += 1
                    continue

            step += 1

        if prog_output:
            print ('Output:\n\t' + prog_output)

    def __tokenize (self):
        """Get all tokens
        """
        l_b = l_e = 0
        for c in self.__code:
            if c in OPS:
                self.__tokens.append(c)

        for t in self.__tokens:
            if t == OP_LOOP_B:
                l_b += 1
            if t == OP_LOOP_E:
                l_e += 1
            if l_e > l_b:
                self.__abort (ERR_CODE_BRACK_INCORR)
        if l_e != l_b:
            self.__abort (ERR_CODE_BRACK_MISSING)

    def run (self, code='', file=''):
        """Run the BF code
        """
        beg = time()

        if file and code:
            print ('WARNING: reading file instead of the code')

        if file:
            source = Path(file)
            if source.exists() :
                if not source.is_file():
                    self.__abort (ERR_CODE_NOT_FILE)
                if file[len(file) - 3 :] != EXTENSION:
                    self.__abort (ERR_CODE_NOT_SOURCE)
                with source.open() as f:
                    self.__code = f.read()
            else:
                self.__abort (ERR_CODE_FILE_MISSING)
        else :        
            self.__code = code

        self.__tokenize()
        self.__execute()
        print ('Finished in {0:.3f} ms.'.format(time() - beg))
