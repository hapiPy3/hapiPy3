The [Python 3 Porting Guide](http://docs.pythonsprints.com/python3_porting/py-porting.html) can be a reference. 

But note that, the Python 3 Porting Guide is last updated in July 29, 2010.

# indent and tab
Do not use the indent and tab at the same time
Or Python Interpreter will report the IndentationError

# httplib
[httplib](https://docs.python.org/2/library/httplib.html) 

The httplib module has been renamed to http.client in Python 3. The 2to3 tool will automatically adapt imports when converting your sources to Python 3.




# urllib2
[urllib2](https://docs.python.org/2/library/urllib2.html)

The urllib2 module has been split across several modules in Python 3 named urllib.request and urllib.error. The 2to3 tool will automatically adapt imports when converting your sources to Python 3.

# print
The usages of print in Python2 and Python3 are slightly different. 
 