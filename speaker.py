import pyttsx3

class speaker():

    def __init__(self, VOICE_ID=0):
        self.speak_module = pyttsx3.init()
        self.voices = self.speak_module.getProperty("voices")
        self.speak_module.setProperty('voice', self.voices[VOICE_ID].id)

    def talk(self, msg):
        self.speak_module.say(msg)
        self.speak_module.runAndWait()