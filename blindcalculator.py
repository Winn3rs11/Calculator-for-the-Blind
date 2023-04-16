import speech_recognition as sr
from gtts import gTTS
import playsound as ps
import re 

r = sr.Recognizer()

def tts(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    ps.playsound(filename)
    
def listening():
    with sr.Microphone() as source:
        print("Speak Anything :")
        r.adjust_for_ambient_noise(source, duration=0.1)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : " + text)
            return text
        except:
            tts("Sorry, could not recognize what you said. Please try saying math next time")
            
speech = listening()
word = speech.split()
print(word)
ans = eval(speech)
tts("The answer is: " + str(ans))
print("The answer is: " + str(ans))
ex_num = []
ex_op = []

for i in word:
    if re.search("[0-100]", i):
        ex_num.append(i)
    else:
        ex_op.append(i)