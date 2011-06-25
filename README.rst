INTRODUCTION
============
This is a Django utility package to handle zero or more form inputs of the same name.

It is not uncommon to find a situation where you need to allow zero or more values for the same field. For example:

Enter your favorite colors:

::

    1.    [ red       ] [+] [-]
    2.    [ purple    ] [+] [-]
    3.    [ green     ] [+] [-]

As an alternative to Django's Formset, you can choose to do the following with django-xfield:

::

    # forms.py
    class FavColorForm(forms.Form):
        colors = ExpandableField(fields.CharField, min_values=3, max_length=100)

::

    # views.py
    def echo_fav_colors(request):
        form = FavColorForm(request.POST)
        if form.is_valid():
            # because 'colors' is an expandable field, it returns a list of all values submitted by the name 'colors'
            colors = self.cleaned_data['colors']
            assert colors == ['red', 'purple', 'green']
            ...

django-xfield introduces 2 classes (they are closures in disguise): ``ExpandableField`` and ``ExpandableWidget``, both are factories that return a subclass
of the class that you provide as the first positional argument. ``ExpandableField`` accepts 2 optional arguments - ``min_values`` and ``max_values`` and pass the
rest of the arguments, if provided, to the actual field class for initialization. 

``min_values``
    the minimum number of values that user must provided, default to 0

``max_values``
    the maximum number of values that user can supply, default to None (**WARNING** not implemented)

For example, "colors" is assigned a subclass of CharField that returns a list with a minimum of 3 items/values in it. 

Just like a normal field, you can supply a different widget if the default is not what you want. However, the widget must be an instance of the
class that ``ExpandableWidget`` returns (recall that ``ExpandableWidget`` is a closure, not a class). For example:

::

    class FavColorForm(forms.Form):
        colors = ExpandableField(fields.CharField, min_values=3, max_length=100, widget=ExpandableWidget(Textarea, min_values=3))
    
**NOTE** It is necessary to pass the same ``min_values``/``max_values`` if you are supplying a custom ``ExpandableWidget``.

This simplify the server-side as well as client-side (Javascript) programming. For a list of working examples, please visit http://demo.phuihock.com/xfield/.
Alternatively, you can also run the demo locally:

::

    $ git clone git://github.com/phuihock/django-xfield.git
    $ virtualenv --distribute django-xfield
    $ cd django-xfield
    $ source bin/activate
    $ pip install -r req.txt
    $ python manage.py runserver

Then, go to http://127.0.0.1:8000/

What works for me may not work for everyone else. If you find this utility useful and need example of specific use case, I'll be glad to provide some.
Also, checkout the demo app.

INSTALLATION
============

::

    $ pip install django-xfield

This is not a Django app, so you don't have to add it to INSTALLED_APPS.


CAVEAT
======
django-xfield works with simple field types, such as CharField, IntegerField, ChoiceField - that returns a single value. It does **not**
support MultiValueField or any subclass of it. That said, do not use this with SplitDateTimeField or your MultiValueField subclass.


BUGS
====
Likely. If you find one, please file an issue.


TODO
====
This should go to issues, but just for the record, this thing needs tests, a lot of tests.
