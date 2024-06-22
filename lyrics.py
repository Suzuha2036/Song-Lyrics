import time

def show_lyrics(lyrics, type_speed, pause):
    for char in lyrics:
        print(char, end='', flush=True)
        time.sleep(type_speed / 1000.0) 
    time.sleep(pause / 1000.0)
    print()



show_lyrics("Cause no one will love you,", 94, 210)
show_lyrics("Like her", 92, 43)
show_lyrics("It's pointless", 95, 55)
show_lyrics("Like tears in the rain", 110, 3010)
show_lyrics("So now that she's gone", 123, 410)
show_lyrics("Embrace all that comes", 134, 113)
show_lyrics("And die with a smile", 124, 213)
show_lyrics("Don't show the world how alone you've become", 174, 33)


