import { Controller } from 'stimulus'
import StimulusReflex from 'stimulus_reflex'

export class BaseController extends Controller {
  connect() {
    StimulusReflex.register(this)
  }
}
