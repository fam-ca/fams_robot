#!/usr/bin/env python
# license removed for brevity
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import time

def move_robot1():
    my_pub = rospy.Publisher('joint_states',JointState, queue_size=10)
    rospy.init_node('move_robot', anonymous=True) #add in launch!
    rate_msg = rospy.Rate(15)
    robot_state = JointState()
    robot_state.header = Header()
    robot_state.header.stamp = rospy.Time.now()
    robot_state.header.frame_id = 'stroka' # can comment
    robot_state.name = ['base_to_body', 'body_to_head', 'body_to_arm'] 
    robot_state.velocity = [] # can comment
    robot_state.effort = [] # can comment


    base_to_body = -0.5
    body_to_head = -3.14
    body_to_arm = -3.14
    my_pub.publish(robot_state)
    while not rospy.is_shutdown():	    
        robot_state.header.stamp = rospy.Time.now()
        robot_state.position = [base_to_body, body_to_head, body_to_arm]   #initial position
        if -0.6 <= base_to_body <= 0:
            base_to_body = base_to_body + 0.05
        if -3.14 <= body_to_arm <= 3.14:
            body_to_arm = body_to_arm + 0.1
        if -3.14 <= body_to_head <= 3.14:
            body_to_head = body_to_head + 0.1
        
        my_pub.publish(robot_state)
        rate_msg.sleep()  
        time.sleep(0.1)      
if __name__ == '__main__':
    try:
        move_robot1()
    except rospy.ROSInterruptException:
        pass
