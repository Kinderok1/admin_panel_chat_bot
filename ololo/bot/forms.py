from django import forms
from .models import Items, Members,MembersList,Sendler


class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('caption', 'image', 'description', 'type')
        widgets = {'caption': forms.TextInput,
                   'image': forms.TextInput,
                   'description': forms.Textarea,
                   }
class MembersListForm(forms.ModelForm):
    class Meta:
        model = MembersList
        fields = ('name',)

class SendlerForm(forms.ModelForm):
    class Meta:
        model = Sendler
        fields = ('header', 'text', 'members_list','send_date', 'image')
        widgets = {'text': forms.Textarea, }