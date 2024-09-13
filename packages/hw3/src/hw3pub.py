#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
import random

def publisher():
    rospy.init_node('hw3_publisher', anonymous=True)
    pub = rospy.Publisher('delta', Float32, queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        value = random.uniform(0, 10)
        rospy.loginfo("publishing delta: %f", value)
        pub.publish(value)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

