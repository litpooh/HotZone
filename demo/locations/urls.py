from django.urls import path

from . import views

urlpatterns = [
    path('find/', views.SearchingLocation.as_view(), name='find'),
    path('results/', views.find, name='results'),
    path('save/', views.save, name='save'),
]
