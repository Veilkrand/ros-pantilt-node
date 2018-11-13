#!/usr/bin/env python
from __future__ import print_function

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

from PantiltWrapper import PantiltWrapper

class Subscriber(object):

    def __init__(self, input_topic, rate, controller):

        # Extra params
        self.scale_tilt = rospy.get_param("~scale_tilt", -10)
        self.scale_pan = rospy.get_param("~scale_pan", 10)

        self.controller = controller
        self.rospy_rate = rate
        self.latest_msg = None
        self.new_msg_available = False
        self.subscriber = rospy.Subscriber(input_topic, Twist, self._callback, queue_size=1)

        # Test joy
        #rospy.Subscriber('/joy', Joy, self._callback_joy, queue_size=1)

        self._loop()

    def _callback(self, data):
        self.latest_msg = data
        self.new_msg_available = True

    # Test
    def _callback_joy(self, data):
        # print(data.axes)
        tilt = data.axes[1]
        pan = data.axes[0]
        self.controller.pantilt_increase_angle(pan * self.scale_pan, tilt * self.scale_tilt)
        # self.controller.pantilt_magnitude(pan, tilt)

    def _process_msg(self, data):
        """
        For rqt compatibility we are using `linear.x` and `angular.z` from a Twist message.
        However it should be `angular.x` and `angular.y`
        """

        # print(data)

        tilt = data.linear.x
        pan = data.angular.z

        #self.controller.pantilt_magnitude(pan, tilt)
        self.controller.pantilt_increase_angle(pan * self.scale_pan, tilt * self.scale_tilt)

    def _loop(self):

        print('Ready.')
        r = rospy.Rate(self.rospy_rate)

        while not rospy.is_shutdown():
            if self.new_msg_available:
                self.new_msg_available = False
                self._process_msg(self.latest_msg)
                #rospy.loginfo(self.latest_msg.axes)

                r.sleep()

if __name__ == "__main__":

    _node_name = 'pantilt_node'

    print('* {} starting... '.format(_node_name), end="")

    rospy.init_node(_node_name, anonymous=True)

    # Params
    _input_rotation_topic = rospy.get_param("~input_rotation_topic", '/cmd_pantilt')
    _rate = rospy.get_param("~rate", 90) #60

    controller = PantiltWrapper()
    Subscriber(_input_rotation_topic,_rate, controller)
