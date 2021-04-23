from django.urls import path, include

from .views import notifications,post

urlpatterns = [
    path('', notifications, name='notifications'),
    path('/bot/account_action',post,name='sad')

]