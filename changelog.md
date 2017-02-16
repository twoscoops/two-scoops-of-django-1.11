# Changelog

## Introduction

* Move to Python 2.7 and 3.5/3.6

## Chapter 3

* Changed our preferred project layout to the Saurabh Kumar's "modified 2-tier" design
* Removed mention of deprecated project templates

## Chapter 10

* Corrected super() class call in FlavorUpdateView

## Chapter 15

* Removed Jinja2 section explaining that the Jinja2 documentation didn't accurately describe differences between DTL and Jinja2
* Corrected import errors in chapter 15 examples
* Fixed random_once comment on environment gotchas

## Chapter 16

* Made focus of chapter Django REST Framework
* Added more hyperrefs
* Moved SOA discussion out. Might go to an appendix or a blog article

## Chapter 17

* Removed detailed JavaScript examples of how to deal with CSRF in exchange to links to the formal documentation for each framework
* Mentioned JavaScript Fatigue

## Chapter 22

* Corrected method call in add_middleware_to_response to process_response

## Chapter 25

* Added Django Channels
* Added Serverless (AWS Lambda)
* Reduced content on Redis-Q, Huey, et al. We can only write what we are using, and we haven't touched any of these in years. Of course, all general advice still applies.

## Chapter 29

* Converted slugification of non-English languages from a packagebox to its own subsection

## Appendix F

* Change from using Python 3.x with Django to using Python 2.7

## Universal

* Grammar!
* For ebooks, colorized the tip, warning, and package boxes
* For ebooks, colorized the code examples
* Switched from braces.views.LoginRequiredMixin to from django.contrib.auth.mixins.LoginRequiredMixin
* Updated links
* Python 3 everywhere! All references to `__future__` are moved to Appendix F
* When formatting allows, change from using 2scoops.co for links and to using direct HTTP references. 
