from django.urls import path
from .views import IndexView, ContactView, AboutView, Handler405

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato', ContactView.as_view(), name='contato'),
    path('sobre', AboutView.as_view(), name='sobre'),
    path('error', Handler405.as_view(), name='error'),

]