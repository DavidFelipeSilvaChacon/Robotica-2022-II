# Lab 3 - Robotica de desarrollo - Cinemática Directa

### Daniel Esteban Prieto Jiménez y David Felipe Silva Chacón


## Descripción de la solución planteada.

Aquí va la descripción de la solución, incluye los parámetros del robot y sus configuraciones en matlab, la creación del workspace, la configuración del archivo basic.yaml, el uso de arduino para el puerto, el uso de dynamixel para los límites articulares, la lógica del código de python y la ejecución con 3 terminales de linux.


## Código del script utilizado:

```
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    while not rospy.is_shutdown():
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()
        point.positions = [0, 0, 0, 0, 0]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(5)
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()
        point.positions = [-0.34, 0.34, -0.34, 0.34, 0]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(5)
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()
        point.positions = [0.52, -0.52, 0.52, -0.52, 0]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(5)
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()
        point.positions = [-1.57, 0.26, -0.95, 0.29, 0]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(5)
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()
        point.positions = [-1.57, 0.78, -0.95, 0.78, 0.17]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(5)


if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass

```


## Gráfica de la configuración comparándola con la fotografía del brazo en la misma configuración.

Aquí van las gráficas de la configuración en MATLAB y las fotos del brazo en cada configuración.


## Video del brazo alcanzando cada posición solicitada:

[Video] (aquí va el link del video en drive o youtube)
