import numpy as np
import tkinter as tk

import psychopy.visual
import psychopy.event
import psychopy.core
import psychopy.monitors

class Config:
    '''
    ############## Config #################
    '''
    # *****Config settings to choose*****
    # Platform config
    platformWidth = 59#40
    platformHeight = 6
    platformColour = (-1, -1, -1)
    platformLineWidth = 0

    # Belt config
    beltWidth = 5
    beltColour = (1, 1, 1)
    belt1Speed = 0  # this does nothing, just sets speed to 0 during initialisation before user chooses speed
    belt2Speed = 0  # this does nothing, just sets speed to 0 during initialisation before user chooses speed
    beltDotLife = 1000
    beltnDots = 900
    beltCoherence = 1
    beltDotSize = 3
    movebeltby = 15

    position = -0.49  # y position of the entire visual stimuli
    rulerON = False
    #testing = False
    monitor_choice = 'Projector'

    # Monitor settings
    '''root = tk.Tk()
    screen_width_px = root.winfo_screenwidth()
    screen_height_px = root.winfo_screenheight()'''
    if monitor_choice == 'Projector':
        screen_width_px = 1920 # **** HAVE HAD TO SET THESE MANUALLY AS CANT GET EXTERNAL SCREEN INFO WITH THE ABOVE METHOD****
        screen_height_px = 1080
        monitorwidth = 210#143.3  # in cm THIS IS WHERE ****MANUALLY**** ADJUST ACTUAL VISUAL CUE SPEED
        viewdist = 20.  # viewing distance in cm
        monitorname = 'Projector'
        scrn = 1  # 0 to use main screen, 1 to use external screen
        mon = psychopy.monitors.Monitor(monitorname, width=monitorwidth, distance=viewdist)
        mon.setSizePix((screen_width_px, screen_height_px))
        mon.save()
    elif monitor_choice == 'DellMonitor':
        screen_width_px = 1920  # **** HAVE HAD TO SET THESE MANUALLY AS CANT GET EXTERNAL SCREEN INFO WITH THE ABOVE METHOD****
        screen_height_px = 1080
        monitorwidth = 60.22  # in cm
        viewdist = 20.  # viewing distance in cm
        monitorname = 'DellMonitor'
        scrn = 1  # 0 to use main screen, 1 to use external screen
        mon = psychopy.monitors.Monitor(monitorname, width=monitorwidth, distance=viewdist)
        mon.setSizePix((screen_width_px, screen_height_px))
        mon.save()
    elif monitor_choice == 'DellXPS':
        screen_width_px = 1536  # **** HAVE HAD TO SET THESE MANUALLY AS CANT GET EXTERNAL SCREEN INFO WITH THE ABOVE METHOD****
        screen_height_px = 864
        monitorwidth = 34.421  # in cm
        viewdist = 60.  # viewing distance in cm
        monitorname = 'DellXPS'
        scrn = 0  # 0 to use main screen, 1 to use external screen
        mon = psychopy.monitors.Monitor(monitorname, width=monitorwidth, distance=viewdist)
        mon.setSizePix((screen_width_px, screen_height_px))
        mon.save()

    monitorStart = monitorwidth * -0.5
    monitorEnd = monitorwidth * 0.5

    travellatorCentre = -1.3 # offet for centre point of the travellator. The more positive the number the further right the centre moves.
    travellatorCentre = travellatorCentre * -1