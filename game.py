import speech_recognition as sr
import random

mic = sr.Microphone()
recog = sr.Recognizer()
# Here score
score = 0

def playgame(emh):
    global score
    # This is your dictionary of your random words and complexities that you write in function arguments.
    levels = {

    "easy": ["dairy", "Mouse", "computer"],
    "medium": ["programming", "algorithm", "developer"],
    "hard": ["neural network", "machine learning", "artificial intelligence"]

    }   
    # Does this variable give you a random word
    LEL = random.choice(levels[emh])
    # This code will ask you for a random word.
    print("Please say ", LEL, " " * 40, "Score ", score)
    # The code here means voice recognition 
    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        res = recog.recognize_google(audio, language='en-EN')
    # This print() means that you speak.
    print(res)
    # Here are the conditions for evaluation.
    if res == LEL :
        print("Amazing.")
        score = score + 1
    elif score < 1 :
        print("GAME OVER")
        return 0
    else:
        print("BAD")
        score = score - 1

while True:
    playgame('easy')
