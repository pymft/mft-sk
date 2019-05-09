## defenition : 

```python
def echo(s):
    return s
```

write decorator `saveit`, to make a copy of every function returned values 
into file `log.txt`

```python
@saveit
def echo(s):
    return s
```


```python
@save_into('filename.txt')
def echo(s):
    return s 
```


template for logfile: 
```
[timestamp], echo , args=("Hello", ), return_values=("Hello")
fact , args=(5, )  ,  return_values=(120, )
```





