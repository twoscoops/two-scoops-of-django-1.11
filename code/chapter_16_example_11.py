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

# sundaes/api/views.py
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Sundae, Syrup
from .serializers import SundaeSerializer, SyrupSerializer

class PourSyrupOnSundaeView(APIView):
    """View dedicated to adding syrup to sundaes"""

    def post(self, request, *args, **kwargs):
        # Process pouring of syrup here,
        # Limit each type of syrup to just one pour
        # Max pours is 3 per sundae
        sundae = get_object_or_404(Sundae, uuid=request.data['uuid'])
        try:
            sundae.add_syrup(request.data['syrup'])
        except Sundae.TooManySyrups:
            msg = "Sundae already maxed out for syrups"
            return Response({'message': msg}, status_code=400)
        except Syrup.DoesNotExist
            msg = "{}  does not exist".format(request.data['syrup'])
            return Response({'message': msg}, status_code=404)
        return Response(SundaeSerializer(sundae).data)

    def get(self, request, *args, **kwargs):
        # Get list of syrups already poured onto the sundae
        sundae = get_object_or_404(Sundae, uuid=request.data['uuid'])
        syrups = [SyrupSerializer(x).data for x in sundae.syrup_set.all()]
        return Response(syrups)
