from django.utils.datastructures import MultiValueDict, MergeDict

def ExpandableWidgetFactory(base_widget, min_values, max_values):
    class _ExpandableWidget(base_widget):
        def __getattr__(self, name):
            return getattr(base_widget, name)

        def value_from_datadict(self, data, files, name):
            data_dict = getattr(self, 'input_type', None) == 'file' and files or data
            if isinstance(data_dict, (MultiValueDict, MergeDict)):
                values = data_dict.getlist(name)
            else:
                values = data_dict.get(name)
            return self._pad(values)

        def _pad(self, values):
            # pad values as necessary
            if not values:
                values = [''] * min_values
            elif len(values) < min_values:
                values += [''] * (min_values - len(values))
            return values

        def _render_generator_factory(self):
            def render_generator(name, values, attrs):
                # delete the 'id' key from attrs if it exists because an expandable field should not have id
                if isinstance(attrs, dict) and 'id' in attrs:
                    del attrs['id']

                values = self._pad(values)
                for v in values:  
                    yield super(_ExpandableWidget, self).render(name, v, attrs)
                else:
                    raise StopIteration
            return render_generator

        def render(self, name, values, attrs=None):
            if not hasattr(self, '_render_generator'):
                # values must be an iterator or a list
                self._render_generator = self._render_generator_factory()(name, values, attrs)

            try:
                return self._render_generator.next()
            except StopIteration:
                # when list is exhausted, render empty widget
                return super(_ExpandableWidget, self).render(name, '', attrs)
    return _ExpandableWidget


def ExpandableWidget(base_widget, min_values=0, max_values=None, **kwargs):
    """
    Given a widget, returns an expandable version of the widget.
    An expandable widget accepts zero or more values in GET or POST data. For example,

    <form name="fav_food_form">
        <input type="text" name="food"></input>
        <input type="text" name="food"></input>
        <input type="text" name="food"></input>
        ...
    </form>
    
    class FavFoodForm(forms.Form):
        food = ExpandableField(CharField, widget=ExpandableWidget(widgets.TextInput))
        ...

        def clean_food(self):
            list_of_food = self.cleaned_data['food']  # this is a list of strings
    """
    return ExpandableWidgetFactory(base_widget, min_values, max_values)(**kwargs)
