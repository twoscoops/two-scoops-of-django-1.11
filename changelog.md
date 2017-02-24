# Changelog

## Introduction

* Moved to Python 2.7 and 3.5/3.6

## Chapter 1 Coding Style

* Moved section on `from __future__ import absolute_imports` to Appendix F

## Chapter 2 The Optimal Django Environment Setup

* Added GitLab as an DVCS option
* Removed mention of Mercurial

## Chapter 3 How to Lay Out Django Projects

* Changed our preferred project layout to the Saurabh Kumar's "modified 2-tier" design
* Removed mention of deprecated project templates

## Chapter 5 Settings and Requirements Files

* Switcedh from unipath to Pathlib
* Removed mention of Mercurial
* Added Elastic Beanstalk in examples of how to set environment variables

## Chapter 6

* Added dedicated section for migrations
* Added dedicated section on RunPython
* Added subsections for getting access to methods of various types during migrations
* Added subsection on RunPython-called functions that allow reverse migrations but do nothing

## Chapter 10

* Corrected super() class call in FlavorUpdateView
* Changed update_users_who_favorited to update_user_who_favorited

## Chapter 15

* Removed Jinja2 section explaining that the Jinja2 documentation didn't accurately describe differences between DTL and Jinja2
* Corrected import errors in chapter 15 examples
* Fixed random_once comment on environment gotchas

## Chapter 16

* Made focus of chapter Django REST Framework
* Added more hyperrefs
* Changed tutorial from adding a simple view to a walkthrough of DRF design concepts and best practices
* Added recommendation not to use sequential keys for public identifiers
* New section called 'When DRF Gets In the Way'
  * Included RPC subsection
  * New subsection on dealing with complex data
  * Advising simplification/going atomic
* Added examples to RPC subsection
* Moved SOA discussion out. Might go to an appendix or a blog article

## Chapter 17

* Removed detailed JavaScript examples of how to deal with CSRF in exchange to links to the formal documentation for each framework
* Mentioned JavaScript Fatigue
* Removed section on helping search engines crawl AJAX-rendered pages. Modern search engines have improved and this no longer relevant

## Chapter 22

* Corrected method call in add_middleware_to_response to process_response

## Chapter 25

* Added Django Channels
* Added Serverless (AWS Lambda)
* Reduced content on Redis-Q, Huey, et al. We can only write what we are using, and we haven't touched any of these in years. Of course, all general advice still applies.

## Chapter 26

* Added mention of Let's Encrypt

## Chapter 29 What About Those Random Utilities?

* Converted slugification of non-English languages from a packagebox to its own subsection
* Changed unicode slugs to use Django's slugify function with the allow_unicode flag
* Added subsection for using DRF serializers for serialization of data

## Chapter 30 Deployment: Platforms as a Service

* Added Elastic Beanstalk as an PaaS option
* Added subsection on evaluating on which HTTP server a PaaS uses

## Chapter 31 Deploying Django Projects

* Updated "A Rapidly Changing World" to include Kubernetes and Mesos
* Updated pros & cons of different HTTP server setups

## Chapter 32 Continuous Integration

* Changed "git or mercurial" to "GitHub or GitLab"
* Added GitLab as an option for CI
* Removed Drone, Circle, and codeship as options for CI. We haven't used any of them in a while, and Drone is out of business.

## Appendix F Advice for Python 2.7 Users

* Changed appendix from how to use Python 3.x to a catch-all appendix for Python 2.7 users
* Explained that Django is moving away from Python 2.7
* Covered Armin Ronacher's problems with Python 3 unicode

## Universal

* Grammar!
* For ebooks, colorized the tip, warning, and package boxes
* For ebooks, colorized the code examples
* Switched from braces.views.LoginRequiredMixin to from django.contrib.auth.mixins.LoginRequiredMixin
* Updated links to point to Django 1.11
* Python 3 everywhere! Some highlights:
  * All references to `__future__` are moved to Appendix F.
  * Removed Python 2.7 unicode-style string declarations
* When formatting allows, change from using 2scoops.co for links and to using direct HTTP references. To preserve space, removed `http(s)` prefix wherever it didn't hurt formatting.
* Added mention of GitLab in places where other repo hosting options are listed. For reference, the source code for Two Scoops of Django and the review process for it has been hosted on Git since 2014 (Two Scoops of Django 1.6)
