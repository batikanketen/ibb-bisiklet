from .models import Settings

def settings(request):
    context = Settings.objects.first()
    return {'setting': context}
