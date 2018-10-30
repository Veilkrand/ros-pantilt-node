from __future__ import print_function
import pantilthat as pt
from numpy import interp

# Move to somewhere:
def clamp(n, smallest, largest):
    if n<smallest: return smallest
    if n>largest: return largest
    return  n

class PantiltWrapper(object):

    def __init__(self, tilt_range=(90,-90), pan_range=(-90,90), tilt_constrains=(-75,65), pan_constrains=(-90,90)):

        self.tilt_range = tilt_range
        self.pan_range = pan_range
        self.tilt_constrains = tilt_constrains
        self.pan_constrains = pan_constrains

        self.pan = 0
        self.tilt = 0

        self.center()

    def center(self):
        self.pantilt_magnitude(0, 0)

    def pan_increase_angle(self, angle):
        a = self.pan
        a += angle
        a = clamp(a, self.pan_constrains[0], self.pan_constrains[1])
        self.pan = a
        pt.pan(int(a))

    def tilt_increase_angle(self, angle):
        a = self.tilt
        a += angle
        a = clamp(a, self.tilt_constrains[0], self.tilt_constrains[1])
        self.tilt = a
        pt.tilt(int(a))

    def pantilt_increase_angle(self, pan, tilt):
        self.pan_increase_angle(pan)
        self.tilt_increase_angle(tilt)

    def pan_magnitude(self, magnitude): # between -1, 1
        deg = interp(magnitude,[-1.0,1.0], [self.pan_range[0],self.pan_range[1]])
        deg = clamp(deg, self.pan_constrains[0], self.pan_constrains[1])
        self.pan = deg
        pt.pan(int(deg))

    def tilt_magnitude(self, magnitude): # between -1, 1
        deg = interp(magnitude,[-1.0,1.0], [self.tilt_range[0],self.tilt_range[1]])
        deg = clamp(deg, self.tilt_constrains[0], self.tilt_constrains[1])
        self.tilt = deg
        pt.tilt(int(deg))

    def pantilt_magnitude(self, pan, tilt):
        #print(pan,tilt)
        self.pan_magnitude(pan)
        self.tilt_magnitude(tilt)
