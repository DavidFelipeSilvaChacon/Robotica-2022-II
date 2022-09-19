from pynput import keyboard
import rospy
import roslaunch
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
from numpy import pi

rospy.init_node('velPub', anonymous=True)

def pubVel(speed, angspeed, t):
    velpub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    velmsg = Twist()
    velmsg.linear.x = speed
    velmsg.angular.z = angspeed
    endTime = rospy.Time.now() + rospy.Duration(t)
    while rospy.Time.now() < endTime:
        velpub.publish(velmsg)

def on_press(key):
    return

def on_release(key):
    if key == keyboard.KeyCode.from_char('w'):
        pubVel(1, 0, 1)
    if key == keyboard.KeyCode.from_char('s'):
        pubVel(-1, 0, 1)
    if key == keyboard.KeyCode.from_char('a'):
        pubVel(0, -1, 1)
    if key == keyboard.KeyCode.from_char('d'):
        pubVel(0, 1, 1)
    if key == keyboard.Key.space:
        giro180 = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
        giro180(0, pi)
    if key == keyboard.KeyCode.from_char('r'):
        teleportOrigen = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        teleportOrigen(5.5, 5.5, 0)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()