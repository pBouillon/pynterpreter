# !/usr/bin/env python3
# -*- coding: utf-8 -*-

OP_INC    = '+'
OP_DEC    = '-'
OP_NEXT   = '>'
OP_PREV   = '<'
OP_INP    = ','
OP_PRINT  = '.'
OP_LOOP_B = '['
OP_LOOP_E = ']'

OPS = [
    OP_INC   ,
    OP_DEC   ,
    OP_NEXT  ,
    OP_PREV  ,
    OP_INP   ,
    OP_PRINT ,
    OP_LOOP_B,
    OP_LOOP_E]

class Interpetor:
    """
    """
    def __init__(self, limit=200, size=30):
        """
        """
        self.__max_loop = limit
        self.__tab_size = size

        self.__code   = []
        self.__vals   = [0 for x in range(self.__tab_size)]
        self.__tokens = []

    def __str__(self):
        """
        """
        tostr = 'Memory tab :\n| '
        for x in self.__vals:
            tostr += str(x) + ' | '
        return tostr

    def __tokenize(self):
        """
        """
        l_b = l_e = 0
        for c in self.__code:
            if c not in OPS:
                exit('Error: Unknown symbol \'' + c + '\'')
            self.__tokens.append(c)
        for t in self.__tokens:
            if t == OP_LOOP_B:
                l_b += 1
            if t == OP_LOOP_E:
                l_e += 1
            if l_e > l_b:
                exit('Error: loop closed before begin')
        if l_e != l_b:
            exit('Error: missing brackets')

    def __execute(self):
        """
        """
        index = step = 0
        loop = 0
        beg_ind = end_ind = -1
        while step < len(self.__tokens):
            token = self.__tokens[step]
            #
            if token == OP_INC:
                self.__vals[index] += 1
            #
            elif token == OP_DEC:
                self.__vals[index] -= 1
            #
            elif token == OP_NEXT:
                if index < self.__tab_size:
                    index += 1
            #
            elif token == OP_PREV:
                if index > 0 :
                    index -= 1
            #
            elif token == OP_INP:
                entry = input()
                self.__vals[index] = ord(entry)
            #
            elif token == OP_PRINT:
                content = ''
                for v in self.__vals:
                    if v != 0:
                        content += chr(v)
                print(content)
            #
            elif token == OP_LOOP_B:
                beg_ind = step 
                end_ind = [i for i,x in enumerate(self.__tokens) if x == OP_LOOP_E][0]
            #
            elif token == OP_LOOP_E:
                if loop == self.__max_loop:
                    exit('Error: looped too many times')
                if self.__vals[index] == 0:
                    step += 1
                    beg_ind = end_ind = -1
                else:
                    step = beg_ind
                    loop += 1
                    continue
            step += 1

    def run(self, code):
        """
        """
        self.__code = code
        self.__tokenize()
        print('Output: ')
        self.__execute()


def main():
    code = '+++++++++[>++++++++++<-]>>+++++++.'

    print('\n-------------------------\n')

    # default configuration
    pyint = Interpetor()
    pyint.run(code)
    print(pyint)

    print('\n-------------------------\n')

    # expecting smaller size
    pyint2 = Interpetor(size=10)
    pyint2.run(code)
    print(pyint2)

    print('\n-------------------------\n')

    # expecting to fail: limit 5 and `code` need to loop 9 time
    pyint3 = Interpetor(limit=5)
    pyint3.run(code)
    print(pyint3)

    print('\n-------------------------\n')


if __name__ == '__main__':
    main()
