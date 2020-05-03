from mycroft import MycroftSkill, intent_file_handler


class AudioPlayer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('player.audio.intent')
    def handle_player_audio(self, message):
        self.speak_dialog('player.audio')


def create_skill():
    return AudioPlayer()

