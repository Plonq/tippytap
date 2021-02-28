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
        print("new_message", text)
        user_id = self.session.get("user_id", None)
        Message.objects.create(text=text, user_id=user_id)

        # Force update of all users
        channel = Channel('StimulusReflex-Channel', identifier='{"channel":"StimulusReflex::Channel"}')
        channel.dispatch_event({
            "name": "force:update",
            "selector": ".chat",
        })
        channel.broadcast()
