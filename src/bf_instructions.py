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

# Debug symbol: prints current tab when met
OP_DEBUG = '%'

# Primary BF instructions
OPS = [
    OP_INC   ,
    OP_DEC   ,
    OP_NEXT  ,
    OP_PREV  ,
    OP_INP   ,
    OP_PRINT ,
    OP_LOOP_B,
    OP_LOOP_E,
    OP_DEBUG
]

# BF extension
EXTENSION = '.bf'
