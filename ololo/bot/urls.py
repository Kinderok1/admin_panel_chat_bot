from django.urls import path, include

from .views import notifications,post,settings

urlpatterns = [

    path('settings', settings, name='settings'),
    path('', notifications, name='notifications'),

    path('/bot/account_action', post, name='sad')

]