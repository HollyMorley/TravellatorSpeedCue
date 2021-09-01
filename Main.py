import movingDots
import Config


class Main(movingDots.MovingDots):
    def __init__(self):
        super().__init__()

    def setup_params(self):
        self.initialise_window()
        self.ruler_setup()
        self.platforms_setup()
        self.moving_belts_setup()

    def set_speed(self):

        speedb2 = float(input("Enter visual cue speed for BELT 1 (m/s):"))
        speedb1 = float(input("Enter visual cue speed for BELT 2 (m/s):"))

        #self.dsBelt1.speed = speedb1*100  #convert chosen speed (m/s) into cm/s and adjust animation speed
        #self.dsBelt2.speed = speedb2*100
        self.dsBelt1.speed = speedb1 * 100 / -57 #* - 0.0155  #convert chosen speed (m/s) into cm/s and adjust animation speed (with scaling for visual purposes)
        self.dsBelt2.speed = speedb2 * 100 / -57 #* - 0.0155


    def run_animation(self):
        self.setup_params()  # initialise psychopy window and belt, platform and ruler parameters
        self.set_speed()  # get required animation speed
        self.draw_stimuli()  # run animation



if __name__ == "__main__":
    m = Main()
    m.run_animation()