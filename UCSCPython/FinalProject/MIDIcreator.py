
from mido import Message, MidiFile, MidiTrack

class makeMidi:


    def __init__(self):
        mid = MidiFile()
        track1 = MidiTrack()
        mid.tracks.append(track1)

    def on_midi(x,y,z): # x = note / y = velocity / z = time
        track1.append(Message('note_on', note=x, velocity=y, time=z))


    def off_midi(x,y,z):
        track1.append(Message('note_off', note=x, velocity=y, time=z))


    def first_key(a_string:str) ->str:
        for elm in a_string:
            if elm == 'A':
                return "A"
            elif elm == 'B':
                return "B"
            elif elm == 'C':
                return "C"
            elif elm == 'D':
                return "D"
            elif elm == 'E':
                return "E"
            elif elm == 'F':
                return "F"
            elif elm == 'G':
                return "G"
            else:
                ''


    def string_conversion(st:str) ->str:        # Rules
        n = 0           # Length of Phrase
        li = list(st)
        start_key =  ""
        start_key = start_key + makeMidi.first_key(st)
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


    def midi_write_from_string(self, s:str,fn:str):      # WRITE A MIDI FILE

        mid = MidiFile()
        track1 = MidiTrack()
        mid.tracks.append(track1)


        ma = makeMidi.string_conversion(s)
        print(ma)
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
                        makeMidi.off_midi(last_note[0],velocity,yyy)
                    zzz = zzz + 100
                else:
                    if symb == '1':
                        if len(last_note) > 0:
                            makeMidi.off_midi(last_note[0],velocity,zzz)
                            del last_note[0]
                            zzz = 100
                        last_note.append((int(symb))+note+key_mod+0)
                        makeMidi.on_midi(last_note[0],velocity,yyy)
                        yyy = 100
                    elif symb == '2':
                        if len(last_note) > 0:
                            makeMidi.off_midi(last_note[0],velocity,zzz)
                            del last_note[0]
                            zzz = 100
                        last_note.append((int(symb))+note+key_mod+1)
                        makeMidi.on_midi(last_note[0],velocity,yyy)
                        yyy = 100
                    elif symb == '3':
                        if len(last_note) > 0:
                            makeMidi.off_midi(last_note[0],velocity,zzz)
                            del last_note[0]
                            zzz = 100
                        last_note.append((int(symb))+note+key_mod+1)
                        makeMidi.on_midi(last_note[0],velocity,yyy)
                        yyy = 100
                    elif symb == '4':
                        if len(last_note) > 0:
                            makeMidi.off_midi(last_note[0],velocity,zzz)
                            del last_note[0]
                            zzz = 100
                        last_note.append((int(symb))+note+key_mod+2)
                        makeMidi.on_midi(last_note[0],velocity,yyy)
                        yyy = 100
                    elif symb == '5':
                        if len(last_note) > 0:
                            makeMidi.off_midi(last_note[0],velocity,zzz)
                            del last_note[0]
                            zzz = 100
                        last_note.append((int(symb))+note+key_mod+3)
                        makeMidi.on_midi(last_note[0],velocity,yyy)
                        yyy = 100
                    elif symb == '6':
                        if len(last_note) > 0:
                            makeMidi.off_midi(last_note[0],velocity,zzz)
                            del last_note[0]
                            zzz = 100
                        last_note.append((int(symb))+note+key_mod+3)
                        makeMidi.on_midi(last_note[0],velocity,yyy)
                        yyy = 100
                    elif symb == '7':
                        if len(last_note) > 0:
                            makeMidi.off_midi(last_note[0],velocity,zzz)
                            del last_note[0]
                            zzz = 100
                        last_note.append((int(symb))+note+key_mod+4)
                        makeMidi.on_midi(last_note[0],velocity,yyy)
                        yyy = 100
        mid.save(fn)

