from mido import Message, MidiFile, MidiTrack

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

fn = (input("MIDI FILE NAME: "))+'.mid'     # User enters MIDI file name
gd = '''Right outside this lazy summer home 
you ain't got time to call your soul a critic no.
Right outside the lazy gate of winter's summer home,
wond'rin' where the nut-thatch winters,
wings a mile long just carried the bird away.

Wake up to find out that you are the eyes of the world,
the heart has its beaches, its homeland and thoughts of its own.
Wake now, discover that you are the song that the mornin' brings,
But the heart has its seasons, its evenin's and songs of its own.

There comes a redeemer, and he slowly too fades away,
And there follows his wagon behind him that's loaded with clay.
And the seeds that were silent all burst into bloom, and decay,
and night comes so quiet, it's close on the heels of the day.

Wake up to find out that you are the eyes of the world,
the heart has its beaches, its homeland and thoughts of its own.
Wake now, discover that you are the song that the mornin' brings,
But the heart has its seasons, its evenin's and songs of its own.

Sometimes we live no particular way but our own,
And sometimes we visit your country and live in your home,
sometimes we ride on your horses, sometimes we walk alone,
sometimes the songs that we hear are just songs of our own.

Wake up to find out that you are the eyes of the world,
the heart has its beaches, its homeland and thoughts of its own.
Wake now, discover that you are the song that the mornin' brings,
But the heart has its seasons, its evenin's and songs of its own. '''
mi = '''You know, young rich niggas
You know so we ain't really never had no old money
We got a whole lotta new money though, hah
(If Young Metro don't trust you I'm gon' shoot ya)
Hey!

Raindrop (drip), drop top (drop top)
Smokin' on cookie in the hotbox (cookie)
Fuckin' on your bitch, she a thot, thot (thot)
Cookin' up dope in the crockpot (pot)
We came from nothin' to somethin', nigga (hey)
I don't trust nobody, grip the trigger (nobody)
Call up the gang and they come and get ya (gang)
Cry me a river, give you a tissue (hey)
My bitch is bad and boujee (bad)
Cookin' up dope with a Uzi (blaow)
My niggas is savage, ruthless (savage)
We got 30's and 100 rounds too (grrah)
My bitch is bad and boujee (bad)
Cookin' up dope with a Uzi (dope)
My niggas is savage, ruthless (hey)
We got 30's and 100 rounds too (glah)

Offset, whoo, whoo, whoo, whoo, whoo!
Rackaids on rackaids, got back-ends on back-ends
I'm ridin' around in a coupe (coupe)
I take your bih right from you (you)
Bitch, I'm a dog, roof (grr)
Beat the ho walls loose (hey)
Hop in the frog, whoo (skrt)
I tell that bih to come comfort me (comfort me)
I swear these niggas is under me (hey)
They hate and the devil keep jumpin' me (jumpin' me)
Bankrolls on me keep me company (cash)
Ayy, we do the most
Yeah, pull up in Ghosts (whoo)
Yeah, my diamonds a choker (glah)
Holdin' the fire with no holster (blaow)
Rick the Ruler, diamonds cooler (cooler)
This a Rollie, not a Muller (hey)
Dabbin' on 'em like the usual (dab)
Magic with the brick, do voodoo (magic)
Courtside with a bad bitch (bitch)
Then I send the bitch through Uber (go)
I'm young and rich and plus I'm bougie (hey)
I'm not stupid so I keep the Uzi (rrah)
Rackaids on rackaids, got back-ends on back-ends
So my money makin' my back ache (aagh)
You niggas got a low Act rate (Act)
We from the Nawf, yeah, dat way (nawf)
Fat Cookie blunt in the ashtray (cookie)
Two bitches, just national smash day (smash)
Hop in the Lamb, have a drag race (skrt)
I let them birds take a bath, bae (brr)

Raindrop (drip), drop top (drop top)
Smokin' on cookie in the hotbox (cookie)
Fuckin' on your bitch, she a thot, thot (thot)
Cookin' up dope in the crockpot (pot)
We came from nothin' to somethin', nigga (hey)
I don't trust nobody, grip the trigger (nobody)
Call up the gang and they come and get ya (gang)
Cry me a river, give you a tissue (hey)
My bitch is bad and boujee (bad)
Cookin' up dope with a Uzi (blaow)
My niggas is savage, ruthless (savage)
We got 30's and 100 rounds too (grrah)
My bitch is bad and boujee (bad)
Cookin' up dope with a Uzi (dope)
My niggas is savage, ruthless (hey)
We got 30's and 100 rounds too (glah)

Pour a four, I'm droppin' muddy
Outer space, Kid Cudi (drank)
Introduce me to your bitch as wifey and we know she sluttin'
Broke a brick down, nutted butted, now that nigga duckin'
Don't move too fast, I might shoot ya (huh?)
Draco bad and boujee (draco)
I'm always hangin' with shooters (brrah)
Might be posted somewhere secluded (private)
Still be playin' with pots and pans, call me Quavo Ratatouille
Run with that sack, call me Boobie (run with it)
When I'm on stage show me boobies (ayy)
Ice on my neck, I'm the coolest (ice)
Hop out the suicide with the Uzi (pew-pew-pew)
I pull up, I pull up, I pull up
I hop out with all of the drugs and the good luck (skrrt)
I'm cookin', I'm cookin', I'm whippin'
I'm whippin' into a rock up, let it lock up (lock up)
I gave her 10 racks
I told her go shoppin' and spend it all at the pop up (ten)
These bitches, they fuck and suck dick
And they bustin' for Instagram, get your Klout up
Uh, yeah, dat way, float on the track like a Segway (go)
Yeah, dat way, I used to trap by the Subway (trappin')
Yeah, dat way, young nigga trap with the AK (rrrah)
Yeah, dat way, big dyke ho, get the door, Macy Gray (hey)

Raindrop (drip), drop top (drop top)
Smokin' on cookie in the hotbox (cookie)
Fuckin' on your bitch, she a thot, thot (thot)
Cookin' up dope in the crockpot (pot)
We came from nothin' to somethin', nigga (hey)
I don't trust nobody, grip the trigger (nobody)
Call up the gang and they come and get ya (gang)
Cry me a river, give you a tissue (hey)
My bitch is bad and boujee (bad)
Cookin' up dope with a Uzi (blaow)
My niggas is savage, ruthless (savage)
We got 30's and 100 rounds too (grrah)
My bitch is bad and boujee (bad)
Cookin' up dope with a Uzi (dope)
My niggas is savage, ruthless (hey)
We got 30's and 100 rounds too (glah)

Yeah, yeah, yeah, yeah, yeah
My bitch, she bad to the bone
Ayy, wait, these niggas watchin'
I swear to God they be my clones
Yeah, hey, huh
Switchin' my hoes like my flows (what?)
Switchin' my flows like my clothes (like what?)
Keep on shootin' that gun, don't reload
Ooh, ooh, now she want fuck with my crew
'Cause the money come all out the roof
Drive the Rari, that bitch got no roof (skrt)
Wait, what kind of Rari? 458 (damn)
All of these niggas, they hate (they hate)
Try to hide, shoot through the gate
Look, go to strip club, make it rain
Yeah, so much money they use rakes
Count a hundred thousand in your face (in your face)
Yeah, then put 300 right in the safe
Met her today, yeah
She talk to me like she knew me, yeah
Go to sleep in a jacuzzi, yeah
Wakin' up right to a two-piece, yeah
Countin' that paper like loose leaf, yeah
Gettin' that chicken with blue cheese, yeah
Boy, you so fake like my collar, you snakin'
I swear to God that be that Gucci (ayy)
And you know we winnin' (winnin')
Yeah, we is not losin'
Try to play your song, it ain't move me (what?)
Saw your girl once, now she choosin', yeah

Raindrop (drip), drop top (drop top)
Smokin' on cookie in the hotbox (cookie)
Fuckin' on your bitch, she a thot, thot (thot)
Cookin' up dope in the crockpot (pot)
We came from nothin' to somethin', nigga (hey)
I don't trust nobody, grip the trigger (nobody)
Call up the gang and they come and get ya (gang)
Cry me a river, give you a tissue (hey)
My bitch is bad and boujee (bad)
Cookin' up dope with a Uzi (blaow)
My niggas is savage, ruthless (savage)
We got 30's and 100 rounds too (grrah)
My bitch is bad and boujee (bad)
Cookin' up dope with a Uzi (dope)
My niggas is savage, ruthless (hey)
We got 30's and 100 rounds too (glah)'''
test = 'eab a.'


def on_midi(x,y,z): # x = note / y = velocity / z = time
    track.append(Message('note_on', note=x, velocity=y, time=z))


def off_midi(x,y,z):
    track.append(Message('note_off', note=x, velocity=y, time=z))


def string_conversion(st:str) ->str:        # Rules
    n = 0           # Length of Phrase
    li = list(st)
    new_st = 'C'

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


def midi_write_from_string(s:str) ->str:
    ma = string_conversion(s)
    velocity = 50
    time = 0
    key_mod = 0
    last_note = []
    note = 0
    print(ma)

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
                time = time + 1
                print(time)
            elif symb == ' ':
                time = time + 1
                print(time)
                if len(last_note) > 0:
                    off_midi(last_note[0],velocity,time)
            else:
                if symb == '1':
                    if len(last_note) > 0:
                        off_midi(last_note[0],velocity,time)
                        del last_note[0]
                    last_note.append((int(symb))+key_mod+0)
                    on_midi(last_note[0],velocity,time)
                    print(last_note)
                    time = time + 1
                elif symb == '2':
                    if len(last_note) > 0:
                        off_midi(last_note[0],velocity,time)
                        del last_note[0]
                    last_note.append((int(symb))+key_mod+1)
                    on_midi(last_note[0],velocity,time)
                    print(last_note)
                    time = time + 1
                elif symb == '3':
                    if len(last_note) > 0:
                        off_midi(last_note[0],velocity,time)
                        del last_note[0]
                    last_note.append((int(symb))+key_mod+1)
                    on_midi(last_note[0],velocity,time)
                    print(last_note)
                    time = time + 1
                elif symb == '4':
                    if len(last_note) > 0:
                        off_midi(last_note[0],velocity,time)
                        del last_note[0]
                    last_note.append((int(symb))+key_mod+2)
                    on_midi(last_note[0],velocity,time)
                    print(last_note)
                    time = time + 1
                elif symb == '5':
                    if len(last_note) > 0:
                        off_midi(last_note[0],velocity,time)
                        del last_note[0]
                    last_note.append((int(symb))+key_mod+3)
                    on_midi(last_note[0],velocity,time)
                    print(last_note)
                    time = time + 1
                elif symb == '6':
                    if len(last_note) > 0:
                        off_midi(last_note[0],velocity,time)
                        del last_note[0]
                    last_note.append((int(symb))+key_mod+3)
                    on_midi(last_note[0],velocity,time)
                    print(last_note)
                    time = time + 1
                elif symb == '7':
                    if len(last_note) > 0:
                        off_midi(last_note[0],velocity,time)
                        del last_note[0]
                    last_note.append((int(symb))+key_mod+4)
                    on_midi(last_note[0],velocity,time)
                    print(last_note)
                    time = time + 1
    mid.save(fn)
    return str("File saved as "+fn)


print(midi_write_from_string(gd))



