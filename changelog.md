# Changes on 2017-03-17

## Chapter 1: Coding Style

* Switched JS linter from JSCS to ESLint
* Switched CSS linter from csscomb to stylelint

## Chapter 4: Fundamentals of App Design

* Specified `db/` as a package so it wouldn't be mistaken as a directory

## Chapter 5: Settings and Requirements

* Added subsection on unsetting environment variables

## Chapter 10: Best Practices for CBVs

* Renamed PDFFlavorView to FlavorPDFView

## Acknowledgements

* For the sake of brevity, condensed the 1.5-era contributors down to just one section.

## General

* Finished rebuilding the book rendering process

# Changes on 2017-03-15

## Introduction

* Explained why even though the book focuses on Python 3.6, we keep the old usage of the `super()` built-in. The reason is that switching would make the book challenging to use for all those Djangonauts still using Python 2.7. If there is a Two Scoops of Django 2.2, we'll use the terser form of `super()`

## Chapter 1: Code Style

* Added solution for unavoidable naming conflicts

## Chapter 10: Best Practices for CBVs

* Replaced the third introductory chapter that mostly explained the confusion around the 1.3 era release of CBVs with a tipbox about ccbv.co.uk in the guidelines section

## Chapter 11: Form Patterns

* Combined imports from same module
* Referenced callables instead of just functions in custom form validators

## Chapter 26: Security

* First section is now a reference list to security-related material in other chapters
* Content on handling security failures has been moved to Appendix H

## Appendix H: Handling Security Failures

## Universal

* Grammar!
* Corrected sorting of imports across the book
* Switched from `MyKlass(object):` to `MyKlass:`
* Links are wrapping!  

# Changes on 2017-03-14

## Chapter 5: Settings and Requirements

* Changed adding of values to `bin/activate` to `bin/postactivate`
* Moved to consistent naming for local development settings. Specifically `local.py` or `local_pydanny.py` rather than having `dev.py` `dev_pydanny.py`

## Chapter 7: Databases

* Moved ORM definition to front of chapter

## Chapter 19: Admin

* Moved in the section on securing the admin from the security chapter

## Chapter 26: Security

* Moved section on securing the admin to the admin chapter

## Chapter 33: Debugging

* Updated the `ALLOWED_HOSTS` subsection to reflect it's always on and that it provides a useful error message

# Changes on 2017-03-13

## Chapter 1: Coding Style

* Use `implicit relative` consistently, removed use of the word `hardcoded`

## Chapter 5: Settings and Requirement Files

* Added `STATICFILES_DIRS` to hardcoding example
* Changed DIRS as list to tuple in examples
* Cleanup on example "Using os.path to discover project root"

## Chapter 26: Security

* Mentioned Insecure Direct Object References
* As it is out of scope for the book, removed edge case issue with telephone numbers as identity attack vendor.

## General

* More consistent use of `python manage.py XYZ` vs `django-admin.py XYZ`
* Code blocks are called 'Examples' in their title
* As always, grammar corrections and enhancements
* Changed `from django.core.urlresolvers import reverse` to `from django.urls import reverse`

# Changes on 2017-03-09

## Chapter 26 Security

* Rather than using DTL for snippets (overkill), advocated using `format_html` instead

## General

* Massive external link cleanup

# Changes on 2017-03-08

## Chapter 2: Optimal Django Setup

* Removed Vagrant mention
* Added dockerbook.com to the list of useful Docker resources

## Chapter 3: Ultimate Django Setup

* Clarified and codified the setup text
* Removed paragraph that duplicated a tipbox

## Chapter 5: Settings and Requirements Files

* In order to make the database setup example more succinct, removed the `USER`, `PASSWORD`, and `HOST` parameters

## Chapter 6: Model Best Practices

* Removed dead link to scalenpm.org.

## Chapter 18

* Repaired broken comparison table and added it back to the book

## Chapter 26

* Added readthedocs.com as a commercial documentation service

## General

* Massive internal reference link cleanup
* Massive external link cleanup, ending at chapter 22

# Changes on 2017-03-06

## Note from the authors

* Added Library of Congress as agency example

## Introduction

* Changed our ice cream preferences

## Coding Style

* Got link to wrap!

## The Optimal Django Environment Setup

* Added reference to RealPython article on Django + Docker

## Form Fundamentals

* Repaired broken code example that broke the LaTeX build

## General

* Titlecase corrections
* Grammar!
* Changed more links to point to Django 1.11 references
* Figured out how to make links wrap. This will affect the layout in many places going forward



# Changes on 2017-03-03

# Introduction

* Described why we aren't using f-strings in our code examples. We'll switch to them for TSD 2.2. ;)

# Models

* Removed mention that BinaryField was added in Django 1.8
* Removed any mention of IPAddressField

# Queries

* Removed a number of mentions of changes that occurred in Django 1.8 or earlier.

## Security

* Removed warning about remove_tags. It was removed from Django in 1.10
* Added shutdown packages

## General

* Decided to once again not to include a list of links to code examples within the book. Why:
  * Takes up a whopping 16 pages of the PDF
  * Confuses searching PDFs
  * The link to the code listings from the table of content insisted on going to the previous page. Even Audrey with her 15 years of LaTeX was stuck.


# Changes up to 2017-02-28

## Introduction

* Moved to Python 2.7 and 3.6
* Described why we aren't using f-strings in our code examples. We'll switch to them in TSD 2.2. ;)

## Chapter 1 Coding Style

* Moved section on `from __future__ import absolute_imports` to Appendix F

## Chapter 2 The Optimal Django Environment Setup

* Added GitLab as an DVCS option
* Removed mention of Mercurial

## Chapter 3 How to Lay Out Django Projects

* Changed our preferred project layout to the Saurabh Kumar's "modified two-tier" design
* Removed mention of deprecated project templates

## Chapter 5 Settings and Requirements Files

* Switcedh from unipath to Pathlib
* Removed mention of Mercurial
* Added Elastic Beanstalk in examples of how to set environment variables

## Chapter 6 Model Best Practices

* Added dedicated section for migrations
* Added dedicated section on RunPython
* Added subsections for getting access to methods of various types during migrations
* Added subsection on RunPython-called functions that allow reverse migrations but do nothing
* Removed mention that BinaryField was added in Django 1.8
* Removed any mention of IPAddressField

## Chapter 7 Queries

* Removed a number of mentions of changes that occurred in Django 1.8 or earlier.

## Chapter 8 Function- and Class-Based Views

* Switch from pointing out failure in the Django tutorial to the Django CBV docs
* Removed section warning about referencing views as strings in URLConf. Django thankfully removed this functionality in 1.10.

## Chapter 10

* Corrected super() class call in FlavorUpdateView
* Changed update_users_who_favorited to update_user_who_favorited

## Chapter 15 Jinja2

* Removed Jinja2 section explaining that the Jinja2 documentation didn't accurately describe differences between DTL and Jinja2
* Corrected import errors in chapter 15 examples
* Fixed random_once comment on environment gotchas

## Chapter 16 Building REST APIs with Django Rest Framework

* Made focus of chapter Django REST Framework
* Added more hyperrefs
* Changed tutorial from adding a simple view to a walkthrough of DRF design concepts and best practices
* Added recommendation not to use sequential keys for public identifiers
* New section called 'When DRF Gets In the Way'
  * Included RPC subsection
  * New subsection on dealing with complex data
  * Advising simplification/going atomic
* Added examples to RPC subsection
* Added subsection discussing how to name API-related modules.
* Moved SOA discussion out. Might go to an appendix or a blog article

## Chapter 17

* Removed detailed JavaScript examples of how to deal with CSRF in exchange to links to the formal documentation for each framework
* Mentioned JavaScript Fatigue
* Removed section on helping search engines crawl AJAX-rendered pages. Modern search engines have improved and this no longer relevant

## Chapter 19 Working with the Django Admin

* Changed "Don't use list\_editable in Multiuser Environments" to "Be wary of  Multiuser Environments"

## Chapter 20 Dealing with the User Model

* Removed opening paragraph about the confusion of User model practices from the pre-Django 1.5 era.
* Removed section on migrating Pre-1.5 user models to 1.5+'s custom user models
* Removed tipbox that the `User.get_profile()` method is gone, since that was removed circa 1.5.
* Shortened summary as it contained thoughts on the 1.5-era changes

## Chapter 21 Django's Secret Sauce: Third-Party Packages

* Added mention of Cookiecutter's integration in IDEs such as PyCharm
* Changed what is mention as Django project giveaways

## Chapter 22 Testing

* Corrected method call in add_middleware_to_response to process_response
* Changed test file structure to specify nesting
* Remind users not to use features of their IDE to structure tests
* Added a tipbox pointing out that the Django testing tutorials' use of a utility function is a mistake
* Added faker as a test data generator package


## Chapter 24 Finding and Reducing Bottlenecks

* Updated links to modern versions of database references
* Added Redis as a potential cache store
* Added the [Unnofficial MySql Optimizer Guide](http://www.unofficialmysqlguide.com)

## Chapter 25

* Added Django Channels
* Added Serverless (AWS Lambda)
* Reduced content on Redis-Q, Huey, et al. We can only write what we are using, and we haven't touched any of these in years. Of course, all general advice still applies.

## Chapter 26 Security

* Added mention of Let's Encrypt
* Added Mozilla Observatory to the checkup section
* Changed section on lookups based on UUIDs to "Never Display Sequential Primary Keys"
* Removed mention of django-passwords, as it's subsumed by Django's built-in password validators
* Removed mention of django-autoadmin, as it no longer appears to be supported
* Removed warning about remove_tags. It was removed from Django in 1.10
* Added shutdown packages

## Chapter 27 Logging

* Described what Sentry does in greater detail and emphatically advocated its use
* Removed App Enlight as an option
* Added Opbeat as an option

## Chapter 28 Signals: Use Cases and Avoidance Techniques

* Added use case for third-party packages

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

* Title has been changed to "Two Scoops of Django 1.11 LTS"
* Subtitle is now "Best Practices for Django"
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
* Decided to once again not to include a list of links to code examples within the book. Why:
  * Takes up a whopping 16 pages of the PDF
  * Confuses searching PDFs
  * The link to the code listings from the table of content insisted on going to the previous page. Even Audrey with her 15 years of LaTeX was stuck.
