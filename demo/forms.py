from django import forms
from demo.models import Person
from dal import autocomplete


class DisabledOptionSelect(forms.Select):
    def __init__(self, attrs=None, choices=(), disabled_choices=()):
        super(forms.Select, self).__init__(attrs, choices=choices)
        self.disabled_choices = disabled_choices

    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option = super(forms.Select, self).create_option(
            name, value, label, selected, index, subindex, attrs
        )
        if value in self.disabled_choices:
            option["attrs"]["disabled"] = True
        return option


class OptionAttrSelect(forms.Select):
    def __init__(self, attrs=None, choices=()):
        super(forms.Select, self).__init__(attrs, choices=choices)

    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option = super(forms.Select, self).create_option(
            name, value, label, selected, index, subindex, attrs
        )
        option["attrs"].update({"data-foo": "bar", "data-baz": "qux"})
        return option


class SelectForm(forms.Form):
    select = forms.ChoiceField(
        choices=[("1", "one"), ("2", "two"), ("3", "three")],
        widget=forms.Select(attrs={"autofocus": True}),
    )

    select_with_initial = forms.ChoiceField(
        choices=[("1", "one"), ("2", "two"), ("3", "three")],
        widget=forms.Select(attrs={"autofocus": True}),
        initial="2",
    )

    select_with_size_attr = forms.ChoiceField(
        choices=[("1", "one"), ("2", "two"), ("3", "three")],
        widget=forms.Select(attrs={"size": 3}),
    )

    select_disabled = forms.ChoiceField(
        choices=[("1", "one"), ("2", "two"), ("3", "three")],
        widget=forms.Select(attrs={"disabled": True}),
        required=False,
    )

    select_multiple = forms.MultipleChoiceField(
        choices=[("1", "one"), ("2", "two"), ("3", "three")]
    )

    select_multiple_with_initial = forms.MultipleChoiceField(
        choices=[("1", "one"), ("2", "two"), ("3", "three")], initial=["1", "2"]
    )

    select_multiple_with_attrs = forms.MultipleChoiceField(
        choices=[("1", "one"), ("2", "two"), ("3", "three")],
        widget=forms.SelectMultiple(attrs={"data-foo": "bar"}),
    )

    select_with_custom_attrs = forms.ChoiceField(
        choices=[("1", "one"), ("2", "two"), ("3", "three")],
        widget=forms.Select(attrs={"class": "custom-class", "data-custom": "value"}),
    )

    select_with_option_attrs = forms.ChoiceField(
        choices=[
            ("1", "one"),
            ("2", "two"),
            ("3", "three"),
        ],
        widget=OptionAttrSelect(attrs={"class": "custom-class"}),
    )

    select_with_disabled_options = forms.ChoiceField(
        choices=[("1", "one"), ("2", "two"), ("3", "three")],
        widget=DisabledOptionSelect(
            attrs={"class": "custom-class"}, disabled_choices=["2"]
        ),
    )

    select_with_placeholder = forms.ChoiceField(
        choices=[("", "Select an option"), ("1", "one"), ("2", "two"), ("3", "three")],
        widget=forms.Select(attrs={"class": "custom-class"}),
    )

    grouped_select = forms.TypedChoiceField(
        choices=[
            (
                "Group 1",
                [
                    ("1", "one"),
                    ("2", "two"),
                ],
            ),
            (
                "Group 2",
                [
                    ("3", "three"),
                    ("4", "four"),
                ],
            ),
        ],
        coerce=str,
        widget=forms.Select(attrs={"class": "custom-class"}),
    )

    dal_select = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=autocomplete.ModelSelect2(url="person-autocomplete"),
    )
