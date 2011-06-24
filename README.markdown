INTRODUCTION
===========
This is a Django utility package to handle zero or more inputs of the same name.

It is not uncommon to find a situation where you need to allow zero or more values for the same field. For example:

Enter your favorite colors:

    1.    [ red       ] [+] [-]
    2.    [ purple    ] [+] [-]
    3.    [ green     ] [+] [-]

HTML version:
    <p>Enter your favorite colors:
        <ol>
            <li>
                <input type="text" name="colors" value="red"></input> <a href="javascript: void(0)">[ + ]</a>&nbsp;<a href="javascript: void(0)">[ - ]</a>
            </li>
            <li>
                <input type="text" name="colors" value="purple"></input> <a href="javascript: void(0)">[ + ]</a>&nbsp;<a href="javascript: void(0)">[ - ]</a>
            </li>
            <li>
                <input type="text" name="colors" value="green"></input> <a href="javascript: void(0)">[ + ]</a>&nbsp;<a href="javascript: void(0)">[ - ]</a>
            </li>
        </ol>
    </p>

As an alternative to Django's Formset, you can choose to do the following with django-xfield:

**1. forms.py**

    class FavColorForm(forms.Form):
        colors = ExpandableField(fields.CharField, min_values=3, max_length=100)

**2. views.py**

    def echo_fav_colors(request):
        form = FavColorForm(request.POST)
        if form.is_valid():
            # because 'colors' is an expandable field, it returns a list of all values submitted with the name 'colors'
            colors = self.cleaned_data['colors']
            assert colors == ['red', 'purple', 'green']
            ...

django-xfield introduces 2 classes (in fact, they are closures): ExpandableField and ExpandableWidget, both are factories that return a subclass
of the class that you provide as the first positional argument. For example, "colors" is assigned a subclass of CharField that
returns a list with a minimum of 3 items/values in it.

This simplify the server-side programming as well as client-side Javascript programming.

For a list of working examples, please visit http://projs.phuihock.com/xfield/. Alternatively, you can also run the demo locally:

    $ git clone git@github.com:phuihock/django-xfield.git
    $ virtualenv.py --distribute django-xfield
    $ cd django-xfield
    $ source bin/activate
    $ pip install -r req.txt
    $ python manage.py runserver


INSTALLATION
============
    $ pip install django-xfield

This is not a Django app, so you don't have to add it to INSTALLED_APPS.


CAVEAT
======
django-xfield works with simple field types, such as CharField, IntegerField, ChoiceField - that returns a single value by default. It does **not**
support MultiValueField or any subclass of it. That said, do not use this with SplitDateTimeField or your MultiValueField subclass.


BUGS
====
What works for me may not work for me. If you find one, please file an issue.
