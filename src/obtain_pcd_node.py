#!/usr/bin/env python3
import rospy
import rospkg
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import numpy as np
import pcl

#kinect虚拟相机拍摄的点云单位为m，文件类型为.pcd, 配准需要.ply文件且单位为mm，因此需要增加该转换操作
def convert_pcd_to_ply(ply_file, pcd_file):
    # 读取PCD文件,转换单位m to mm
    point_cloud = pcl.load(pcd_file)
    pt_m = point_cloud.to_array()
    pt_mm = pt_m*1000
    point_cloud = pcl.PointCloud(pt_mm)
    # 保存为Ply文件
    #point_cloud.to_file(ply_file)
    pcl.save(point_cloud,ply_file)

def save_as_pcd(points):
    '''
    @points: point cloud data to be saved
    @save_path: save point cloud to a given path
    '''
    pcl_cloud = pcl.PointCloud()
    pcl_cloud.from_array(points[:,:3].astype(np.float32))
    # rospack = rospkg.RosPack()
    # package_path = rospack.get_path('grasp_icp')  
    # Replace 'your_package_name' with your actual package name
    pcd_file_path = pcd_path + "/pcd/scence_gazebo.pcd"   
    # Replace 'your_file_name' with your desired file name
    pcl.save(pcl_cloud, pcd_file_path)
    # convert_pcd_to_ply
    ply_file_path = pcd_path + "/pcd/scence_gazebo.ply"  #填入ply文件的路径
    convert_pcd_to_ply(ply_file_path, pcd_file_path)
    rospy.loginfo("Point cloud saved as .ply file: %s", ply_file_path)

def point_cloud_callback(msg):
    # Convert PointCloud2 message to numpy array
    cloud_data = pc2.read_points(msg, skip_nans=True)
    cloud_points = np.array(list(cloud_data))
    rospy.loginfo(cloud_points.shape)
    # Save the numpy array as .pcd file and convert .pcd to .ply
    save_as_pcd(cloud_points)

def obtain_pointcloud(save_path):
    rospy.loginfo("获取点云")
    global pcd_path 
    pcd_path = save_path
    sub = rospy.Subscriber('/camera/depth/points', PointCloud2, point_cloud_callback,queue_size=1,buff_size=52428800)   
    rospy.sleep(0.5)
    sub.unregister()

if __name__ == '__main__':
    obtain_pointcloud()
