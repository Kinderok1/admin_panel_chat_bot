from django.contrib import admin
from django.utils.translation import ngettext
from django.contrib import messages
from django.urls import path, reverse
from django.utils.html import format_html

# Register your models here.
from django.utils.safestring import mark_safe
from imagekit.admin import AdminThumbnail
from .models import Members, Items, Type, MembersList, Sendler, Notifications, Messages
from .forms import ItemForm, MembersListForm,SendlerForm
from django.conf import settings
from django.template.response import TemplateResponse




class MembersAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "name", 'user_state', 'members_actions']
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


    # def get_actions(self, request):
    #     '''эта функция отключает возможность удалить пользователей'''
    #     actions = super().get_actions(request)
    #     del actions['delete_selected']
    #     return actions

    def get_urls(self):  # create path
        urls = super().get_urls()

        custom_urls = [
            # path(
            #     '<int:account_id>/messages',
            #     self.admin_site.admin_view(self.members_messages),
            #     name='account-deposit',
            # ),
            path('<int:account_id>/messages',
                 self.admin_site.admin_view(self.members_messages, cacheable=True),
                 name='account-deposit')
        ]
        return custom_urls + urls

    def members_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Сообщения</a> ',
            reverse('admin:account-deposit', args=[obj.pk]),  # по имени шаблона ищет юрл адрес
        )

    members_actions.short_description = 'Сообщения подписчика'
    members_actions.allow_tags = True

    def members_messages(self, request, account_id, *args, **kwargs):
        return self.process_action(
            request=request,
            account_id=account_id,
            action_title='Сообщения:',
        )

    def process_action(
            self,
            request,
            account_id,
            action_title
    ):
        '''Это своеобразное вью администратора'''
        if request.method == 'POST':
            member = Members.objects.get(pk=account_id)
            entites = Messages(owner=member, to_user_msg=request.POST['msg'])
            entites.save()

        context = self.admin_site.each_context(request)

        context['opts'] = self.model._meta
        context['title'] = action_title

        messages = Messages.objects.filter(owner=account_id)
        context['entries'] = messages
        print(context)

        return TemplateResponse(
            request,
            'admin/account_action.html',
            context,
        )


class ItemsAdmin(admin.ModelAdmin):
    list_filter = ('type',)
    list_display = ('caption', 'image', 'description', 'type')
    form = ItemForm

class MembersListAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    form = MembersListForm

    def has_add_permission(self, request, obj=None):
        '''hide add model button'''
        return False

class SendlerAdmin(admin.ModelAdmin):
    list_display = ('header', 'text', 'members_list', 'status', 'image_tag')
    form = SendlerForm
    change_form_template = settings.BASE_DIR + "/bot/templates/admin/bot/Sendler/change_form.html"

class TypeAdmin(admin.ModelAdmin):
    pass

class NotificationsAdmin(admin.ModelAdmin):

    def has_module_permission(self, request):
        return False
    # def has_add_permission(self, request, obj=None):
    #     return False







admin.site.register(Items, ItemsAdmin)
admin.site.register(MembersList, MembersListAdmin)
admin.site.register(Members, MembersAdmin)
admin.site.register(Sendler, SendlerAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Notifications, NotificationsAdmin)
admin.site.enable_nav_sidebar = False

