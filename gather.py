Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> async def main_parallel():
...     tasks = [
...         download_file("file1.txt"),
...         download_file("file2.txt"),
...         download_file("file3.txt"),
...     ]
...     results = await asyncio.gather(*tasks)
...     print("All files downloaded:", results)
... 
... asyncio.run(main_parallel())
