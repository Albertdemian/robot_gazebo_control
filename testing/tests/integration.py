#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from control_msgs.msg import JointControllerState
from sensor_msgs.msg import JointState



state = 0
command = 0

def callback_msg(data):
    state = data.position[0]
    print(data.position[0], type(data.position[0]))

def callback_real(data):
    command = data
    print(data)

def listener():


    rospy.init_node('joint_state_sub', anonymous=True)

    rospy.Subscriber("/rrbot/joint_states", JointState, callback_msg)
    rospy.Subscriber('/rrbot/joint1_position_controller/command',Float64, callback_real)
    
    while not rospy.is_shutdown():
        print(state, command,state == command)
        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

if __name__ == '__main__':
    listener()