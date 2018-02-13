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

import sys
sys.path.append('../src')

import exceptions
from exceptions import ExecutionException
from exceptions import InitializationException

import interpreter
from interpreter import Interpreter

import unittest
from unittest import main
from unittest import TestCase


BF_CODE_LOOP_TWICE = '++[>+<-]'
BF_CODE_COMMENT    = 'not a bf code'
BF_MISSING_BRACK   = '[[]'
BF_INCORRECT_BRACK = '][]['
BF_CORRECT_BRACK   = '[[]]'
BF_INFINITY_LOOP   = '[+]'

INVALID_LIMIT = -1
INVALID_LOOP  = -1

MISSING_FILE    = 'this_is_not_even_a_real_file.bf'
WRONG_EXT_FILE  = '../etc/sample.txt'
WRONG_TYPE      = '../etc/'


class InterpreterTest(TestCase) :
    """Tests for Interpreter
    """
    def test_brackets_success(self):
        """Test if correct brackets pass
        """
        found = False
        pyint = Interpreter()
        try:
            pyint.run(code=BF_CORRECT_BRACK)
        except SystemExit: 
            found = True
        self.assertFalse(found)

    def test_code_comment_success(self):
        """Check if a bf code full of comments is handled
        """
        found = False
        pyint = Interpreter()
        try:
            pyint.run(code=BF_CODE_COMMENT)
        except SystemExit: 
            found = True
        self.assertFalse(found)

    def test_exc_on_incorrect_brack(self):
        """Test incorrect bracket order
        """
        with self.assertRaises(ExecutionException):
            pyint = Interpreter(limit=1)
            pyint.run(code=BF_INCORRECT_BRACK)

    def test_exct_on_infinity_loop(self):
        """Test if infinity loop is avoided
        """
        with self.assertRaises(ExecutionException):
            pyint = Interpreter()
            pyint.run(code=BF_INFINITY_LOOP)

    def test_exc_on_missing_brack(self):
        """Test missing bracket handling
        """
        with self.assertRaises(ExecutionException):
            pyint = Interpreter(limit=1)
            pyint.run(code=BF_MISSING_BRACK)

    def test_exit_on_missing_file(self):
        """Test if interpreter exit with a missing file
        """
        with self.assertRaises(SystemExit):
            pyint = Interpreter()
            pyint.run(file=MISSING_FILE)

    def test_exit_on_wrong_extension(self):
        """Test if interpreter exit with a folder
        """
        with self.assertRaises(SystemExit):
            pyint = Interpreter()
            pyint.run(file=WRONG_EXT_FILE)

    def test_exit_on_wrong_type(self):
        """Test if interpreter exit with a non bf source code
        """
        with self.assertRaises(SystemExit):
            pyint = Interpreter()
            pyint.run(file=WRONG_TYPE)

    def test_init_err_limit(self):
        """Test if incorrect limit is handled
        """
        with self.assertRaises(InitializationException):
            pyint = Interpreter(limit=INVALID_LIMIT)

    def test_init_err_size(self):
        """Test if incorrect size is handle
        """
        with self.assertRaises(InitializationException):
            pyint = Interpreter(size=INVALID_LOOP)

    def test_init_success(self):
        """Test if default initialization is successful
        """
        found = False
        try:
            pyint = Interpreter()
        except InitializationException: 
            found = True
        self.assertFalse(found)

    def test_run_loop_exc(self):
        """Test if the loop limitation is handle
        """
        with self.assertRaises(ExecutionException):
            pyint = Interpreter(limit=1)
            pyint.run(code=BF_CODE_LOOP_TWICE)

    def test_run_loop_success(self):
        """Test if the code can loop
        """
        found = False
        pyint = Interpreter(limit=15)
        try:
            pyint.run(code=BF_CODE_LOOP_TWICE)
        except SystemExit: 
            found = True
        self.assertFalse(found)

    def test_limit_set(self):
        """Test limit setter
        """
        _limit     = 5
        _new_limit = 6
        pyint = Interpreter(limit = _limit)
        pyint.set_lim(_new_limit)
        self.assertEqual(pyint.get_lim(), _new_limit)

    def test_size_set(self):
        """test size setter
        """
        _size     = 5
        _new_size = 6
        pyint = Interpreter(size = _size)
        pyint.set_size(_new_size)
        self.assertEqual(pyint.get_size(), _new_size)

if __name__ == '__main__':
    main()
