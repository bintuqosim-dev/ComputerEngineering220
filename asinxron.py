Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import asyncio
... 
... class FooAsync:
...     def __init__(self):
...         self.first_done = asyncio.Event()
...         self.second_done = asyncio.Event()
... 
...     async def first(self, printFirst):
...         printFirst()
...         self.first_done.set()
... 
...     async def second(self, printSecond):
...         await self.first_done.wait()
...         printSecond()
...         self.second_done.set()
... 
...     async def third(self, printThird):
...         await self.second_done.wait()
...         printThird()
... 
... # Sinov uchun
... async def main():
...     foo = FooAsync()
...     await asyncio.gather(
...         foo.first(lambda: print("first")),
...         foo.second(lambda: print("second")),
...         foo.third(lambda: print("third"))
...     )
... 
... asyncio.run(main())
