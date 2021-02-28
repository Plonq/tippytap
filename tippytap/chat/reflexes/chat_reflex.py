from django.template.loader import render_to_string
from sockpuppet.channel import Channel
from sockpuppet.reflex import Reflex

from tippytap.chat.models import Message


class ChatReflex(Reflex):

    def new_message(self, text):
        user_id = self.session.get("user_id", None)
        message = Message.objects.create(text=text, user_id=user_id)

        html = render_to_string("chat_message.html", {"message": message})
        channel = Channel('chatroom')
        channel.insert_adjacent_html({
            "selector": ".chat .conversation",
            "position": "afterbegin",
            "html": html,
        })
        channel.broadcast()
