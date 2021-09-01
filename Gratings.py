import numpy as np

import psychopy.visual
import psychopy.event
import psychopy.core

'''
******** THIS IS NOT BEING USED FOR NOW DUE TO WAGON WHEEL EFFECT ISSUES*********
Script is a standalone. If want to use, should integrate it into Main.py

Psychopy important info:
phase = the relative positioning of the light and dark regions of the grating
spatial frequency = the number of cycles (oscillations) over some unit of distance, e.g. pixels. Ie how many cycles per pixel
getTime() function of psychopy.core.Clock() tells us how many seconds have elapsed since the clock was created.
'''

win = psychopy.visual.Window(
    mon='DellXPS',
    #size=[3840, 2160],
    size=[1536, 864],
    units="pix",
    fullscr=True,
    color=(-1, -1, -1)
)

grating = psychopy.visual.GratingStim(
    win=win,
    size=[1700, 200],
    units="pix",
    #size=[15, 10],
    #units="cm",
    sf=5/5000, #sf=5.0 / 200.0,
    contrast=1
)

clock = psychopy.core.Clock()

keep_going = True

clock.reset()

while keep_going:

    grating.phase = np.mod(clock.getTime() / 0.01, 1)

    grating.draw()

    win.flip()

    keys = psychopy.event.getKeys()

    if len(keys) > 0:
        keep_going = False

win.close()