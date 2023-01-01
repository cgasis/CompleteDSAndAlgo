lurk
====

A script which extracts HTML from web pages that match a certain CSS pattern.
::

    $ pip install lurk

=====
usage
=====

**in python**

In python, lurk returns a dictionary:

::

    from lurk import lurk

    for link in lurk('http://en.wikipedia.org/wiki/en', 'a'):
        if 'href' in link:
            print link['href']

**in bash**

In bash, lurk returns JSON.

Familiarize yourself with `CSS attribute selectors <https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors>`_.

::

    $ lurk \
    http://www.gnu.org/software/libc/manual/html_node/Function-Index.html \
    'a[href*="#index-"]' \
    > links.json

This command saves a JSON object containing an array of links to all GNU C functions into **links.json**:

::

    [
      {
        "code": "*pthread_getspecific",
        "href": "Thread_002dspecific-Data.html#index-_002apthread_005fgetspecific"
      },

      {
        "code": "*sbrk",
        "href": "Resizing-the-Data-Segment.html#index-_002asbrk"
      },

      // ...
    ]


