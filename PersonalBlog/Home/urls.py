from django.urls import include, path

from . import views

urlpatterns = [
    #Funciones view
    #path('', views.index, name='index'),
    #Class-based views
    path('', views.Index.as_view(), name='index'),
    path('about/', views.About.as_view(), name='about'),
]
