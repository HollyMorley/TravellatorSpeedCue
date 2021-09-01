import numpy as np
import tkinter as tk
import keyboard

import psychopy.visual
import psychopy.event
import psychopy.core
import psychopy.monitors

import Config

'''
########### Script to generate shapes which move at predetermined speeds (cm/s) along a virtual belt area #############
To do this, need to:
- generate shapes which are evenly but randomly distributed across the field 
- give these shapes a lifetime, ideally that can be adjusted
- rebirth shapes in a new position after their lifetime has expired
- generate the movement (left or right) of these shapes at a specified speed (cm/s)

'''


class MovingShapes(Config.Config):
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
        rulerThickness = 0.5
        self.rulerTop = psychopy.visual.Line(
            win=win,
            units='cm',
            lineWidth=rulerThickness,
            size= self.monitorwidth,
            pos=[0,(self.position + self.beltWidth*0.5)],
            ori=45,
            lineColor=(1,1,1)
        )
        self.rulerBottom = psychopy.visual.Line(
            win=win,
            units='cm',
            lineWidth=rulerThickness,
            size= self.monitorwidth,
            pos=[0,(self.position - self.beltWidth*0.5)],
            ori=45,
            lineColor=(1,1,1)
        )

    def platforms_setup(self):
        self.firstPlat = psychopy.visual.Rect(
            win=win,
            units='cm',
            width=self.platformWidth,
            height=self.platformHeight,
            pos=[(self.monitorStart+self.platformWidth*0.5),self.position],
            fillColor=self.platformColour
        )

        self.middlePlat = psychopy.visual.Rect(
            win=win,
            units='cm',
            width=0.1,
            height=self.platformHeight,
            pos=[0,self.position],
            fillColor=self.platformColour
        )

        self.endPlatform = psychopy.visual.Rect(
            win=win,
            units='cm',
            width=self.platformWidth,
            height=self.platformHeight,
            pos=[(self.monitorEnd - self.platformWidth*0.5),self.position],
            fillColor=self.platformColour
        )

    def new_shapes(self):
        self.initialise_window()
        global win
        nShapes = 30
        dotSize = [1,0.5]

        fieldSize = [self.monitorwidth/2,self.beltWidth]

        # create a numpy vector of random positions within the field
        xys = np.random.random([nShapes, 2])
        xys[:, 0] = xys[:, 0] * fieldSize[0] #- fieldSize[0] / 2.0
        xys[:, 1] = xys[:, 1] * fieldSize[1] #- fieldSize[1] / 2.0

        self.shapes = psychopy.visual.ElementArrayStim(
            win=win,
            nElements=nShapes,
            sizes=dotSize,
            xys=xys,
            fieldSize=[self.monitorwidth/2,self.beltWidth],
            fieldPos=[self.monitorwidth*-0.25, -3],
            fieldShape='square',
            colors=[1, 1, 1],
            sfs=0,
            colorSpace='rgb',
            units='cm',
            elementMask=np.ones([20,20]),
            opacities=1
        )

    def new_dots_xy(self):
        self.new_shapes()

    def draw_stimuli(self):
        self.new_shapes()
        self.ruler_setup()

        while not psychopy.event.getKeys():
            self.shapes.draw()

            if self.rulerON:
                self.rulerTop.draw()
                self.rulerBottom.draw()

            win.flip()

if __name__ == "__main__":
    m = MovingShapes()
    m.draw_stimuli()
