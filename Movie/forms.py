from django import forms

from .models import movie

class movieform(forms.ModelForm):
    class Meta:
        model=movie
        fields='__all__'

class SearchMovieName(forms.Form):
    nameofthemovie=forms.CharField(label='',max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Search movie','id':'search-input'}))
    # {'id':'search-input','placeholder':'Search movie'}