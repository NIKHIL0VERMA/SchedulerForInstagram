#  Copyright (c)  2023-2023, Nikhil Verma
#
#  This file was last modified at 3/9/23, 5:12 PM
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import os
from webbot import Browser
import authHandler
import scheduler
import pickle

web = Browser()
if not os.path.isfile(os.getcwd() + '\\toInstaHelper.exe'):
    web.driver.quit()
    quit("Can't find Helper to upload file. Please recheck from git")

if os.path.isfile(os.getcwd() + '\\cookies.pkl'):
    web.go_to('https://business.facebook.com/')
    cookies = pickle.load(open(os.getcwd() + "\\cookies.pkl", "rb"))
    for cookie in cookies:
        web.driver.add_cookie(cookie)
    scheduler.upload(web)
else:
    authHandler.login(web)
