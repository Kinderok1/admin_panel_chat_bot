from django import forms
from .models import Items, Members


class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('caption', 'image', 'description', 'type')
        widgets = {'caption': forms.TextInput,
                   'image': forms.TextInput,
                   'description': forms.Textarea,
                   }