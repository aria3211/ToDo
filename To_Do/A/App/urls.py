from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('delete/<int:id>', views.Delete, name='Delete'),
    path('uncomplete/<int:id>', views.InComplete, name='InComplete'),
    path('complete/<int:id>', views.Complete, name='Complete'),
]
