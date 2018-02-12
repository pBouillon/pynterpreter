# pynterpreter
Small Brainfuck interpreter in Python3.X

## usage
### from a source file
```shell
~$ python3 path/src/brainfuck.py -f etc/hello_world.bf
Output:
    Hello World!
Finished in 0.051 ms.
```

### raw code as parameter
```shell
~$ python3 path/src/brainfuck.py -c "+++[>++++++++++<-]>+++."
Output:
    !
Finished in 0.000 ms.
```

### cli usage
```shell
~$ python3 path/src/brainfuck.py

*********************************************************
* Brainfuck interpreter written in Python 3             *
*                                                       *
* Author: pBouillon (https://pierrebouillon.tech/)      *
* See:    https://github.com/pBouillon/pynterpreter.git *
*********************************************************

pynterpreter> _
```
see `/help` to have an overview of available commands:
```shell
pynterpreter> /help
    /help  ......... displays help
    /size  ......... change tab size
    /clear ......... clear memory cells
    /loop  ......... change max loop limit
    /show  ......... show cells status
    /quit  ......... exit CLI

pynterpreter> _
```
Example to print `!`:
```shell

    *********************************************************
    * Brainfuck interpreter written in Python 3             *
    *                                                       *
    * Author: pBouillon (https://pierrebouillon.tech/)      *
    * See:    https://github.com/pBouillon/pynterpreter.git *
    *********************************************************

pynterpreter> +++
pynterpreter> [>+++++ +++++ <-]
pynterpreter> >+++
pynterpreter> .
!
pynterpreter> /show
| 0 | [33] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
pynterpreter> _
```

## improvements
- [x] arg parser for source file
- [x] better exception/error handling
- [ ] comments
- [x] interpreter in CLI
- [ ] nested loops
- [x] unit testing

## contributions
All contributions are welcome !
