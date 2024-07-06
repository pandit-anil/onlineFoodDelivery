from . models import SystemSetting

def System(request):
    sys = SystemSetting.objects.first()
    return {'sys':sys}