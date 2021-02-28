import { Application } from 'stimulus'
import StimulusReflex from 'stimulus_reflex'
import WebsocketConsumer from 'sockpuppet-js'
import {ChatController} from './controllers/chat.controller'
import CableReady from "cable_ready"

const application = Application.start()
const consumer = new WebsocketConsumer(`ws://${window.location.host}/ws/sockpuppet-sync`)

consumer.subscriptions.create('chatroom', {
  received (data) {
    if (data.cableReady) CableReady.perform(data.operations)
  }
})

application.register("chat", ChatController)
StimulusReflex.initialize(application, { consumer })
