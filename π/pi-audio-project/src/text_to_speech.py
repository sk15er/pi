class TextToSpeech:
    def __init__(self):
        import pyttsx3
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def save_audio(self, filename):
        import pyttsx3
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()