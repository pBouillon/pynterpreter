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

import exceptions
from exceptions import ExecutionException
from exceptions import InitializationException

import interpreter
from interpreter import Interpreter

COLOR_END     = '\033[0m'
COLOR_FAIL    = '\033[91m'
COLOR_OKGREEN = '\033[92m'
COLOR_INFO = '\033[93m'

CMD_CLS  = 'clear'
CMD_HELP = 'help'
CMD_QUIT = 'quit'
CMD_LOOP = 'loop'
CMD_SIZE = 'size'
CMD_SHOW = 'show'

DEFAULT_OUTPUT = 'pynterpreter> '
DEFAULT_PREFIX = '/'
DEFAULT_ANSW   = 'Bad command, please see ' + \
                    DEFAULT_PREFIX + \
                    CMD_HELP

EXIT_SUCCESS   = 0

HELPER = '''\
    /help  ......... displays help
    /size  ......... change tab size
    /clear ......... clear memory cells
    /loop  ......... change max loop limit
    /show  ......... show cells status
    /quit  ......... exit CLI
'''

WELCOME = '''
*********************************************************
* Brainfuck interpreter written in Python 3             *
*                                                       *
* Author: pBouillon (https://pierrebouillon.tech/)      *
* See:    https://github.com/pBouillon/pynterpreter.git *
*********************************************************
'''


class CLI:
    """
    """
    def __init__(self):
        """
        """
        self.__inter = Interpreter()

    def run(self):
        """
        """
        print (WELCOME)
        while True:
            usr_in = input(DEFAULT_OUTPUT)

            # input is a command
            if usr_in.startswith(DEFAULT_PREFIX) :
                self.__run_cmd(usr_in[1:])
            # input is BF code
            else:
                try:
                    self.__inter.run(code = usr_in)
                except ExecutionException as e:
                    print (
                        COLOR_FAIL + 
                        'Error: '  + 
                        e.msg + 
                        COLOR_END
                    )
                except TypeError as e1:
                    print (
                        COLOR_FAIL + 
                        'Error: expected only one char' + 
                        COLOR_END
                    )
                finally:
                    self.__inter.clear_tokens()

    def __run_cmd(self, cmd):
        """
        """
        # helper
        if cmd == CMD_HELP:
            print (COLOR_INFO + HELPER + COLOR_END)

        # changing size
        elif cmd == CMD_SIZE:
            msg = '\tCurrent size is {}. New size: '
            msg =  msg.format(self.__inter.get_size())
            
            new_size = input (msg)
            if new_size.isdigit():
                self.__inter.set_size(int(new_size))
            else:
                print (COLOR_FAIL + 'ERROR: bad size' + COLOR_END)
        
        # changing limit
        elif cmd == CMD_LOOP:
            msg = '\tCurrent limit is {}. New limit: '
            msg =  msg.format(self.__inter.get_lim())

            new_lim = input (msg)
            if new_lim.isdigit():
                self.__inter.set_lim(int(new_lim))
            else:
                print (COLOR_FAIL + 'ERROR: bad limit' + COLOR_END)

        # clearing cells
        elif cmd == CMD_CLS:
            print (COLOR_OKGREEN + 'cells cleared' + COLOR_END)
            self.__inter.clear_cells()

        # show cells
        elif cmd == CMD_SHOW:
            print(COLOR_INFO + str(self.__inter) + COLOR_END)

        # exiting cli
        elif cmd == CMD_QUIT:
            exit(EXIT_SUCCESS)

        # unhandled cmd
        else:
            print(COLOR_INFO + DEFAULT_ANSW + COLOR_END)
