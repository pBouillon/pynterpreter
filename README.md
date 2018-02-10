# pynterpreter
Small Brainfuck interpreter in Python3.X

## usage
### from a source file
code
```python3
pyint = Interpreter()
pyint.run(file='etc/hello_world.bf')
```
out:
```shell
Output:
	Hello World!
Finished in 0.002 ms.
```

### raw code as parameter
code
```python3
pyint = Interpreter()
pyint.run(code='>+')
```
out:
```shell
Finished in 0.000 ms.
```

### show status
To print your 'memory' status, just print the interpreter's object:
```python3
mem_cell = 8
pyint = Interpreter(size=mem_cell)
pyint.run(file='etc/hello_world.bf')
print(pyint)
```
out:
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
