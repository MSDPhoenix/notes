from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('post_new_note',views.post_new_note),
]
