"""
Using This Code Example
=========================

The code examples provided are provided by Daniel Greenfeld and Audrey Roy of
Two Scoops Press to help you reference Two Scoops of Django: Best Practices
for Django 1.11. Code samples follow PEP-0008, with exceptions made for the
purposes of improving book formatting. Example code is provided "as is", and
is not intended to be, and should not be considered or labeled as "tutorial
code".

Permissions
============

In general, you may use the code we've provided with this book in your
programs and documentation. You do not need to contact us for permission
unless you're reproducing a significant portion of the code or using it in
commercial distributions. Examples:

* Writing a program that uses several chunks of code from this course does
    not require permission.
* Selling or distributing a digital package from material taken from this
    book does require permission.
* Answering a question by citing this book and quoting example code does not
    require permission.
* Incorporating a significant amount of example code from this book into your
    product's documentation does require permission.

Attributions usually include the title, author, publisher and an ISBN. For
example, "Two Scoops of Django: Best Practices for Django 1.11, by Daniel
Roy Greenfeld and Audrey Roy Greenfeld. Copyright 2017 Two Scoops Press
(978-0-692-91572-1)."

If you feel your use of code examples falls outside fair use of the permission
given here, please contact us at info@twoscoopspress.org.
"""

from unittest import mock, TestCase

import icecreamapi

from flavors.exceptions import CantListFlavors
from flavors.utils import list_flavors_sorted

class TestIceCreamSorting(TestCase):

    # Set up monkeypatch of icecreamapi.get_flavors()
    @mock.patch.object(icecreamapi, 'get_flavors')
    def test_flavor_sort(self, get_flavors):
        # Instructs icecreamapi.get_flavors() to return an unordered list.
        get_flavors.return_value = ['chocolate', 'vanilla', 'strawberry', ]

        # list_flavors_sorted() calls the icecreamapi.get_flavors()
        #   function. Since we've monkeypatched the function,  it will always
        #   return ['chocolate', 'strawberry', 'vanilla', ]. Which the.
        #   list_flavors_sorted() will sort alphabetically
        flavors = list_flavors_sorted()

        self.assertEqual(
            flavors,
            ['chocolate', 'strawberry', 'vanilla', ]

        )
