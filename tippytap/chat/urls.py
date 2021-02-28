from django.urls import path

from tippytap.chat.views.chat import ChatView

urlpatterns = [
    path('chat/', ChatView.as_view(), name="chat"),
]
