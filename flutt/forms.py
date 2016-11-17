from django import forms
from .models import Flutt

class FluttForm(forms.ModelForm):
    """
    Form for posting a flutt
    """

    class Meta:
        model = Flutt
        fields = ('author', 'body')

class SearchForm(forms.Form):
    """
    Basic search form
    """
    query_text = forms.CharField(max_length=128)
