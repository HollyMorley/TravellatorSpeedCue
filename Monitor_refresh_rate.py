import psychopy.visual

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

win.recordFrameIntervals = True

for frame in range(100):
    win.flip()

average = sum(win.frameIntervals) / len(win.frameIntervals)
refresh_rate = 1/average
print("refresh rate is {} Hz".format(refresh_rate))
