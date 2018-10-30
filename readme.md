# PanTilt Node

Receive Twist messages to control a pan-tilt camera setup using constrains.
For rqt compatibility we are using `linear.x` and `angular.z` from a Twist message. However it should be `angular.x` and `angular.y`

## Topic to Subscribe
`/cmd_pantilt`

## Launch

`roslaunch pantilt_node default.launch`


## (Move to another Teleop node) PS4 support with ds4drv

PS4 controller needs to emulate xbox controller. Use ros joy node.

Install:
`sudo pip install ds4drv`

(???)Permissions: https://github.com/chrippa/ds4drv#permissions

Start emulator of already connected controller:
`sudo ds4drv --hidraw`
