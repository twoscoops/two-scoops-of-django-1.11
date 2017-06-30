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

# vouchers/managers.py
from django.db import models
from django.utils import timezone

from dateutil.relativedelta import relativedelta

class VoucherManager(models.Manager):
    def age_breakdown(self):
        """Returns a dict of age brackets/counts."""
        age_brackets = []
        now = timezone.now()

        delta = now - relativedelta(years=18)
        count = self.model.objects.filter(birth_date__gt=delta).count()
        age_brackets.append(
            {'title': '0-17', 'count': count}
        )
        count = self.model.objects.filter(birth_date__lte=delta).count()
        age_brackets.append(
            {'title': '18+', 'count': count}
        )
        return age_brackets
