import speech_recognition
import pyttsx3

class VoiceAi():
    def __init__(self):
        self.recognizer=speech_recognition.Recognizer()

    def listen_voice(self):
        print("run")
        while True:
            try:
                print("HEre we go")
                with speech_recognition.Microphone() as mic:
                    print('listinging')
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio=self.recognizer.listen(mic)
                    
                    text=self.recognizer.recognize_google(audio)
                    text=text.lower()
                    print(text)
                    break
            except:
                self.recognizer=speech_recognition.Recognizer()
                continue