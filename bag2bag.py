from dataclasses import dataclass
from genericpath import isdir
from time import sleep
import rosbag
import os
from std_msgs.msg import Header
from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2, PointField
import math
import numpy as np

def rote_Y(x):
    return np.array([math.cos(x), 0, math.sin(x), 0, 0, 1, 0, 0, -math.sin(x), 0, math.cos(x), 0, 0, 0, 0, 1]).reshape(4,4)
    
def rote_Z(x):
    return np.array([math.cos(x), math.sin(x), 0, 0, -math.sin(x), math.cos(x), 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]).reshape(4,4)

def bag2bag(bag_file, result_file):
    bag = rosbag.Bag(result_file, 'w')
    bag_data = rosbag.Bag(bag_file, "r")
    info = bag_data.get_type_and_topic_info()
    count = 1
    perception_data = bag_data.read_messages('/iv_points')
    for topic, msg, t in perception_data:
        gen = point_cloud2.read_points(msg, field_names=("x", "y", "z", "intensity"), skip_nans=True)
        points = []
        for p in gen:
            x, y, z, i = p
            # pt = [x, y, z, float(i)]
            pt = [z, -y, x, float(i)]
            points.append(pt)
        # points = np.dot(points, rote_Z((-60/180*math.pi))) #负数向左，正数向右
        points = np.dot(points, rote_Y((-5/180*math.pi))) # 负数抬高，正数降低
        points2 = [list(t) for t in set(tuple(_) for _ in points)]
        print(count)
        count += 1
        fields = [PointField('x', 0, PointField.FLOAT32, 1),
                    PointField('y', 4, PointField.FLOAT32, 1),
                    PointField('z', 8, PointField.FLOAT32, 1),
                    PointField('intensity', 12, PointField.FLOAT32, 1),]
        header = Header()
        header.frame_id = "innovusion"
        header.stamp = t
        pc2 = point_cloud2.create_cloud(header, fields, points2)
        bag.write('/iv_points', pc2)
    bag.close()
    sleep(2)
    os.system("rosbag reindex " + result_file)
    os.remove(result_file[:-4] + ".orig.bag")

if __name__ == "__main__":
    FileName = "/home/tusimple/Downloads/Falcon/"
    bag_file_list = os.listdir(FileName)
    for i in range(len(bag_file_list)):
        if not os.path.exists(FileName+"convert/"):
            os.mkdir(FileName+"convert/")
        if (".bag" in bag_file_list[i]):
            print(bag_file_list[i])
            bag2bag(FileName + bag_file_list[i], FileName+"convert/" + bag_file_list[i])





