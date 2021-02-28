import uuid

from django.contrib.auth.models import User
from django.views.generic.base import TemplateView

from tippytap.chat.models import Message


class ChatView(TemplateView):
    template_name = 'chat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_id = self.request.session.get("user_id", None)
        if not user_id:
            user_id = User.objects.create(username=uuid.uuid4().hex.upper()[0:6]).id
            self.request.session["user_id"] = user_id
        context["user_id"] = user_id

        messages = Message.objects.all().order_by("-created")
        context['messages'] = messages

        return context
