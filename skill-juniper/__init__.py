from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from mycroft.util.log import getLogger
LOGGER = getLogger(__name__)


class Juniper_skill(MycroftSkill):
    def __init__(self):
        super(WikipediaSkill, self).__init__(name="Juniper_skill")

    @intent_handler(IntentBuilder("").require("Query").require("juniper").require("health"))
    def handle_intent(self, message):
        # Extract what the user asked about
        self.speak_dialog("good")



def create_skill():
    return Juniper_skill()


