from django.urls import path
from django.views.generic import TemplateView
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.HelloView.as_view())
]
