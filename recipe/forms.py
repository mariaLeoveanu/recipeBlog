from django.forms import ModelForm
from .models import Recipe
from django import forms


class RecipeForm(ModelForm):
    overview = forms.CharField(widget=forms.Textarea, label='Recipe overview: ')

    class Meta:
        model = Recipe
        fields = ['name', 'overview', 'ingredients', 'duration', 'preparation', 'type', 'image']
    
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'style': 'width: 50%'})
        self.fields['overview'].widget.attrs.update({'style': 'width: 100%; padding: 15px;'})
        self.fields['ingredients'].widget.attrs.update({'style': 'width: 100%;padding: 15px;'})
        self.fields['duration'].widget.attrs.update({'style': 'width: 50%;'})
        self.fields['preparation'].widget.attrs.update({'style': 'width: 100%;padding: 15px;'})
        self.fields['image'].widget.attrs.update({'style': 'margin-bottom:5px;'})





