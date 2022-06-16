import numpy as np
import tkinter as tk
import keyboard

import psychopy.visual
import psychopy.event
import psychopy.core
import psychopy.monitors

import Config

class MovingDots(Config.Config):
    win = None

    def __init__(self):
        super().__init__()

    def initialise_window(self):
        # Initialise window
        global win
        win = psychopy.visual.Window(
            monitor=self.mon,
            size=(self.screen_width_px,self.screen_height_px),
            colorSpace='rgb',
            color=(-1,-1,-1),
            units='pix',
            screen=self.scrn,
            allowGUI=False,
            fullscr=True
        )

    def ruler_setup(self):
        # use when checking alignment of set up
        global win
        rulerThickness = 0.2
        self.rulerTop = psychopy.visual.Line(
            win=win,
            units='cm',
            lineWidth=rulerThickness,
            size= self.monitorwidth,
            pos=[(0+self.travellatorCentre),(self.position + self.beltWidth*0.5)],
            ori=45,
            lineColor=(1,1,1)
        )
        self.rulerBottom = psychopy.visual.Line(
            win=win,
            units='cm',
            lineWidth=rulerThickness,
            size= self.monitorwidth,
            pos=[(0+self.travellatorCentre), (self.position - self.beltWidth*0.5)],
            ori=45,
            lineColor=(1,1,1)
        )

    def platforms_setup(self):
        self.firstPlat = psychopy.visual.Rect(
            win=win,
            units='cm',
            width=self.platformWidth,
            height=self.platformHeight,
            pos=[(self.monitorStart + self.platformWidth*0.5 + self.travellatorCentre),self.position],
            fillColor=self.platformColour,
            lineWidth= self.platformLineWidth
        )

        self.middlePlat = psychopy.visual.Rect(
            win=win,
            units='cm',
            width=0.1,
            height=self.platformHeight,
            pos=[(0 + self.travellatorCentre),self.position],
            fillColor=self.platformColour
        )

        self.endPlatform = psychopy.visual.Rect(
            win=win,
            units='cm',
            width=self.platformWidth + 1,
            height=self.platformHeight,
            pos=[(self.monitorEnd - self.platformWidth*0.5 + self.travellatorCentre),self.position],
            fillColor=self.platformColour,
            lineWidth=self.platformLineWidth
        )

    def moving_belts_setup(self):
        global win

        self.dsBelt1 = psychopy.visual.DotStim(
            win=win,
            fieldShape="sqr",
            fieldSize=[self.monitorwidth/2,self.beltWidth],
            fieldPos=[(self.monitorwidth*-0.25 + self.movebeltby + 40 + self.travellatorCentre),self.position],
            units='cm',
            speed=self.belt1Speed,
            dotLife=self.beltDotLife,
            nDots=self.beltnDots,
            coherence=self.beltCoherence,
            dotSize=self.beltDotSize,
            color=self.beltColour,
            colorSpace="rgb"
        )

        self.dsBelt2 = psychopy.visual.DotStim(
            win=win,
            fieldShape="sqr",
            fieldSize=[self.monitorwidth/2,self.beltWidth],
            fieldPos=[(self.monitorwidth*0.25 + self.travellatorCentre),self.position],
            units='cm',
            speed=self.belt2Speed,
            dotLife=self.beltDotLife,
            nDots=self.beltnDots,
            coherence=self.beltCoherence,
            dotSize=self.beltDotSize,
            color=self.beltColour,
            colorSpace="rgb"
        )

        self.dsbelt2background = psychopy.visual.Rect(
            win=win,
            units='cm',
            size=[self.monitorwidth/2,self.beltWidth],
            pos=[(self.monitorwidth*0.25 + self.travellatorCentre),self.position],
            fillColor=(-1,-1,-1),  #self.platformColour
            fillColorSpace="rgb",
            lineColor=(-1,-1,-1)
        )



    def draw_stimuli(self):
        '''self.initialise_window()
        self.ruler_setup()
        self.platforms_setup()
        self.moving_belts_setup()'''

        print("Visual cue starting...")
        print("press SPACE to pause")
        print("Press # to quit")

        clock = psychopy.core.Clock()

        keep_going = True

        clock.reset()

        # upon start up draw a stationary dot array
        self.dsBelt1.draw()
        self.dsbelt2background.draw()
        self.dsBelt2.draw()
        self.firstPlat.draw()
        self.middlePlat.draw()
        self.endPlatform.draw()

        win.flip()

        # only start moving after pressing ENTER
        keys = psychopy.event.getKeys()
        start = input('press P to start')

        if start == 'p':
            while keep_going:

                self.dsBelt1.draw()
                self.dsbelt2background.draw()
                self.dsBelt2.draw()
                self.firstPlat.draw()
                self.middlePlat.draw()
                self.endPlatform.draw()

                if self.rulerON:
                    self.rulerTop.draw()
                    self.rulerBottom.draw()

                win.flip()

                keys = psychopy.event.getKeys()

                if keyboard.is_pressed("#"):
                    keep_going = False
                elif keyboard.is_pressed("Space"):  #for pausing
                    pause = input('Press Enter to resume or S to change speed or 2 to increase speed by 2 cm/s...')
                    if pause == 'Enter':
                        keep_going = True
                    elif pause == 's':
                        self.speedb1 = float(input('Belt 1 speed: '))
                        self.speedb2 = float(input('Belt 2 speed: '))
                        self.dsBelt1.speed = self.speedb1 * 100 / -57  #convert chosen speed (m/s) into cm/s and adjust animation speed (with scaling for visual purposes)
                        self.dsBelt2.speed = self.speedb2 * 100 / -57
                        keep_going = True
                    elif pause == '2':
                        self.speedb1 = self.speedb1 + 0.02
                        self.speedb2 = self.speedb2 + 0.02
                        self.dsBelt1.speed = self.speedb1 * 100 / -57  # convert chosen speed (m/s) into cm/s and adjust animation speed (with scaling for visual purposes)
                        self.dsBelt2.speed = self.speedb2 * 100 / -57
                        print("Belt 1 running at: {:.2f}".format(self.speedb1))
                        print("Belt 2 running at: {:.2f}".format(self.speedb2))
                        keep_going = True

        win.close()
