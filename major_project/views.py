from django.views.generic import TemplateView
class HomePage(TemplateView):
    template_name='index.html'

#class LoginView(TemplateView):
#    template_name='login.html'

class AboutView(TemplateView):
    template_name='about.html'

class ContactView(TemplateView):
    template_name='contactUs.html'
