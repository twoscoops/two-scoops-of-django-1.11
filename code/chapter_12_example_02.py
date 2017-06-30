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

import csv

from django.utils.six import StringIO

from django import forms

from .models import Purchase, Seller

class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase

    def clean_seller(self):
        seller = self.cleaned_data['seller']
        try:
            Seller.objects.get(name=seller)
        except Seller.DoesNotExist:
            msg = '{0} does not exist in purchase #{1}.'.format(
                seller,
                self.cleaned_data['purchase_number']
            )
            raise forms.ValidationError(msg)
        return seller

def add_csv_purchases(rows):

    rows = StringIO.StringIO(rows)

    records_added = 0
    errors = []
    # Generate a dict per row, with the first CSV row being the keys.
    for row in csv.DictReader(rows, delimiter=','):

        # Bind the row data to the PurchaseForm.
        form = PurchaseForm(row)
        # Check to see if the row data is valid.
        if form.is_valid():
            # Row data is valid so save the record.
            form.save()
            records_added += 1
        else:
            errors.append(form.errors)

    return records_added, errors

