# pynterpreter
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 
Brainfuck interpreter in Python3.X

## about this interpreter
### Brainfuck 
You can use this interpreter to run 'classic' brainfuck, which means 
use those 8 instructions: `+` `-` `>` `<` `[` `]` `.` and `,`. All other symbols will be 
considered as comments.

If you never heard of brainfuck, you can 
[start now here](https://fr.wikipedia.org/wiki/Brainfuck).

### changes
*pynterpreter* brings one new operation symbol. When the debug mode is 
activated (see CLI example bellow), use `%` to print your cells while 
running a code.

For example, this code:
```brainfuck
++%+++%
```
will result as:
```
pynterpreter> ++%+++%
| [2] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| [5] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
pynterpreter> 
```

## pynterpreter usage
For simplicity, I strongly recommend you to set an alias into your `bash.rc`:
```shell
alias brainfuck='path/src/brainfuck.py'
```
### from a source file
```shell
~$ python3 path/src/brainfuck.py -f etc/hello_world.bf
Output:
    Hello World!
Finished in 0.003 ms.
```

### raw code as parameter
```shell
~$ python3 path/src/brainfuck.py -c "+++[>++++++++++<-]>+++."
Output:
    !
Finished in 0.002 ms.
```

### cli
![CLI example](https://github.com/pBouillon/pynterpreter/blob/readme_img/img/cli_example.png?raw=true "CLI example")

## improvements
- [x] arg parser for source file
- [x] better exception/error handling
- [x] comments
- [x] debug symbol
- [x] debug status in spec for CLI
- [x] interpreter in CLI
- [x] nested loops
- [x] unit testing

## contributions
All contributions are welcome !
