import winsound
import os
import time
import platform
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    else:
        return

os.chdir("Music/")
while True:
    clear()
    playlist = []
    print("PyPlayer by JuanR4140")
    print("---")
    print("1. Play a Song")
    print("2. Look at Songs Available")
    print("3. Make a PlayList")
    print("4. Change Directory")
    print("5. Exit PyPlayer")
    option = input("> ")
    if option == "1":
        clear()
        print("would you like to type in the name of a song or choose one by typing a number?")
        print("1. Type Manually")
        print("2. Choose from List")
        optionMusic = input("> ")
        if optionMusic == "1":
            clear()
            print("enter song name:")
            songName = input("> ")
            print("Currently Playing: " + songName)
            winsound.PlaySound(songName, winsound.SND_FILENAME)
        elif optionMusic == "2":
            clear()
            currentDir = os.listdir(".")
            print("type the number of the song you wanna play\n")
            print("----------------------------------------------\n")
            counter = 1
            for musicFile in currentDir:
                print(str(counter) + ". " + musicFile + "\n")
                int(counter)
                counter += 1
            print("----------------------------------------------")
            bsongNum = input("> ")
            print("playing track #" + bsongNum + " of list..")
            try:
                songNum = int(bsongNum)
                songNum = songNum - 1
            except ValueError:
                print("error.")
            try:
                print("Currently Playing: " + currentDir[songNum])
            except NameError:
                print("error.")
            try:
                winsound.PlaySound(currentDir[songNum], winsound.SND_FILENAME)            
            except:
                print("error.")
                print("song number not in list!")
    elif option == "2":
        clear()
        songsExist = False
        currentDir = os.listdir(".")
        print("current songs in the music directory:\n")
        counter = 1
        for musicFile in currentDir:
            print(str(counter) + ". " + musicFile + "\n")
            int(counter)
            counter += 1
            songsExist = True
        if songsExist != True:
            print("There are no songs present in this directory!")
        input("> ")
    elif option == "3":
        clear()
        currentDir = os.listdir(".")
        counter = 1
        for musicFile in currentDir:
            print(str(counter) + ". " + musicFile + "\n")
            int(counter)
            counter += 1
        print("which songs to add to playlist?")
        print("when done type 'MAKE'")
        while True:
            baddSong = input("> ")
            if baddSong == "MAKE":
                print("Choose how to play this Playlist")
                print("1. Play Once")
                print("2. Loop Playlist")
                loopConfirm = input("> ")
                if loopConfirm == "1":
                    print("playing songs...")
                    songCount = 1
                    for currentSong in playlist:
                        try:
                            print("Currently Playing: " + currentDir[currentSong] + " (" + str(songCount) + "/" + str(len(playlist)) + ")")
                            int(songCount)
                            songCount += 1
                            winsound.PlaySound(currentDir[currentSong], winsound.SND_FILENAME)
                        except IndexError:
                            print("Stopped playback due to error.")
                    break
                elif loopConfirm == "2":
                    print("looping songs...")
                    print("(to stop loop exit)")
                    while True:
                        songCount = 1
                        for currentSong in playlist:
                            try:
                                print("Currently Playing: " + currentDir[currentSong] + " (" + str(songCount) + "/" + str(len(playlist)) + ") (LOOPING)")
                                int(songCount)
                                songCount += 1
                                winsound.PlaySound(currentDir[currentSong], winsound.SND_FILENAME)
                            except IndexError:
                                print("Stopped playback due to error.")
            else:
                try:
                    addSong = int(baddSong)
                    addSong = addSong - 1
                    playlist.append(addSong)
                except ValueError:
                    print("error occured.")
                    break
    elif option == "4":
        clear()
        print("type the complete directory name to change the working directory")
        checkDir = os.getcwd()
        print("current directory: " + checkDir)
        print("----------------------------------------------\n")
        currentDir = os.listdir(".")
        for folder in currentDir:
            if "." in folder:
                pass
            else:
                print(folder)
        changeDir = input("> ")
        try:
            os.chdir(changeDir)
        except:
            print("This directory does not exist!")
    elif option == "5":
        clear()
        print("Thank you for using PyPlayer!")
        time.sleep(2)
        quit()
    else:
        clear()
        print("'" + option + "'" + " is not a valid command.")
        input("> ")