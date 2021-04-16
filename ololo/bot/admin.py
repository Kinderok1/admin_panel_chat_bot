from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe
from imagekit.admin import AdminThumbnail
from .models import Members,Items,Type
from .forms import ItemForm
from django.conf import settings

@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ["image_tag","name"]
    class Media:
        css = {
            'all': (r'C:\Users\павел\PycharmProjects\huita\ololo\bot\static\styles.css',)
        }

class MyModelAdmin(admin.ModelAdmin):
    # A template for a very customized change view:
    change_form_template = ('admin/botapp/templates/admin/botapp/change_list')

    def get_osm_info(self):
        # ...
        pass

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['osm_data'] = self.get_osm_info()
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_filter = ('type',)
    list_display = ('caption', 'image', 'description', 'type')
    form = ItemForm

admin.site.register(Type)
