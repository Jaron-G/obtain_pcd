#!/usr/bin/env python3
import rospy
from obtain_pcd.srv import * #注意是功能包名.srv
from  obtain_pcd_node import obtain_pointcloud

import argparse  # 导入argparse模块
# 用来装载参数的容器
parser = argparse.ArgumentParser(description='Calculate')
# 给这个解析对象添加命令行参数
parser.add_argument('save_path', type=str, help='the path of point cloud data to be saved')
# 获取排除ros自身启动节点外所有参数：__name:=xxx __log:=/root/.ros/log/xxx.log
args = parser.parse_args(rospy.myargv()[1:])

def handle_obtain_pcd(req):
    is_success = obtain_pointcloud(args.save_path)
    return ObtainPcdResponse(is_success)

if __name__ == "__main__":
    rospy.init_node('obtain_pcd_server')
    server = rospy.Service('obtain_pcd', ObtainPcd, handle_obtain_pcd)
    rospy.spin()


