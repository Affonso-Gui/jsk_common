#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy

from sensor_msgs.msg import Image

from jsk_topic_tools import DiagnosticTransport


class SimpleImageTransport(DiagnosticTransport):
    def __init__(self):
        super(SimpleImageTransport, self).__init__('simple_image_transport')
        self._pub = self.advertise('~output', Image, queue_size=1)

    def subscribe(self):
        self.sub_img = rospy.Subscriber('~input', Image, self._process)

    def unsubscribe(self):
        self.sub_img.unregister()

    def _process(self, img_msg):
        self.vital_checker.poke()
        self._pub.publish(img_msg)


if __name__ == '__main__':
    rospy.init_node('sample_image_transport')
    img_trans = SimpleImageTransport()
    rospy.spin()
