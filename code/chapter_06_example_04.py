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

from django.db import migrations, models

def add_cones(apps, schema_editor):
    Scoop = apps.get_model('scoop', 'Scoop')
    Cone = apps.get_model('cone', 'Cone')

    for scoop in Scoop.objects.all():
        Cone.objects.create(
            scoop=scoop,
            style='sugar'
        )

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scoop', '0051_auto_20670724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=10),
                    choices=[('sugar', 'Sugar'), ('waffle', 'Waffle')]),
                ('scoop', models.OneToOneField(null=True, to='scoop.Scoop'
                    on_delete=django.db.models.deletion.SET_NULL, )),
            ],
        ),
        # RunPython.noop does nothing but allows reverse migrations to occur
        migrations.RunPython(add_cones, migrations.RunPython.noop)
    ]
