#!/usr/bin/env python

import os
import http.cookies as cookies

print("Content-type: text/html\n\n")

print("""
<html>
<body>
<h1>Display cookies</h1>
""")

if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ.get('HTTP_COOKIE')

    cookieList = os.environ['HTTP_COOKIE']
    print(cookieList)

    cookieList = cookieList.split('; ')
    print(cookieList)

    for cookie in cookieList:
        c = cookies.SimpleCookie()
        c.load(cookie)
        print(c)

print("""
</body>
</html>
""")