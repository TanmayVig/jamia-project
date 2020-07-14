from django.views import generic

class Index(generic.TemplateView):
    template_name='index.html'

class Thanks(generic.TemplateView):
    template_name='thanks.html'
    
