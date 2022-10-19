from cmath import pi
import rospy
import numpy as np
import math
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = [0,0,0,0,0]
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(5)

    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = [20*pi/180,0,0,0,0]
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(5)

    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = [20*pi/180,20*pi/180,0,0,0]
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(5)

    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = [20*pi/180,20*pi/180,20*pi/180,0,0]
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(5)

    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = [20*pi/180,20*pi/180,20*pi/180,20*pi/180,0]
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(5)

    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = [0,0,0,0,0]
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(5)
    
    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = [-20*pi/180,20*pi/180,-20*pi/180,20*pi/180,0]
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(5)
    
    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = [30*pi/180,-30*pi/180,30*pi/180,-30*pi/180,0]
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(5)

    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = [-90*pi/180,15*pi/180,-55*pi/180,17*pi/180,0]
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(5)

    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = [-90*pi/180,45*pi/180,-55*pi/180,45*pi/180,10*pi/180]
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(5)

    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = [0,-pi/2,pi/2,pi/4,0]
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(5)

    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = [0.25, 0, 0, 0, 1.3]    
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(5)

if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass