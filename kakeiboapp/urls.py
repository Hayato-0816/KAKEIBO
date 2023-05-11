from django.urls import path
from . import views

urlpatterns = [
    path('top/<int:pk>', views.BaseClass.as_view()),
]