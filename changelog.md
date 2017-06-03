## Two Scoops of Django Changelog

This lists many, but not all the changes between TSD 1.11 and TSD 1.8.

## Note from the authors

* Added Library of Congress as agency example

## Introduction

* Moved to Python 2.7 and 3.6, with allowances for Python 3.5 and 3.4
* Explained why even though the book focuses on Python 3.6, we keep the old usage of the `super()` built-in. The reason is that switching would make the book challenging to use for all those Djangonauts still using Python 2.7. If there is a Two Scoops of Django 2.2, we'll use the terser form of `super()`
* Changed our ice cream preferences

## Chapter 1: Coding Style

* Use `implicit relative` consistently, removed use of the word `hardcoded`
* Added solution for unavoidable naming conflicts
* Moved section on `from __future__ import absolute_imports` to Appendix F
* Switched JS linter from `JSCS` to `ESLint`
* Switched CSS linter from `csscomb` to `stylelint`
* Corrected color for example 1.7
* Added the `Standard` styleguide for JS and Node
* Removed JS styleguides that have lost momentum

## Chapter 2: The Optimal Django Environment Setup

* Added GitLab as an DVCS option
* Removed mention of Mercurial
* Added reference to RealPython article on Django + Docker
* Added dockerbook.com to the list of useful Docker resources
* Removed Vagrant mention
* Warned against use of SQLite in production

## Chapter 3: How to Lay Out Django Projects

* Changed our preferred project layout to the Saurabh Kumar's "modified two-tier" design
* Removed mention of deprecated project templates
* Clarified and codified the setup text
* Removed paragraph that duplicated a tipbox
* Added missing `apps.py` module and `migrations` directory to default app layout
* Corrected wrong default project layout by running `tree` again
* Moved the description of `config/` from table 3.2 to table 3.1


## Chapter 4: Fundamentals of App Design

* Specified `db/` as a package so it wouldn't be mistaken as a directory

## Chapter 5: Settings and Requirements Files

* Switched from unipath to Pathlib
* Removed mention of Mercurial
* Added Elastic Beanstalk in examples of how to set environment variables
* In order to make the database setup example more succinct, removed the `USER`, `PASSWORD`, and `HOST` parameters
* Added `STATICFILES_DIRS` to hardcoding example
* Changed DIRS as list to tuple in examples
* Cleanup on example "Using os.path to discover project root"
* Changed adding of values to `bin/activate` to `bin/postactivate`
* Moved to consistent naming for local development settings. Specifically `local.py` or `local_pydanny.py` rather than having `dev.py` or `dev_pydanny.py`
* Added subsection on unsetting environment variables
* For windows environment variables, use `setx` instead of `set`

## Chapter 6: Model Best Practices

* Added dedicated section for migrations
* Added subsections for getting access to methods of various types during migrations
* Added subsection on RunPython.noop
* Removed mention that BinaryField was added in Django 1.8
* Removed any mention of IPAddressField
* Removed dead link to scalenpm.org
* Added choice model constants example
* Added  enum variant of choice model constants example
* Added JSONField to the list of PostgreSQL fields
* Fixed JSONField `null` and `blank` descriptions
* Added tipbox instructing that migrations must always be in version control


## Chapter 7: Queries

* Moved ORM definition to front of chapter
* Removed a number of mentions of changes that occurred in Django 1.8 or earlier
* Added tipbox about class-based model indexes
* Added subsection on chaining queries for legibility
* For the sake of clarity, changed `fun_function(**kwargs)` to `fun_function(name=None)`

## Chapter 8: Function- And Class-Based Views

* Switch from pointing out failure in the Django tutorial to the Django CBV docs
* Removed section warning about referencing views as strings in URLConf. Django thankfully removed this functionality in 1.10
* Corrected references numbers for bad examples

## Chapter 10: Best Practices for CBVs

* Renamed `PDFFlavorView` to `FlavorPDFView`
* Changed `update_users_who_favorited` to `update_user_who_favorited`
* Corrected `super()` class call in `FlavorUpdateView`
* Replaced the third introductory paragraph that mostly explained the confusion around the 1.3 era release of CBVs with a tipbox about ccbv.co.uk in the guidelines section
* Added warningbox for when overriding the `dispatch()` method of `LoginRequiredMixin`
* Use CHOICES attributes in example model

## Chapter 11: Form Patterns

* Combined imports from same module
* Referenced callables instead of just functions in custom form validators
* Added reference to abstract models in chapter 6

## Chapter 12: More Forms

* In code examples, for ultimate compatibility we switched from `import StringIO` to `from django.utils.six import StringIO`
* Refactored section on CSRF Protection
* Provided commentary on slicing of serialized data
* Added section on Custom Form Widgets


## Chapter 13: templates

* Removed subsection on template locations that duplicated the `Keep Templates Mostly in `templates/` section
* Namespace `flavors_list` to `flavors:list`
* Added tipbox advocating use of implicit context objects in templates when writing reusable code
* Corrected comment to use `objects` attribute instead of `object`

## Chapter 14: Template tags and filters

* Removed duplicate paragraph

## Chapter 15: Jinja2

* Removed Jinja2 section explaining that the Jinja2 documentation didn't accurately describe differences between DTL and Jinja2
* Corrected import errors in chapter 15 examples
* Fixed random_once comment on environment gotchas
* Changed subsection on how to use context processors as middleware to a tipbox advocating injection into the environment. This what Django recommends


## Chapter 16: Building REST APIs with Django Rest Framework

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
* Corrected description of 401 status
* "304 Unchanged" changed to "304 Not Modified"
* Mentioned built-in API docs
* Mentioned Py/JS client libs at http://www.django-rest-framework.org/topics/api-clients/
* Mentioned [Core API](http://www.coreapi.org/)
* Moved SOA discussion out. Might go to an appendix or a blog article
* Changed `core/api.py` to `core/api_urls.py` because "explicit is better than Implicit"
* Renamed `FlavorCreateReadView` and `FlavorReadUpdateDeleteView` to `FlavorListCreateAPIView` and `FlavorRetrieveUpdateDestroyAPIView`
* Fleshed out the pouring syrup RPC example
* Switched from slug to UUID for lookups as it will be more common for developers to use. Flavors and syrups are, by definition, limited in variety
* Added tipbox requesting commercial support of DRF
* Added security-related section of the process of adding custom authentication schemes
* Correct API deprecation version mismatch

## Chapter 17: Consuming REST APIs

* Removed detailed JavaScript examples of how to deal with CSRF in exchange to links to the formal documentation for each framework
* Mentioned JavaScript Fatigue
* Removed section on helping search engines crawl AJAX-rendered pages. Modern search engines have improved and this no longer relevant
* Changed CSRF section to advocate use of the DRF API client
* Added subsection for setting `CSRF_HTTP_ONLY` appropriately

## Chapter 19: Working with the Django Admin

* Changed "Don't use list\_editable in Multiuser Environments" to "Be wary of  Multiuser Environments"
* Moved in the section on securing the admin from the security chapter
* Switched from `admin.site.register` to using the `@admin.register` class decorator
* Changed SSL recommendation to TLS
* Changed `IceCreamBarAdmin` to `IceCreamBarModelAdmin`
* Removed `ADMIN_FOR` reference as that was taken out in Django 1.7
* Removed mention of use of `__unicode__()` method for Python 2.7 when that conflicts with use of `django.utils.encoding.python_2_unicode_compatible()`
* Split `__str__()` and `list_display` into two subsections
* Updated screenshots to the modern Django admin skin

## Chapter 20: Dealing with the User Model

* Removed opening paragraph about the confusion of User model practices from the pre-Django 1.5 era.
* Removed section on migrating Pre-1.5 user models to 1.5+'s custom user models
* Removed tipbox that the `User.get_profile()` method is gone, since that was removed circa 1.5.
* Shortened summary as it contained thoughts on the 1.5-era changes
* Moved warningbox about third-party packages to the end the chapter


## Chapter 21: Django's Secret Sauce: Third-Party Packages

* Added mention of Cookiecutter's integration in IDEs such as PyCharm
* Changed what is mentioned as Django project giveaways
* Mentioned that @jayfk is the current maintainer of Django Packages
* Removed tipbox with duplicate information from section 21.1
* Added link to http://djangoappschecklist.com


## Chapter 22: Testing

* Corrected method call in `add_middleware_to_response` to `process_response`
* Changed test file structure to specify nesting
* Reminded users not to use features of their IDE to structure tests
* Added a tipbox advocating that the Django testing tutorials' use of a utility function inside their tests is a mistake
* Added faker as a test data generator package

## Chapter 23: documentation

* Added [readthedocs.com](https://readthedocs.com/) as a commercial documentation service

## Chapter 24: Finding and Reducing Bottlenecks

* Updated links to modern versions of database references
* Added Redis as a potential cache store
* Added the [Unofficial MySql Optimizer Guide](http://www.unofficialmysqlguide.com)

## Chapter 25: Asynchronous Task Queues

* Added Django Channels
* Added Serverless (AWS Lambda)
* Reduced content on Redis-Q, Huey, et al. We can only write what we are using, and we haven't touched any of these in years, if at all. Of course, all general advice still applies


## Chapter 26: Security

* First section is now a reference list to security-related material in other chapters
* Added mention of Let's Encrypt
* Added Mozilla Observatory to the checkup section
* Changed section on lookups based on UUIDs to "Never Display Sequential Primary Keys"
* Removed mention of django-passwords, as it's subsumed by Django's built-in password validators
* Removed mention of django-autoadmin, as it no longer appears to be supported
* Removed warning about remove_tags. It was removed from Django in 1.10
* Added shutdown packages
* Rather than using DTL for snippets (overkill), advocated using `format_html` instead
* Moved section on securing the admin to the admin chapter
* Mentioned Insecure Direct Object References
* As it is out of scope for the book, removed edge case issue with telephone numbers as identity attack vendor.
* Content on handling security failures has been moved to Appendix H
* Explain the purpose of a strong password better
* Mentioned that DRF serializers can be used to validate incoming data
* Added section for other useful tools
  * django-restricted-sessions
  * Mozilla SSL Configuration Generator
  * Included subsection on unusual JavaScript
* Included subsection on Content Security Policy
* Discussed 2FA recovery scenarios
* Clarified risks of non-HTTPS static/media

## Chapter 27: Logging

* Described what Sentry does in greater detail and emphatically advocated its use
* Removed App Enlight as an option
* Added Opbeat as an option

## Chapter 28: Signals: Use Cases and Avoidance Techniques

* Added use case for third-party packages

## Chapter 29: What About Those Random Utilities?

* Converted slugification of non-English languages from a packagebox to its own subsection
* Changed unicode slugs to use Django's slugify function with the `allow_unicode` flag
* Added subsection for using DRF serializers for serialization of data

## Chapter 30: Deployment: Platforms as a Service

* Added Elastic Beanstalk as an PaaS option
* Added subsection on evaluating on which HTTP server a PaaS uses
* Added subsection on multiple requirements files
* Corrected wrong filename reference

## Chapter 31: Deploying Django Projects

* Updated "A Rapidly Changing World" to include Kubernetes and Mesos
* Updated pros & cons of different HTTP server setups
* Removed most Chef and Puppet references

## Chapter 32: Continuous Integration

* Changed "git or mercurial" to "GitHub or GitLab"
* Added GitLab as an option for CI
* Removed Drone, Circle, and codeship as options for CI. We haven't used any of them in a while, and Drone is out of business

## Chapter 33: Debugging

* Updated the `ALLOWED_HOSTS` subsection to reflect it's always on and that it provides a useful error message
* Mentioned that `UserBasedExceptionMiddleware` is a security concern
* Changed tipbox on `Take Care with Email Addresses` to `Take Special Care With User Data`

## Chapter 34: Asking for help

* Added tipbox about the Django Code of Conduct

## Chapter 35: Closing Thoughts

* Specified end-of-life date for Two Scoops of Django 1.11 (April 2020)

## Appendix A: Packages Used in the book

* Added a bunch of new awesome things
* Removed dead packages
* Added pipenv
* Added django-js-reverse

## Appendix C: Resources

* Focused more on up-to-date lists of of modern references

## Appendix D: Internationalization and Localization

* Added section on the challenges of time

## Appendix F: Advice for Python 2.7 Users

* Changed appendix from how to use Python 3.x to a catch-all appendix for Python 2.7 users
* Explained that Django is moving away from Python 2.7
* Covered Armin Ronacher's problems with Python 3 unicode
* Removed source encodings except for describing use with Python 2.7

## Appendix G: Security Settings reference

* Added `SECURE_CONTENT_TYPE_NOSNIFF`
* Fixed text overflow in table 35.2

## Acknowledgements

* For the sake of brevity, condensed the 1.5-era contributors down to just one section.

## Universal

* Added Appendix I: Websockets
* Grammar!
* Titlecase corrections
* Links enhancements
  * Links wrap!
  * Updated links to point to Django 1.11
  * Massive internal reference link cleanup  
* For ebooks, colorized the tip, warning, and package boxes
* For ebooks, colorized the code examples
* Switched from `braces.views.LoginRequiredMixin` to from `django.contrib.auth.mixins.LoginRequiredMixin`
* Python 3 everywhere! Some highlights:
  * All references to `__future__` are moved to Appendix F
  * Removed Python 2.7 unicode-style string declarations
  * Changed from `class MyKlass(object)` to `class MyKlass`
* When formatting allows, changed from using [2scoops.co](https://2scoops.co) for links and to using direct HTTP references. To preserve space, removed `http(s)` prefix wherever it didn't hurt formatting.
* Added mention of [GitLab](https://gitlab.com/) in places where other repo hosting options are listed. For reference, the source code for Two Scoops of Django and the review process for it has been hosted on [GitLab](https://gitlab.com/) since 2014 (Two Scoops of Django 1.6)
* Changed `from django.core.urlresolvers import reverse` to `from django.urls import reverse`
* Corrected sorting of imports across the book
* Switched from `MyKlass(object):` to `MyKlass:`
* Many inline code examples are now shaded
* Moved to single quotes for all Python examples (docstrings remain as double quotes)

## Things not done

* Decided to once again not to include a list of links to code examples within the book. Why:
  * Takes up a whopping 16 pages of the PDF
  * Confuses searching PDFs
  * The link to the code listings from the table of content insisted on going to the previous page. Even Audrey with her 15 years of LaTeX was stuck.
  * More consistent use of `python manage.py XYZ` vs `django-admin.py XYZ`
  * Code blocks are called 'Examples' in their title  
