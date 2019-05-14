[homework](https://github.com/iamvee/hwpy/tree/master/02)


# Decorators


## decorate function with nothing!

```python
def decorator(fn):
    def decorated(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result
    return decorated

@decorator
def echo(s):
    return s 

# what `@` does here: 
# echo = decorator(echo)


if __name__ == "__main__":
    text = echo("Hello World!")
    print(text)
```


## decorate function with a simple tag!

```python
def tagger(fn):
    def function_decorated_by_tags(*args, **kwargs):
        tag = "tag"
        result = fn(*args, **kwargs)
        return f"<{tag}>{result}</{tag}>"
    return function_decorated_by_tags


def ansi_color_red(fn):
    def function_colorized(*args, **kwargs):
        before = "\033[31m"
        after = "\033[0m"
        result = fn(*args, **kwargs)
        return f"{before}{result}{after}"
    return function_colorized


@ansi_color_red
def echo_1(s):
    return s 


@tagger
def echo_2(s):
    return s 


def echo_3(s):
    return s 

if __name__ == "__main__":
    for fun in [echo_1, echo_2, echo_3]:
        text = fun("Hello World!")
        print(fun, text, sep='\n', end='\n\n')
```        
   

## decorators with input parameters

```python
def tag_this(tag):
    def decorator(fn):
        def decorated(*args, **kwargs):
            # tag = "tag"   # dont need it anymore 
            result = fn(*args, **kwargs)
            return f"<{tag}>{result}</{tag}>"
        return decorated
    return decorator


@tag_this('bold')
def echo(s):
    return s 

# `@`'s role here: 
# echo = tag_this('bold')(echo)

# each time we're calling echo, we're gonna reach 
# old `echo` this way:
# tag_this('bold')(echo)("Hello World!")
# |------>       |     | 
# |-------------->     |
# |-------------------->


if __name__ == "__main__":
    text = echo("Hello World!")
    print(text)
    
```


## decorating class

```python 
#!/usr/bin/env python3.7

def class_decorator(Cls):
    class DecoratedClass(Cls):
        def __init__(self, *args, **kwargs):
            print(f"an instance of {Cls} created \nand decorated to {__class__} \nid = {id(self)}")
            super().__init__(*args, **kwargs)

        def __hash__(self):
            pass    
    return DecoratedClass


@class_decorator
class A:
    def __init__(self, i):
        self.i = i


if __name__ == "__main__":
    a = A(10)
    print(a.__dict__)
```

## decorating instance method

```python

def method_decorator(f):
    def decorated(self, *args, **kwargs):
        res = f(self, *args, **kwargs)
        res = f"\033[31;1m{self.name}:\033[0m {res}"
        return res
    return decorated


class MySampleClass:
    def __init__(self, name):
        self.name = name

    @method_decorator
    def say_name(self):
        return self.name


if __name__ == "__main__":
    obj = MySampleClass("John")
    val = obj.say_name()

    print(val)
```
## decorating class (keep the history)

```python
#!/usr/bin/env python3.7

def duplicate_fail(Cls):
    class DecoratedClass(Cls):
        _instances = {}
        counter = 0
        def __init__(self, *args, **kwargs):
            self.__args = args
            self.__kwargs = tuple(kwargs.keys())
            super().__init__(*args, **kwargs)
            hash_val = hash(self)
            if not hash_val in self._instances:
                self._instances.update({hash_val: self})
                self.counter += 1
                self.__class__.counter += 1
            else:
                raise Exception("duplicated instance")

        def __hash__(self):
            return hash(self.__args + self.__kwargs)

        def __repr__(self):
            return f"object index {self.counter} out of {self.__class__.counter}"

    return DecoratedClass


@duplicate_fail
class MySampleClass:
    def __init__(self, i):
        self.i = i



if __name__ == "__main__":    
    a = MySampleClass(10)
    print(hash(a), a, MySampleClass, sep='\n', end='\n\n')

    b = MySampleClass(100)
    print(hash(a), a, MySampleClass, sep='\n', end='\n\n')
    print(hash(b), b, MySampleClass, sep='\n', end='\n\n')

    c = MySampleClass(10)

```
