#!/usr/bin/env python3
import rospy
from obtain_pcd.srv  import * #注意是功能包名.srv

def obtain_pcd_client():
    rospy.wait_for_service('obtain_pcd')
    try:
        obtain_pcd = rospy.ServiceProxy('obtain_pcd', ObtainPcd)
        resp1 = obtain_pcd()
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    rospy.init_node("obtain_pcd_client")
    rospy.loginfo("Start obtain pcd !")
    response = obtain_pcd_client()
    rospy.loginfo("Obtain pcd is OK !")
