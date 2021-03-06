import {BaseController} from "./base.controller";

export class ChatController extends BaseController {
  static targets = ["form", "message"]

  newMessage(event) {
    event.preventDefault()
    const text = String(this.messageTarget.value)
    if (!text.length) {
      console.debug("Text empty, aborting")
      return;
    }
    console.log("Sending message:", text)
    console.log("this", this)
    this.stimulate('ChatReflex#new_message', text).then(() => {
      this.formTarget.reset()
      this.messageTarget.focus()
    })
  }
}

