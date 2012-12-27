Jabba-Webkit
============

Jabba's headless webkit browser for scraping AJAX-powered webpages.

* Author: Laszlo Szathmary, 2012 (<jabba.laci@gmail.com>)
* Blog post: <http://ubuntuincident.wordpress.com/2012/12/27/scraping-ajax-web-pages-part-4/>
* GitHub: <https://github.com/jabbalaci/Jabba-Webkit>

Usage:
------
`jabba_webkit.py <url> [<time>]`

`url`: the page whose source you want to get

`time`: The application will quit after this given time (in seconds).

If the webpage is AJAX-powered and updates itself, you can
tell this browser to wait X seconds. Then it fetches the
*generated* HTML source.

You can also use it as a library:

    >>> import jabba_webkit as jw
    >>> html1 = jw.get_page(url1, time1)
    >>> html2 = jw.get_page(url2)    # yes, you can call it several times