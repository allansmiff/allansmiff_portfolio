from django.urls import path
from .views import IndexView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato', ContactView.as_view(), name='contato'),

]