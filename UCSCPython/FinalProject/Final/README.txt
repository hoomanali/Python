#--------------------------------------------------------#
#                  String to Music App                   # 
# CMPS-5P                                                # 
# Fall 2017                                              #
# Final Project                                          #
# Group: Text to Music                                   #
#--------------------------------------------------------#

#--------------------------------------------------------#
# File List:                                             #
# MuStrings.py      -- Main program with MIDI creation   #
# StringToMusic.py  -- String to music conversion        #
# testfile.txt      -- Sample text file to convert       #
# README.txt        -- This file                         #
#--------------------------------------------------------#

#--------------------------------------------------------#
# Instructions:                                          #
#                                                        #
# String to Music uses timidity and pygame for music     #
# playback. Please make sure both are installed for      #
# the play button to work.                               #
#                                                        #
# 1. Run MuString.py:                                    #
#        From command line: python3 MuStrings.py         #
#        Or using IDE                                    #
# 2. Enter text into input box or load a text file       #
# 3. Click convert button                                #
# 4. Text will be converted and midi file created        #
# 5. Use play/stop buttons to playback midi file.        #
#        Midi file is in same directory as program.      #
#--------------------------------------------------------#

#--------------------------------------------------------#
# Modules used:                                          #
#                                                        #
# tkinter       -- GUI development                       #
# pygame        -- Audio playback                        #
# os.path       -- File system operations                #
# mido          -- MIDI message creation                 #
# time          -- Time keeping                          #
# StringToMusic -- User defined algorithm for text       #
#                  to music conversion                   #
#--------------------------------------------------------#
