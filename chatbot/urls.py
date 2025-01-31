from django.urls import path

from . import views

urlpatterns = [
    path('', views.BotResponseView.as_view(), name='bot_response'),
]
