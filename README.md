# pynterpreter
Small Brainfuck interpreter in Python3.X

## usage
### from a source file
```python3
pyint = Interpreter()
pyint.run(file='etc/hello_world.bf') # specify the source
```
```shell
Output:
	Hello World!
Finished in 0.002 ms.
```

### raw code as parameter
```python3
pyint = Interpreter()
pyint.run(code='>+') # put it raw or from a str var
```
```shell
Finished in 0.000 ms.
```

### cells status
```python3
mem_cell = 8
pyint = Interpreter(size=mem_cell)
pyint.run(file='etc/hello_world.bf')
print(pyint) # print cells and their values
```
```shell
Output:
	Hello World!
Finished in 0.002 ms.

-----
Memory tab :
| 0 | 87 | 100 | 33 | 10 | 0 | 0 | 0 | 
-----
```

## improvements
- [ ] arg parser for source file
- [x] better exception/error handling
- [ ] interpreter in CLI
- [x] unit testing

## contributions
All contributions are welcome !
