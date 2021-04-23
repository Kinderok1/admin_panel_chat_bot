from .models import Notifications
from .models import Members

def notifications(request):

    if request.user.is_authenticated:
        n = Notifications.objects.filter(is_read=False)
        return {'notifications': n}
    else:
        return {'notifications': []}