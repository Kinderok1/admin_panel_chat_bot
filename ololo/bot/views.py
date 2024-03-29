from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from .forms import MessageForm
from .models import Notifications, Messages, Members

def settings(request):
    '''do smthng'''
    template = loader.get_template('bot/settings.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def post(self, request):
    user_form = MessageForm()
    return render(request,'admin/account_action.html')



def notifications(request):
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)
    owner_id = request.GET.get('extra_id', 0)

    if goto != '':
        #обновляем информацию.Помечаем нотификацию прочитанной
        context={}
        notification = Notifications.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()

        owner = Members.objects.get(id_t=owner_id)
        messages = Messages.objects.filter(owner=owner.pk)
        context['entries'] = messages
        # return TemplateResponse(
        #     request,
        #     'admin/account_action.html',
        #     context
        # )
        url = reverse(
            'admin:account-deposit',
            args=[owner.pk],
            current_app='message',
        )
        return HttpResponseRedirect(url)

    return render(request, 'admin/bot/Notifications/change_form.html')
