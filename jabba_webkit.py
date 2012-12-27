#!/usr/bin/env python

"""
Jabba's headless webkit browser for scraping AJAX-powered webpages.

by Laszlo Szathmary alias Jabba Laci (jabba.laci@gmail.com)
https://ubuntuincident.wordpress.com/
http://pythonadventures.wordpress.com/

Usage: jabba_webkit.py <url> [<time>]

url:  the page whose source you want to get
time: The application will quit after this given time (in seconds).
      If the webpage is AJAX-powered and updates itself, you can
      tell this browser to wait X seconds. Then it fetches the
      _generated_ HTML source.

You can also use it as a library:

>>> import jabba_webkit as jw
>>> html1 = jw.get_page(url1, time1)
>>> html2 = jw.get_page(url2)    # yes, you can call several times

# import jabba_webkit as jw
"""

__version__ = '20121227'

import os
import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import QWebPage

SEC = 1000    # 1 sec. is 1000 msec.
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0'


class JabbaWebkit(QWebPage):
    # 'html' is a class variable

    def __init__(self, url, wait, app, parent=None):
        super(JabbaWebkit, self).__init__(parent)
        JabbaWebkit.html = ''

        if wait:
            QTimer.singleShot(wait * SEC, app.quit)
        else:
            self.loadFinished.connect(app.quit)

        self.mainFrame().load(QUrl(url))

    def save(self):
        JabbaWebkit.html = self.mainFrame().toHtml()

    def userAgentForUrl(self, url):
        return USER_AGENT


def get_page(url, wait=None):
    # here is the trick how to call it several times
    app = QApplication.instance() # checks if QApplication already exists
    if not app: # create QApplication if it doesnt exist
        app = QApplication(sys.argv)
    #
    form = JabbaWebkit(url, wait, app)
    app.aboutToQuit.connect(form.save)
    app.exec_()
    return JabbaWebkit.html

#############################################################################

if __name__ == "__main__":
#    url = 'http://simile.mit.edu/crowbar/test.html'
#    print get_html(url)

#    url = 'http://www.ncbi.nlm.nih.gov/nuccore/CP002059.1'    # wait 30 seconds
#    print get_html(url, 30)

    try:
        if len(sys.argv) == 3:
            print get_page(sys.argv[1], int(sys.argv[2]))
        elif len(sys.argv) == 2:
            print get_page(sys.argv[1])
        else:
            raise ValueError
    except ValueError:
        print "Usage: {0} <url> [<time_in_sec>]".format(os.path.basename(sys.argv[0]))
        sys.exit(1)
