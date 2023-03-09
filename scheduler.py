#  Copyright (c)  2023-2023, Nikhil Verma
#
#  This file was last modified at 3/9/23, 5:03 PM
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


from time import sleep
from datetime import timedelta, date
import os
import subprocess


def upload(web):
    # Looping the photos to post
    dy = int(input("कितने दिन बाद से शेड्यूल करे ??"))
    folder_dir = os.getcwd() + "\\toInstaPost\\"
    for images in os.listdir(folder_dir):
        if images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg"):
            sleep(7)  # Optimization for queue
            web.go_to(
                'https://business.facebook.com/latest/composer/?asset_id=108807775422878&ref=biz_web_content_manager_calendar_view&context_ref=CONTENT_CALENDAR')
            sleep(5)
            web.click('फ़ोटो जोड़ें')
            photo = folder_dir + images
            args = os.getcwd() + '\\toInstaHelper.exe ' + photo
            subprocess.run(args)
            webElement = web.driver.find_element_by_xpath(
                '//div[@aria-label="अपनी पोस्ट में टेक्स्ट शामिल करने के लिए डायलॉग बॉक्स में लिखें."]')
            with open(os.getcwd() + '\\toInstaPost\\tags.txt') as f:
                webElement.send_keys(f.read(), web.Key.TAB, web.Key.TAB, web.Key.TAB, web.Key.TAB, web.Key.ENTER)
            sleep(3)
            os.remove(photo)  # Deleting uploaded photos
            dateForm = web.driver.find_element_by_xpath('//input[@placeholder="dd-mm-yyyy"]')
            dateForm.click()
            Date_req = date.today() + timedelta(days=dy)
            dateForm.send_keys(web.Key.CONTROL + 'a', web.Key.BACKSPACE)
            dateForm.send_keys(Date_req.strftime("%d-%m-%Y"))
            dy = dy + 1
            amOrpm = web.driver.find_element_by_xpath('//input[@aria-valuemin="0"][@aria-valuemax="1"]')
            # Don't try to optimize plz!!!
            if amOrpm.get_attribute('aria-valuenow') == '0':
                web.driver\
                    .find_element_by_xpath('//input[@role="spinbutton"][@aria-label="hours"]')\
                    .send_keys("11",
                               web.Key.TAB,
                               "00",
                               web.Key.TAB,
                               web.Key.TAB,
                               web.Key.TAB,
                               web.Key.TAB,
                               web.Key.ENTER)
            else:
                web.driver\
                    .find_element_by_xpath('//input[@role="spinbutton"][@aria-label="hours"]')\
                    .send_keys("11",
                               web.Key.TAB,
                               "00",
                               web.Key.TAB,
                               web.Key.UP,              # Converting to AM
                               web.Key.TAB,
                               web.Key.TAB,
                               web.Key.TAB,
                               web.Key.ENTER)
    web.driver.quit()
