# pynterpreter
Small Brainfuck interpreter in Python3.

## usage
Specify source path or paste raw your BF code:
```python3
pyint = Interpetor()
pyint.run(file='etc/hello_world.bf')
```
or
```python3
pyint = Interpetor()
pyint.run(code='>+')
```
To print your 'memory' status, just print the interpreter's object:
```python3
max_loop = 300
mem_cell = 64
pyint = Interpetor(limit=max_loop, size=mem_cell)
print(pyint)
pyint.run(file='etc/sample.bf')
print(pyint)
```

## improvements
- [ ] arg parser for source file
- [x] better exception/error handling
- [ ] interpreter in CLI

## contributions
All contributions are welcome !
