#-------------------------------------------------------------------------
# CMPS 5P Final Project
# This is the main source file for string to music converter
# This application takes in a string as input then produces
# a midi representation of the string and plays back the music.
#------------------------------------------------------------------------- 


#-------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------

import tkinter      # tkinter library - graphical user interface functions
import tkinter.filedialog # tkinter File dialogue - Select files
import pygame       # pygame library - midi music playback support
import os.path      # File system operations
import StringToMusic as STM # User defined class, converts string to music
from mido import Message, MidiFile, MidiTrack   # MIDI message creation
import time         # Time keeping for audio playback


#-------------------------------------------------------------------------
# Global Variables
#-------------------------------------------------------------------------

#-------For MIDI creator-----------------------------------
mid = MidiFile()                # Initialize MIDI file
track1 = MidiTrack()            # Initialize MIDI track
mid.tracks.append(track1)       # Add track to MIDI file
fn = "TextMusic.mid"            # Filename for MIDI file
#---------------------------------------------------------- 

#-------------------------------------------------------------------------
# openTextFileClick() - Click event for openFile button
#-------------------------------------------------------------------------
def openTextFileClick():
    inputFilePath = tkinter.filedialog.askopenfilename()

    inputFile = open(inputFilePath, 'r')

    stringTextBox.delete("1.0","end")
    for count, line in enumerate(inputFile):
        stringTextBox.insert("end",line)

    inputFile.close()


#-------------------------------------------------------------------------
# MIDI creation functions - on_midi()   Turns note on
#                           off_midi()  Turn note off
#                           first_key() Determines first key of MIDI
#-------------------------------------------------------------------------
def on_midi(x,y,z): # x = note / y = velocity / z = time
    track1.append(Message('note_on', note=x, velocity=y, time=z))


def off_midi(x,y,z):
    track1.append(Message('note_off', note=x, velocity=y, time=z))


def first_key(a_string:str) ->str:
    for elm in a_string:
        if elm == 'A' or elm == 'a':
            return "A"
        elif elm == 'B' or elm == 'b':
            return "B"
        elif elm == 'C' or elm == 'c':
            return "C"
        elif elm == 'D' or elm == 'd':
            return "D"
        elif elm == 'E' or elm == 'e':
            return "E"
        elif elm == 'F' or elm == 'f':
            return "F"
        elif elm == 'G' or elm == 'g':
            return "G"
        else:
            ''


#-------------------------------------------------------------------------
# string_conversion() - Converts text string to musical representation
#                       for MIDI file creation. This is a modified
#                       version of StringToMusic for creating MIDI files.
#-------------------------------------------------------------------------
def string_conversion(st:str) ->str:        # Rules
    n = 0           # Length of Phrase
    li = list(st)
    start_key =  ""  
    start_key = start_key + first_key(st)
    new_st = start_key

    for elm in li: 
                                                # Note
        if elm == 'e' or elm == 'E':            # Most common letters in English
            new_st = new_st + '1' 
        elif elm == 't' or elm == 'T':
            new_st = new_st + '3' 
        elif elm == 'a' or elm == 'A':
            new_st = new_st + '5' 
        elif elm == 'o' or elm == 'O':
            new_st = new_st + '7' 
        elif elm == 'i' or elm == 'I':
            new_st = new_st + '2' 
        elif elm == 'n' or elm == 'N':
            new_st = new_st + '4' 
        elif elm == 's' or elm == 'S':
            new_st = new_st + '6' 
                                            # Rest
        elif elm == ' ':
            new_st = new_st + ' ' 
                                            # Phrase
        elif elm == """ 
""":
            new_st = new_st + "*" 
            if (new_st[len(new_st)-2]) == '*':     # Key from most common note
                c = (new_st.count('1',n))
                d = (new_st.count('2',n))
                e = (new_st.count('3',n))
                f = (new_st.count('4',n))
                g = (new_st.count('5',n))
                a = (new_st.count('6',n))
                b = (new_st.count('7',n))

                if a ==(max(a,b,c,d,e,f,g)):
                    new_st = new_st + ('A')
                elif b ==(max(a,b,c,d,e,f,g)):
                    new_st = new_st + ('B')
                elif c ==(max(a,b,c,d,e,f,g)):
                    new_st = new_st + ('C')
                elif d ==(max(a,b,c,d,e,f,g)):
                    new_st = new_st + ('D')
                elif e ==(max(a,b,c,d,e,f,g)):
                    new_st = new_st + ('E')
                elif f ==(max(a,b,c,d,e,f,g)):
                    new_st = new_st + ('F')
                elif g ==(max(a,b,c,d,e,f,g)):
                    new_st = new_st + ('G')
                n = len(new_st)
                new_st = new_st + ' ' 
        elif elm == '.':
            new_st = new_st + '.' 
        elif elm == '!':
            new_st = new_st + '!' 
        elif elm == '?':
            new_st = new_st + '?' 
        elif elm == ',':
            new_st = new_st + ',' 
                                            # Note Hold
        else:                                       # all other characters
            if (new_st[len(new_st)-1]) == '1':      # checks last element in new_st
                new_st = new_st + '-' 
            if (new_st[len(new_st)-1]) == '2':
                new_st = new_st + '-' 
            if (new_st[len(new_st)-1]) == '3':
                new_st = new_st + '-'
            if (new_st[len(new_st)-1]) == '4':
                new_st = new_st + '-'
            if (new_st[len(new_st)-1]) == '5':
                new_st = new_st + '-'
            if (new_st[len(new_st)-1]) == '6':
                new_st = new_st + '-'
            if (new_st[len(new_st)-1]) == '7':
                new_st = new_st + '-'
            if (new_st[len(new_st)-1]) == '-':
                new_st = new_st + '-'
            else:
                new_st = new_st + ' '
    return new_st


#-------------------------------------------------------------------------
# midi_write_from_string() - Writes MIDI message from string and saves
#                            to MIDI file.
#-------------------------------------------------------------------------
def midi_write_from_string(s:str):            # WRITE A MIDI FILE

    ma = string_conversion(s)
    velocity = 50
    key_mod = 0
    last_note = []
    note = 0
    yyy = 100   # Note On
    zzz = 100   # Note Off

    for symb in ma:
        if symb == 'A':
            key_mod = 56
        elif symb == 'B':
            key_mod = 58
        elif symb == 'C':
            key_mod = 59
        elif symb == 'D':
            key_mod = 61
        elif symb == 'E':
            key_mod = 63
        elif symb == 'F':
            key_mod = 64
        elif symb == 'G':
            key_mod = 66
        else:
            if symb == '-':
                yyy = yyy + 100
            elif symb == ' ':
                if len(last_note) > 0:
                    off_midi(last_note[0],velocity,yyy)
                zzz = zzz + 100
            else:
                if symb == '1':
                    if len(last_note) > 0:
                        off_midi(last_note[0],velocity,zzz)
                        del last_note[0]
                        zzz = 100
                    last_note.append((int(symb))+note+key_mod+0)
                    on_midi(last_note[0],velocity,yyy)
                    yyy = 100
                elif symb == '2':
                    if len(last_note) > 0:
                        off_midi(last_note[0],velocity,zzz)
                        del last_note[0]
                        zzz = 100
                    last_note.append((int(symb))+note+key_mod+1)
                    on_midi(last_note[0],velocity,yyy)
                    yyy = 100
                elif symb == '3':
                    if len(last_note) > 0:
                        off_midi(last_note[0],velocity,zzz)
                        del last_note[0]
                        zzz = 100
                    last_note.append((int(symb))+note+key_mod+1)
                    on_midi(last_note[0],velocity,yyy)
                    yyy = 100
                elif symb == '4':
                    if len(last_note) > 0:
                        off_midi(last_note[0],velocity,zzz)
                        del last_note[0]
                        zzz = 100
                    last_note.append((int(symb))+note+key_mod+2)
                    on_midi(last_note[0],velocity,yyy)
                    yyy = 100
                elif symb == '5':
                    if len(last_note) > 0:
                        off_midi(last_note[0],velocity,zzz)
                        del last_note[0]
                        zzz = 100
                    last_note.append((int(symb))+note+key_mod+3)
                    on_midi(last_note[0],velocity,yyy)
                    yyy = 100
                elif symb == '6':
                    if len(last_note) > 0:
                        off_midi(last_note[0],velocity,zzz)
                        del last_note[0]
                        zzz = 100
                    last_note.append((int(symb))+note+key_mod+3)
                    on_midi(last_note[0],velocity,yyy)
                    yyy = 100
                elif symb == '7':
                    if len(last_note) > 0:
                        off_midi(last_note[0],velocity,zzz)
                        del last_note[0]
                        zzz = 100
                    last_note.append((int(symb))+note+key_mod+4)
                    on_midi(last_note[0],velocity,yyy)
                    yyy = 100

    # Added for filename creation
    filename = filenameTextBox.get("1.0","end")
    filename = filename[:-1]
    filename = filename + ".mid"
    mid.save(filename)      # User defined filename
    mid.save(fn)            # Create "TextMusic.mid" for playback


#-------------------------------------------------------------------------
# musicPlayerInit() - Initialized pygame musice player.
#-------------------------------------------------------------------------
def musicPlayerInit():
    freq = 44100
    size = -16
    chan = 2
    buf = 1024
    pygame.mixer.init(freq,size,chan,buf)
    time.sleep(0.5)
    pygame.mixer.music.load("TextMusic.mid")
    time.sleep(1)
    

#-------------------------------------------------------------------------
# convertButtonClick() - Click event for convert button
#                        Uses StringToMusic module to convert string.
#                        Currently outputs a string representation of
#                        Converted music.
#-------------------------------------------------------------------------
def convertButtonClick():
    inputString = stringTextBox.get("1.0","end")

    # Convert string
    outputString = STM.StringToMusic.string_conversion(inputString)
    
    # Clear text box and insert new string
    musicTextBox.delete("1.0","end")
    musicTextBox.insert("end", outputString)

    # Musical notes
    mi = stringTextBox.get("1.0","end") + ".mid"
    midi_write_from_string(mi)

    musicPlayerInit()

#-------------------------------------------------------------------------
# play() - Click event for play button, calls playMusic function
#               from music player class.
#-------------------------------------------------------------------------
def play():
    pygame.mixer.music.play()
    

#-------------------------------------------------------------------------
# pause() - Click event for pause/unpause button, pauses and unpauses
#           midi music playback using music player class.
#-------------------------------------------------------------------------
def pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    elif not pygame.mixer.music.get_busy():
        pygame.mixer.music.unpause()


#-------------------------------------------------------------------------
# stop() - Click event for stop button, stops music playback.
#-------------------------------------------------------------------------
def stop():
    pygame.mixer.music.stop()


#-------------------------------------------------------------------------
# top - main graphical window for the application
#-------------------------------------------------------------------------
top = tkinter.Tk()
top.geometry("800x500") # dimensions of window, in pixels
top.resizable(0,0)      # prevents user from resizing window
top.configure(background = "black")


#-------------------------------------------------------------------------
# Frames - Used for organizing widgets in GUI
#-------------------------------------------------------------------------
frame01 = tkinter.Frame(top)
frame01.config(width=800, height=200)
frame01.config(bg = "black", bd=1)

frame02 = tkinter.Frame(top)
frame02.config(width=800, height=200)
frame02.config(bg = "black", bd=1)

break01 = tkinter.Frame(top)
break01.config(width=800, height=50)
break01.config(bg = "black")

frame03 = tkinter.Frame(top)
frame03.config(width=800, height=200)
frame03.config(bg = "black", bd=1)

break02 = tkinter.Frame(top)
break02.config(width=800, height=10)
break02.config(bg = "black")

frame04 = tkinter.Frame(top)
frame04.config(width=800, height=200)
frame04.config(bg = "black", bd=1)

frame04Child01 = tkinter.Frame(frame04)
frame04Child01.config(width=600, height=200)
frame04Child01.config(bg = "black", bd=1)

frame04Child01Break01 = tkinter.Frame(frame04)
frame04Child01Break01.config(width=50)
frame04Child01Break01.config(bg = "black")

frame04Child02 = tkinter.Frame(frame04)
frame04Child02.config(width=200, height=200)
frame04Child02.config(bg = "black", bd=1)


#-------------------------------------------------------------------------
# topLabel - text label for main window
#            This label can be replaced with an image using:
#            topLabel.config(image = image.bmp )
#-------------------------------------------------------------------------
topLabel = tkinter.Label(frame01)
topLabel.config(text = "Text to Midi")  # text to be displayed as title
topLabel.config(background = "black", foreground="green")
topLabel.config(font = ("Arial", 35))


#-------------------------------------------------------------------------
# stringTextBox - Text Entry box for string to be converted to music  
#-------------------------------------------------------------------------
stringTextBox = tkinter.Text(frame02) 
stringTextBox.config(bd = 3) 
stringTextBox.config(height = 6)
stringTextBox.config(width = 80)
stringTextBox.config(insertborderwidth = 3)
stringTextBox.config(takefocus = 1)


#-------------------------------------------------------------------------
# filenameTextBox - Text Entry box for string to be converted to music  
#-------------------------------------------------------------------------
filenameTextBox = tkinter.Text(frame02) 
filenameTextBox.config(bd = 3) 
filenameTextBox.config(height = 1)
filenameTextBox.config(width = 20)
filenameTextBox.config(insertborderwidth = 3)
filenameTextBox.delete("1.0","end")
filenameTextBox.insert("end","TextMusic")


#-------------------------------------------------------------------------
# convertButton - Triggers text to midi conversion
#                 Calls convertButtonClick() method
#-------------------------------------------------------------------------
convertButton = tkinter.Button(frame02)
convertButton.config(command = convertButtonClick)
convertButton.config(background = "white")
convertButton.config(text = "Convert to music")
convertButton.config(width=15)


#-------------------------------------------------------------------------
# openFileButton - Starts open file dialogue
#-------------------------------------------------------------------------
openFileButton = tkinter.Button(frame02)
openFileButton.config(command = openTextFileClick)
openFileButton.config(background = "white")
openFileButton.config(text = "Open text file")
openFileButton.config(width=15)


#-------------------------------------------------------------------------
# musicTextBox - Text box for note output (for now)
#                This can later be replaced with some type of music
#                sheet or any way we figure out how to display the music.
#-------------------------------------------------------------------------
musicTextBox = tkinter.Text(frame03) 
#musicTextBox.config(textvariable = textToConvert)
musicTextBox.config(bd = 3) 
musicTextBox.config(height = 10)
musicTextBox.config(width = 100)
musicTextBox.config(insertborderwidth = 3)


#-------------------------------------------------------------------------
# playButton - Plays midi file
#-------------------------------------------------------------------------
playButton = tkinter.Button(frame04Child01)
playButton.config(command = play)
playButton.config(text = "Play")
playButton.config(width=20)


#-------------------------------------------------------------------------
# pauseButton - Pauses and unpauses music playback
#-------------------------------------------------------------------------
pauseButton = tkinter.Button(frame04Child01)
pauseButton.config(command = pause)
pauseButton.config(text = "Pause/UnPause")
pauseButton.config(width=20)


#-------------------------------------------------------------------------
# stopButton - Stops midi file playback
#-------------------------------------------------------------------------
stopButton = tkinter.Button(frame04Child01)
stopButton.config(command = stop)
stopButton.config(text = "stop")
stopButton.config(width=20)


#-------------------------------------------------------------------------
# Grid everything into main window and run application
#-------------------------------------------------------------------------
frame01.grid(row=0, column=0)   # Top label
topLabel.pack(expand=1)

frame02.grid(row=1, column=0)   # Text box and convert button
stringTextBox.pack(side='left', padx=10)
openFileButton.pack()
filenameTextBox.pack(pady=2)
convertButton.pack()
break01.grid(row=2, column=0)

frame03.grid(row=3, column=0)   # Music string output box
musicTextBox.pack(side='left')
break02.grid(row=4, column=0)

frame04.grid(row=5, column=0)   # Play/Stop

frame04Child01.grid(row=0, column=0)
playButton.pack()
stopButton.pack()


#-------------------------------------------------------------------------
# Main loop - Starts program
#-------------------------------------------------------------------------
if __name__ == "__main__":

    top.mainloop()


