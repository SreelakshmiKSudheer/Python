import speech_recognition as sr

audio_file = ("Khairiyat.wav")
# use audio file as source

r = sr.Recognizer()  # initializes tge recogmiser

with sr.AudioFile(audio_file) as source :
    audio = r.record(source)
#reads the audio file

try :
    print("audio file contains " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError:
    print("Could not get the results from the Google Speech Recognition")
