from django.contrib import admin
from django.utils.translation import ngettext
from django.contrib import messages


# Register your models here.
from django.utils.safestring import mark_safe
from imagekit.admin import AdminThumbnail
from .models import Members, Items, Type, MembersList, Sendler
from .forms import ItemForm, MembersListForm,SendlerForm
from django.conf import settings




#@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "name"]
    actions = ['make_list']
    class Media:
        css = {
            'all': (r'C:\Users\павел\PycharmProjects\huita\ololo\bot\static\styles.css',)
        }

    @admin.action(description='Создать список для рассылки')
    def make_list(self, request, queryset):
        '''эта функция добавляет возможность сделать список пользователей'''
        updated = 0
        id_list = ''
        for obj in queryset:
            id_list += obj.id_t + ','
            updated += 1

        to_write = MembersList()
        to_write.name = 'DEFAULT'
        to_write.id_s_list = id_list
        to_write.save()

        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)


    def get_actions(self, request):
        '''эта функция отключает возможность удалить пользователей'''
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions


#@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_filter = ('type',)
    list_display = ('caption', 'image', 'description', 'type')
    form = ItemForm

#@admin.register(MembersList)
class MembersListAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    form = MembersListForm

    def has_add_permission(self, request, obj=None):
        return False

class SendlerAdmin(admin.ModelAdmin):
    list_display = ('header', 'text', 'members_list', 'status', 'image_tag')
    form = SendlerForm
    change_form_template = settings.BASE_DIR + "/bot/templates/admin/bot/Sendler/change_form.html"



admin.site.register(Items, ItemsAdmin)
admin.site.register(MembersList, MembersListAdmin)
admin.site.register(Members, MembersAdmin)
admin.site.register(Sendler, SendlerAdmin)

