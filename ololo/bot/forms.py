from django import forms
from .models import Items, Members,MembersList,Sendler
from django.template import loader
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget

from django.conf import settings

class BootstrapInputWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(
                '<a href="{}" target="_blank"><img src="{}" width="160" height="160" alt="{}" "/></a>'.
                    format(image_url, image_url, file_name))
        output.append(super().render(name, value, attrs))
        return mark_safe(u''.join(output))

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('caption', 'image', 'description', 'type')
        widgets = {'caption': forms.TextInput,
                   'description': forms.Textarea,
                   'image': BootstrapInputWidget()
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

class MessageForm(forms.Form):
    msg = forms.CharField()

class MembersForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MembersForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs['readonly'] = True
    class Meta:
        model = Members
        fields = ('image', 'name', 'id_t', 'user_state', 'link_id')
        widgets = {
                   'image': BootstrapInputWidget()
                   }
