# pynterpreter
Small Brainfuck interpreter in Python3.X

## usage
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

### cli usage
[[https://raw.githubusercontent.com/pBouillon/pynterpreter/readme_img/img/cli_example.jpg]]

## improvements
- [x] arg parser for source file
- [x] better exception/error handling
- [ ] comments
- [x] interpreter in CLI
- [x] nested loops
- [x] unit testing
- [x] debug symbol
- [x] debug status in spec for CLI

## contributions
All contributions are welcome !
