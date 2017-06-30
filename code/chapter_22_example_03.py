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

# flavors/tests/test_api.py
import json

from django.test import TestCase
from django.urls import reverse

from flavors.models import Flavor

class DjangoRestFrameworkTests(TestCase):

    def setUp(self):
        Flavor.objects.get_or_create(title='title1', slug='slug1')
        Flavor.objects.get_or_create(title='title2', slug='slug2')

        self.create_read_url = reverse('flavor_rest_api')
        self.read_update_delete_url = \
            reverse('flavor_rest_api', kwargs={'slug': 'slug1'})

    def test_list(self):
        response = self.client.get(self.create_read_url)

        # Are both titles in the content?
        self.assertContains(response, 'title1')
        self.assertContains(response, 'title2')

    def test_detail(self):
        response = self.client.get(self.read_update_delete_url)
        data = json.loads(response.content)
        content = {'id': 1, 'title': 'title1', 'slug': 'slug1',
                                            'scoops_remaining': 0}
        self.assertEquals(data, content)

    def test_create(self):
        post = {'title': 'title3', 'slug': 'slug3'}
        response = self.client.post(self.create_read_url, post)
        data = json.loads(response.content)
        self.assertEquals(response.status_code, 201)
        content = {'id': 3, 'title': 'title3', 'slug': 'slug3',
                                            'scoops_remaining': 0}
        self.assertEquals(data, content)
        self.assertEquals(Flavor.objects.count(), 3)

    def test_delete(self):
        response = self.client.delete(self.read_update_delete_url)
        self.assertEquals(response.status_code, 204)
        self.assertEquals(Flavor.objects.count(), 1)
