Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from threading import Lock
... 
... class Foo:
...     def __init__(self):
...         self.first_done = Lock()
...         self.second_done = Lock()
...         self.first_done.acquire()
...         self.second_done.acquire()
... 
...     def first(self, printFirst):
...         printFirst()
...         self.first_done.release()
... 
...     def second(self, printSecond):
...         self.first_done.acquire()
...         printSecond()
...         self.second_done.release()
... 
...     def third(self, printThird):
...         self.second_done.acquire()
...         printThird()
