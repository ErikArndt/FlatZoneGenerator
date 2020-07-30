import random
import time
from os import getcwd
import simpleaudio as sa

# relative paths weren't working for me, so I'm detecting the current directory
FILEPATH = getcwd().replace('\\', '/') + '/'

def play(filename, play_fast=False):
    full_filename = FILEPATH + filename + '.wav'
    wave_obj = sa.WaveObject.from_wave_file(full_filename)
    wave_obj.play()
    if 'bar1' in filename:
        time.sleep(2.9 if play_fast else 2.98)
    else:
        time.sleep(1.45 if play_fast else 1.48)

def first_two_bars():
    '''Randomly chooses a sound file for bars 1 and 2, and plays it.
    '''
    rand_var = random.random()
    if rand_var < 0.2:
        play('bar1_empty')
    elif rand_var < 0.4:
        play('bar1_empty_bass')
    elif rand_var < 0.6:
        play('bar1_melody')
    elif rand_var < 0.8:
        play('bar1_synth')
    else:
        play('bar1_melody_synth')

def third_bar():
    '''Randomly chooses a sound file for bar 3, plays it, and returns its name.
    '''
    rand_var = random.random()
    filename = ''
    if rand_var < 0.25:
        filename = 'bar3_empty'
    elif rand_var < 0.5:
        filename = 'bar3_empty_bass'
    elif rand_var < 0.75:
        filename = 'bar3_melody'
    else:
        filename = 'bar3_melody_bass'
    play(filename)
    return filename

def fourth_bar(played_bar3):
    '''Chooses a sound file to play for bar 4 based on what
    was played in the previous bar.
    '''
    rand_var = random.random()
    if rand_var < 0.05:
        play('intro_fourbeeps')
    elif played_bar3 == 'bar3_empty':
        play('bar4_empty')
    elif played_bar3 == 'bar3_empty_bass':
        if rand_var < 0.6:
            play('bar4_empty_bass')
        elif rand_var < 0.8:
            play('bar4_empty_bass_stac')
        else:
            play('bar4_empty_bass_bstac')
    elif played_bar3 == 'bar3_melody':
        if rand_var < 0.6:
            play('bar4_melody')
        elif rand_var < 0.8:
            play('bar4_melody_stac')
        else:
            play('bar4_melody_bstac')
    elif played_bar3 == 'bar3_melody_bass':
        if rand_var < 0.6:
            play('bar4_melody_bass')
        elif rand_var < 0.7:
            play('bar4_melody_bass_stac')
        elif rand_var < 0.8:
            play('bar4_melody_bass_bstac')
        elif rand_var < 0.9:
            play('bar4_hihat_stac')
        else:
            play('bar4_hihat_bstac')

# These first two sounds seem to take longer to load
play('intro_highnotes', True)
play('intro_fourbeeps', True)
while True:
    first_two_bars()
    bar3 = third_bar()
    fourth_bar(bar3)
