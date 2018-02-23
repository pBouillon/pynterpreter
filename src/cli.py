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

import platform
from platform import system

COLOR_END     = '\033[0m'  if system() is not 'Windows' else ''
COLOR_FAIL    = '\033[91m' if system() is not 'Windows' else ''
COLOR_OKGREEN = '\033[92m' if system() is not 'Windows' else ''
COLOR_INFO    = '\033[93m' if system() is not 'Windows' else ''

CMD_CLS   = 'clear'
CMD_CFG   = 'cfg'
CMD_DEB   = 'debug'
CMD_HELP  = 'help'
CMD_QUIT  = 'quit'
CMD_LIMIT = 'limit'
CMD_SIZE  = 'size'
CMD_SHOW  = 'show'

DEFAULT_OUTPUT = 'pynterpreter> '
DEFAULT_PREFIX = '/'
DEFAULT_TAB_SP = 4
EXIT_SUCCESS   = 0

HELPER = '''\
    /clear ......... clear memory cells
    /cfg   ......... show interpreter's configuration
    /debug ......... toggle debug status
    /help  ......... displays help
    /limit ......... change max limit
    /quit  ......... exit CLI
    /show  ......... show cells status
    /size  ......... change tab size'''

WELCOME = '''
\t*********************************************************
\t* Brainfuck interpreter written in Python 3             *
\t*                                                       *
\t* Author: pBouillon (https://pierrebouillon.tech/)      *
\t* See:    https://github.com/pBouillon/pynterpreter.git *
\t*********************************************************
'''


class CLI:
    @staticmethod
    def poll (interpreter):
        """Show user interface

        Wait for user input
        If input starts with PREFIX, execute it as a command
        Else execute input as brainfuck code
        Start again

        Parameter:
            interpreter (Interpreter) : brainfuck interpreter
        """
        while True:
            usr_in = input(DEFAULT_OUTPUT)

            # input is a command
            if usr_in.startswith(DEFAULT_PREFIX) :
                try:
                    CLI.__run_cmd(usr_in[1:], interpreter)
                except KeyboardInterrupt:
                    print (
                        COLOR_FAIL +
                        '\nCommand canceled' +
                        COLOR_END
                    )
            # input is BF code
            else:
                try:
                    out = interpreter.run(code = usr_in)
                    if out:
                        print (
                            COLOR_INFO +
                            out +
                            COLOR_END
                        )
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
                    interpreter.clear_tokens()

    @staticmethod
    def run (interpreter):
        """Starts the CLI

        Parameter:
            interpreter (Interpreter) : brainfuck interpreter
        """
        print (WELCOME)
        try:
            CLI.poll (interpreter)
        except KeyboardInterrupt:
            print ('Interruption catched, exiting...')
        

    @staticmethod
    def __run_cmd (cmd, interpreter):
        """Execute the provided cmd

        Check if cmd is recognized
        Perform the associated operation
        
        Parameter:
            cmd (str) : command
            interpreter (Interpreter) : brainfuck interpreter
        """
        # helper
        if cmd == CMD_HELP:
            print (
                COLOR_INFO + 
                HELPER.expandtabs(DEFAULT_TAB_SP) + 
                COLOR_END
            )

        # changing size
        elif cmd == CMD_SIZE:
            msg = '\tNew size (current: {}): '
            msg =  msg.format(interpreter.get_size())
            
            new_size = input (msg)
            if not new_size.isdigit():
                print (COLOR_FAIL + 'ERROR: bad type' + COLOR_END)
                return
            try:
                interpreter.set_size(int(new_size))
                print (COLOR_OKGREEN + 'size updated' + COLOR_END)
            except InitializationException as e:
                print (COLOR_FAIL + 'ERROR: bad size' + COLOR_END)
        
        # changing limit
        elif cmd == CMD_LIMIT:
            msg = '\tNew limit (current: {}): '
            msg =  msg.format(interpreter.get_lim())

            new_lim = input (msg)
            if not new_lim.isdigit():
                print (COLOR_FAIL + 'ERROR: bad type' + COLOR_END)
                return
            try:
                interpreter.set_lim(int(new_lim))
                print (COLOR_OKGREEN + 'limit updated' + COLOR_END)
            except InitializationException as e:
                print (COLOR_FAIL + 'ERROR: bad limit' + COLOR_END)

        # clearing cells
        elif cmd == CMD_CLS:
            interpreter.clear_cells()
            print (COLOR_OKGREEN + 'cells cleared' + COLOR_END)

        # show cells
        elif cmd == CMD_SHOW:
            print (COLOR_INFO + str(interpreter) + COLOR_END)

        # show interpreter's configuration
        elif cmd == CMD_CFG:
            cfg_str = 'Configuration:\n'
            cfg_str+= '\tlimit: {}\n'
            cfg_str+= '\tsize : {}\n'
            cfg_str+= '\tdebug is: '
            cfg_str+= 'on' if interpreter.get_debug() else 'off'
            cfg_str = cfg_str.format (
                    interpreter.get_lim(),
                    interpreter.get_size()
                )

            print (
                COLOR_INFO + 
                cfg_str.expandtabs (DEFAULT_TAB_SP) + 
                COLOR_END
            )

        # exiting cli
        elif cmd == CMD_QUIT:
            exit (EXIT_SUCCESS)

        # enable debug
        elif cmd == CMD_DEB:
            interpreter.toggle_debug()
            msg = 'on' if interpreter.get_debug() else 'off'
            print (
                COLOR_OKGREEN + 
                'Debug is now ' +
                msg +
                COLOR_END
            )

        # unhandled cmd
        else:
            print (
                COLOR_INFO +
                'Bad command, please see ' +
                DEFAULT_PREFIX +
                CMD_HELP +
                COLOR_END
            )
