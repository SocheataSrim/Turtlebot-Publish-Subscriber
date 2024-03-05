#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node("draw circle")
    rospy.loginfo("IT's started now")

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 2.0
        pub.publish(msg)
        rate.sleep()
