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

import pickle
from time import sleep
import os

import scheduler


def login(web):
    # Meta business suite entry using Instagram
    web.go_to(
        "https://business.facebook.com/business/loginpage/?login_options[0]=IG")
    web.click(xpath="//div[@role='button']")

    # Changing the focus on Instagram Auth window
    main = web.driver.current_window_handle
    verifyPage = web.driver.window_handles[1]
    web.driver.switch_to.window(verifyPage)

    # Cheat waiting for login form
    while not web.exists(xpath='//*[@id="loginForm"]/div/div[1]/div/label/input'):
        sleep(2)

    # Loging in using given data
    with open(os.getcwd() + '/toInstaPost/user.txt') as user:
        web.type(user.readline().strip(), xpath='//*[@id="loginForm"]/div/div[1]/div/label/input')
        web.type(user.readline().strip(), into="Password")
    web.click(xpath="//button[@type='submit']")
    sleep(5)

    # Just a cleanup nothing hack ;)
    if web.exists('Not Now'):
        web.click('Not Now')

    # Switch back to main page for further work
    web.driver.switch_to.window(main)
    # Saving cookies for next time use
    pickle.dump(web.driver.get_cookies(), open(os.getcwd() + "\\cookies.pkl", "wb"))
    scheduler.upload(web)
