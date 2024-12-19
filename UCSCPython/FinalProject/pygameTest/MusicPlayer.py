#-------------------------------------------------------------------------
# CMPS 5P Final Project - MusicPlayer.py
# MusicPlayer class - This class takes a midi file as input and plays
#                     back the file audio using the pygame library.
#-------------------------------------------------------------------------
class PlayMusic:

    import pygame


#-------------------------------------------------------------------------
# playMusic() - Accepts a midi file as a parameter, inits music player
#                 from pygame library and plays back midi music.
#-------------------------------------------------------------------------
    def playMusic( midiFile ):
        freq = 44100    # Playback frequency
        size = -16      # Unsigned 16 bit
        chan = 2        # Channel
        buf = 1024      # Buffer size
        pygame.mixer.init( freq, size, chan, buf )  // initialize mixer

        ticker = pygame.time.Clock()
        pygame.mixer.music.load( midiFile )
        pygame.mixer.music.play( loops = 0, start = 0.0 )
        
        while pygame.mixer.music.get_busy():
            ticker.tick(30)


#-------------------------------------------------------------------------
# setVol() - Set playback volume from 0.0 to 1.0. 
#-------------------------------------------------------------------------
    def setVol( volume ):
        pygame.mixer.music.set_volume(1.0)


#-------------------------------------------------------------------------
# stopMusic() - Stops music playback
#-------------------------------------------------------------------------
    def stopMusic():
        pygame.mixer.music.stop()


#-------------------------------------------------------------------------
# pauseMusic() - Pauses and unpauses music playback
#-------------------------------------------------------------------------
    def pauseMusic():
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        elif not pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()


