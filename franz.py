






import time
import os

def show_lyrics(lyrics, type_speed, pause):
    for char in lyrics:
        print(char, end='', flush=True)
        time.sleep(type_speed / 1000.0) 
    time.sleep(pause / 1000.0)
    print()


os.system("cls")
show_lyrics("I gotta keep from losin' the rest of me", 60, 800)
show_lyrics("Still worry that", 60, 100)
show_lyrics("I wasted the best of me on you, babe", 80, 100)
show_lyrics("You don't care", 90, 400)

os.system("cls")
show_lyrics("Said, not tryna be a nuisance,",  50,50)
show_lyrics("it's just urgent",  50,1450)
show_lyrics("Tryna make sense of loose change",  50,50)
show_lyrics("Got me at war in my mind",  60,1250)
show_lyrics("Gotta let go of weight,",  50,50)
show_lyrics("can't keep what's holding me",  50,50)
show_lyrics("Choose to watch", 80, 60)
show_lyrics("While the world break up and fall on me",  50,1450)

os.system("cls")
show_lyrics("All the while,",  50,50)
show_lyrics("I'll await my armored fate with a smile", 50,1250)
show_lyrics("Still wanna try, still believe in",  60,550)
show_lyrics("Good days",  150,3250)
show_lyrics("Always sunny inside",  80, 1350)
show_lyrics("Good day living in my mind",  70,50)

print("\n\n\n")


