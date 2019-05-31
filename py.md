## seperate py env for version 2 and 3
```
virtualenv -p /usr/bin/python2 --no-site-packages env2.7
source env2.7/bin/activate
deactivate
pip install argparse
pip install cx_Oracle

virtualenv -p /usr/bin/python3 --no-site-packages env3.7
source env3.7/bin/activate
deactivate
```

## coding

```python
#!/usr/bin/env python
# coding: utf-8

import argparse
import inspect

class Review(object):
    def check_res(self):
        res = ['abtest', 'bctest', 'cctest']
        print (res)
    def review_status(self, engineer):
        res = ['y', 'n']
        print (res)

class Main(Review):
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--username')
        parser.add_argument('--password')
        subparsers = parser.add_subparsers()

        for name in dir(self):
            print('raw fun:', name)
            if not name.startswith("_"):
                print('no_ fun:', name)
                p = subparsers.add_parser(name)
                method = getattr(self, name)
                argnames = inspect.getfullargspec(method).args[1:]
                #use py2.7 usage argnames = inspect.getargspec(method).args[1:]
                print('method argnames:==', argnames)
                for argname in argnames:
                    p.add_argument(argname)
                p.set_defaults(func=method, argnames=argnames)
        self.args = parser.parse_args()

    def set_user(self):
        a = self.args
        username = a.username
        password = a.password
        print('set user!')

    def __call__(self):
        try:
            a = self.args
            print('args:', a)
            callargs = [getattr(a, name) for name in a.argnames]
            try:
                return self.args.func(*callargs)
            finally:
                print('final------')
        except Exception as err:
            print (str(err))
            print (err)


if __name__ == "__main__":
    main = Main()
    main()

```

## output
```
(env3.7) [root@cfBareos Pyora]# python 3.py --username j --password a review_status fred!
raw fun: __call__
raw fun: __class__
raw fun: __delattr__
raw fun: __dict__
raw fun: __dir__
raw fun: __doc__
raw fun: __eq__
raw fun: __format__
raw fun: __ge__
raw fun: __getattribute__
raw fun: __gt__
raw fun: __hash__
raw fun: __init__
raw fun: __init_subclass__
raw fun: __le__
raw fun: __lt__
raw fun: __module__
raw fun: __ne__
raw fun: __new__
raw fun: __reduce__
raw fun: __reduce_ex__
raw fun: __repr__
raw fun: __setattr__
raw fun: __sizeof__
raw fun: __str__
raw fun: __subclasshook__
raw fun: __weakref__
raw fun: check_res
no_ fun: check_res
method argnames:== []
raw fun: review_status
no_ fun: review_status
method argnames:== ['engineer']
raw fun: set_user
no_ fun: set_user
method argnames:== []
args: Namespace(argnames=['engineer'], engineer='fred!', func=<bound method Review.review_status of <__main__.Main object at 0x7f65ab2c3be0>>, password='a', username='j')
['y', 'n']
final------

```

