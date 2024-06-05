#!/usr/bin/env python3
import rospy
from obtain_pcd.srv import * #注意是功能包名.srv

from  obtain_pcd_node import obtain_pcd

def handle_obtain_pcd(req):
    is_success = obtain_pcd()
    return ObtainPcdResponse(is_success)

if __name__ == "__main__":
    rospy.init_node('obtain_pcd_server')
    server = rospy.Service('obtain_pcd', ObtainPcd, handle_obtain_pcd)
    rospy.spin()


