#!/usr/bin/env python3

#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

class Hw3Subscriber:
    def __init__(self):
        self.total = 0
        rospy.Subscriber("delta", Float32, self.callback)
        self.pub = rospy.Publisher("total", Float32, queue_size=10)

    def callback(self, data):
        rospy.loginfo("received delta: %f", data.data)
        self.total += data.data
        rospy.loginfo("updated total: %f", self.total)
        self.pub.publish(self.total)

if __name__ == '__main__':
    rospy.init_node('hw3_subscriber', anonymous=True)
    Hw3Subscriber()
    rospy.spin()

