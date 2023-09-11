from django.urls import path
from . import views


urlpatterns =[
  path('api/', views.StackApiView),
  path('api/<str:name_or_pk>/',views.EditStackApiView)
]

