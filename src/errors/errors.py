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


ERR_CODE_NOT_FILE      = 1
ERR_CODE_NOT_SOURCE    = 2
ERR_CODE_FILE_MISSING  = 3

ERR_CODE_BRACK_INCORR  = 4
ERR_CODE_BRACK_MISSING = 5

ERR_LOOP_TOO_MANY_TIME = 6


ERR_DICT = {
	ERR_CODE_NOT_FILE   : "Source is not a file",
	ERR_CODE_NOT_SOURCE : 'Source is not a BF file',
	ERR_CODE_FILE_MISSING  : 'File does not exists',
	ERR_CODE_BRACK_INCORR  : 'Loop closed before opened',
	ERR_CODE_BRACK_MISSING : 'Missing brackets',
	ERR_LOOP_TOO_MANY_TIME : 'Looped too many times'
}
