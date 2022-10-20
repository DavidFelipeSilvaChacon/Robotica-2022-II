# Lab 3 - Robotica de desarrollo - Cinemática Directa

### Daniel Esteban Prieto Jiménez y David Felipe Silva Chacón


## Descripción de la solución planteada.

Para el desarrolo del laboratorio, se inició programando el robot en MATLAB con los parámetros Denavit Hartenberg, para lo cuál se empleó el código presente en el archivo *Lab4.m* del repositorio. Este archivo se utilizó para graficar el robot en diversas configuraciones verificando que todas fueran alcanzables sin dañar el robot.

En un computador con Ubuntu, tras haber instalado ROS, el toolbox de robótica de Peter Corke, y demás software necesario, se creó un workspace de Catkin en el cuál se clonó el repositorio que permite el movimiento del robot. El archivo *basic.yaml* se editó para agregar las demás articulaciones del robot, ya que inicialmente solo tenía una. Fue en este archivo donde se ajustaron las ID y los valores máximos y mínimos de las articulaciones.

Todos estos valores fueron tomados usando el programa Dynamixel Wizard y moviendo el robot manualmente. Para que el computador reconociera el puerto, fue necesario usar el programa Arduino para identificar el puerto serial correspondiente.

Para el código de Python, se tomó como base el archivo incluído en el repositorio clonado, que permitía mover una articulación. Se amplió este código para soportar todas las articulaciones, se ajustaron los valores con los ángulos propuestos en la guía (en radianes), se ajustó el tiempo que le toma al robot lcambiar de configuración, y se usó el comando *sleep* para que se mantuviera un tiempo determinado en cada posición tras publicar el objeto de tipo *rosPublisher* al nodo. Con un ciclo, se garantizó que el robot se mantuviera iterando entre las cinco configuraciones indefinidamente.

Para la ejecución del código en Python, se usaron tres terminales de Linux: La primera con el comando *roscore* para iniciar el servidor de ROS, la segunda con el comando *roslaunch dynamixel_one_motor one_controller.launch*, y la tercera simplemente para ejecutar el código de Python.

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

Para la configuración 1:
![1](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos1.png)
![2](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos1m.png)

Para la configuración 2:
![3](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos2.png)
![4](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos2m.png)

Para la configuración 3:
![5](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos3.png)
![6](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos3m.png)

Para la configuración 4:
![7](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos4.png)
![8](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos4m.png)

Para la configuración 5:
![9](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos5.png)
![10](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos5m.png)


## Video del brazo alcanzando cada posición solicitada:

[Video] (https://drive.google.com/file/d/1MT1YTQTRgrJEi1LYMcrHDFR1yPw66OQJ/view?usp=sharing)
