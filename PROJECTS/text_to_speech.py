import gtts
import playsound
text = input("INPUT: ")
sound = gtts.gTTS(text=text,lang='en',slow=True)
sound.save("audiofile.mp3")
playsound.playsound('audiofile.mp3')