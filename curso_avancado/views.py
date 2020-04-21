from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContatoForm


class IndexView(TemplateView):
    template_name = 'index.html'


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(ContactView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Falha ao enviar e-mail!')
        return super(ContactView, self).form_invalid(form, *args, **kwargs)





