from .models import Pages

def pages(request):
    return {'pages':Pages.objects.filter(parent=None).order_by('index')}