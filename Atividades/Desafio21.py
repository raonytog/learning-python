# busca e toca um audio em mp3

from pygame import mixer

mixer.init()
mixer.music.load('glueSong.mp3')
print("starting music...")
mixer.music.set_volume(0.2)
mixer.music.play()

while (True):
    print("-"*50)
    print("Type 'p' to pause")
    print("Type 'r' to resume")
    print("Type anything else end the program")
    print("-"*50)
    
    choice = input("Type what you want: ")
    if (choice == 'p'): 
        mixer.music.pause()
        
    elif (choice == 'r'):
        mixer.music.unpause()
        
    else:
        break