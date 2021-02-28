from django.contrib.sessions.models import Session
from django.template.loader import render_to_string
from sockpuppet.channel import Channel
from channels.layers import get_channel_layer
from sockpuppet.reflex import Reflex

from tippytap.chat.models import Message


class ChatReflex(Reflex):

    def reload(self):
        # noop: this method exists so we can refresh the DOM
        pass

    def new_message(self, text):
        user_id = self.session.get("user_id", None)
        message = Message.objects.create(text=text, user_id=user_id)

        session_key = self.session.session_key
        session_keys = Session.objects.exclude(session_key=session_key).values_list("session_key", flat=True)
        for key in session_keys:
            html = render_to_string("chat_message.html", {"message": message})
            channel = Channel(key, identifier='{"channel":"StimulusReflex::Channel"}')
            channel.insert_adjacent_html({
                "selector": ".chat .conversation",
                "position": "afterbegin",
                "html": html,
            })
            channel.broadcast()
