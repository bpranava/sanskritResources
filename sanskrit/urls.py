from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('ramayana/',views.ramayana,name='ramayana')
]