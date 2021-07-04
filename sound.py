import os
from pygame import mixer

class Sound:
    def __init__(self):
        mixer.music.load(os.path.join("assets", "happynes.wav"))
        self.ball_sound = mixer.Sound(os.path.join("assets", "sound_bouncing.wav"))
        self.point_match_sound = mixer.Sound(os.path.join("assets", "sound_correct.wav"))

    def volume_control(self, value):
        self.point_match_sound.set_volume(value)
        self.ball_sound.set_volume(value)
        mixer.music.set_volume(value)

    def play_background_music(self):
        mixer.music.play(-1)

    def stop_background_music(self):
        mixer.music.stop()

    def play_ball_sound(self):
        self.ball_sound.play()

    def stop_ball_sound(self):
        self.ball_sound.stop()
    
    def play_point_match_sound(self):
        self.point_match_sound.play()

    def stop_point_match_sound(self):
        self.point_match_sound.stop()
