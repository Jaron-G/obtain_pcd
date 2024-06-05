#!/usr/bin/env python3
import rospy
import rospkg
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import numpy as np
import pcl

def save_as_pcd(points):
    pcl_cloud = pcl.PointCloud()
    pcl_cloud.from_array(points[:,:3].astype(np.float32))
    rospack = rospkg.RosPack()
    package_path = rospack.get_path('grasp_icp')  
    # Replace 'your_package_name' with your actual package name
    pcd_file_path = package_path + "/pcd/scence_gazebo.pcd"   
    # Replace 'your_file_name' with your desired file name
    pcl.save(pcl_cloud, pcd_file_path)
    rospy.loginfo("Point cloud saved as .pcd file: %s", pcd_file_path)

def point_cloud_callback(msg):
    # Convert PointCloud2 message to numpy array
    cloud_data = pc2.read_points(msg, skip_nans=True)
    cloud_points = np.array(list(cloud_data))
    rospy.loginfo(cloud_points.shape)
    # Save the numpy array as .pcd file
    save_as_pcd(cloud_points)

def obtain_pointcloud():
    rospy.init_node('point_cloud_saver', anonymous=True)
    rospy.loginfo("获取点云")
    sub = rospy.Subscriber('/camera/depth/points', PointCloud2, point_cloud_callback,queue_size=1,buff_size=52428800)   
    rospy.sleep(0.5)
    sub.unregister()
    rospy.spin()

if __name__ == '__main__':
    obtain_pointcloud()
