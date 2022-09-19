# Lab 2 - Robotica de desarrollo - Intro a ROS

### Daniel Esteban Prieto Jiménez y David Felipe Silva Chacón

## Conexión de ROS con MATLAB:

Como indica la guía, lo primero que se hace para conectar ROS con MATLAB es abrir dos terminales de Linux, en el primero se escribe el comando *roscore* (lo que permite iniciar el modo maestro) y en el segundo *rosrun turtlesim turtlesim_node* para abrir el programa turtlesim, como se ve en la imagen.
![1](/media/SS1.png)
A continuación, se inicia una instancia de MATLAB, en el cual se ha previamente instalado el toolbox de robótica. Se crea un script en el cual se escribe el siguiente código:

```
%%
rosinit; %Conexión con modo maestro
%%
velPub = rospublisher('turtle1/cmd_vel','geometry_msgs/Twist'); %Creación publicador
velMsg = rosmessage(velPub); %Creación de mensaje
%%
velMsg.Linear.X = 1; %Valor del mensaje
send(velPub,velMsg); %Envio
pause(1)
%%
subscribed = rossubscriber("/turtle1/pose", "turtlesim/Pose");
lastMessage = subscribed.LatestMessage;
%%
% Script para enviar todos los valores asociados a la pose:
teleporter = rossvcclient("/turtle1/teleport_absolute");
waitforserver(teleporter);
tpmsg = rosmessage(teleporter);
tpmsg.X = 3;
tpmsg.Y = 3;
tpmsg.Theta = pi/2;
call(teleporter, tpmsg);

%%
rosshutdown;
```

Lo primero que se realiza es la suscripcion al nodo de TurtleSim para poder recibir datos, esto se hace mediante la funcion rossubscriber cuyos argumentos son los datos que se desean recibir, que en este caso son los provenientes de turtle1 acerca de la posicion /turtle1/pose, y el segundo argumento es el tipo de mensaje que se va a recibir, de forma general tendra la estructura de la posicion proveniente de TurtleSim /TurtleSim/pose.  

Después de hacer la conexión con el nodo maestro, se crea una suscripción a partir de la cual se lee la información que ROS entrega respecto a la pose de la tortuga. Estos valores leídos se ven en la imagen.
![1](/media/SS2.png)

Posteriormente, para enviar información se crea un objeto a partir de los servicios de ROS, en específico el de *teleport_absolute*. Se le asignan valores de X, Y y ángulo Theta y se llama el servicio, como se muestra en la imagen.
![1](/media/SS3.png)

Finalmente, se usa el comando *rosshutdown* para finalizar la conexión.


## Uso de ROS con Python:

En el repositorio importado dentro del workspace de Catkin, en la carpeta Scripts, se crea el siguiente código de Python:

```
from pynput import keyboard
import rospy
import roslaunch
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
from numpy import pi

rospy.init_node('velPub', anonymous=True)

def pubVel(speed, angspeed, t):
    velpub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    velmsg = Twist()
    velmsg.linear.x = speed
    velmsg.angular.z = angspeed
    endTime = rospy.Time.now() + rospy.Duration(t)
    while rospy.Time.now() < endTime:
        velpub.publish(velmsg)

def on_press(key):
    return

def on_release(key):
    if key == keyboard.KeyCode.from_char('w'):
        pubVel(1, 0, 1)
    if key == keyboard.KeyCode.from_char('s'):
        pubVel(-1, 0, 1)
    if key == keyboard.KeyCode.from_char('a'):
        pubVel(0, -1, 1)
    if key == keyboard.KeyCode.from_char('d'):
        pubVel(0, 1, 1)
    if key == keyboard.Key.space:
        giro180 = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
        giro180(0, pi)
    if key == keyboard.KeyCode.from_char('r'):
        teleportOrigen = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        teleportOrigen(5.5, 5.5, 0)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```

Este código inicialmente importa las librerías necesarias, tanto las de ROS como aquella que se usará para tomar la entrada del teclado. Posteriormente, se inicializa el nodo de ROS. Se declara una función llamada *pubVel* que nos permitirá publicar a ROS un mensaje que contenga la velocidad lineal y la velocidad angular que deseamos imprimirle a nuestra tortuga. Para esto usamos la función de *Publisher* de *ros* y se le pasa como argumento el tópico *cmd_vel*. Además del publisher, se tiene un mensaje que es al que se le asignan los valores de velocidad que deseamos. Un parámetro adicional de la función permite determinar el tiempo durante el cual se le imprimen estas velocidades a la tortuga.  
Después, se tienen otras dos funciones que permiten la lectura del teclado. Es aquí donde se tienen los condicionales que, según la tecla que se presione entre w, a, s y d, llaman a la función *pubVel* para otorgarle la velocidad a la tortuga. En el caso de las teclas espacio y r, en lugar de publicar un mensaje a otro nodo, se usan los servicios de ROS *TeleportRelative* y *TeleportAbsolute* respectivamente para girar 180° la tortuga y para devolverla a inicio.  
Finalmente, se tiene una línea de código que permite que el programa espere las señales del teclado y reconozca la tecla que se presiona.  

Una vez se tiene el script de Python, se incluye este en el archivo CMakeList.txt y se hace build. Luego, se abren dos terminales con los mismos comandos que se emplearon para la sección en MATLAB. Se abre un tercer terminal en el directorio del workspace de Catkin y se ejecuta desde este el archivo de Python que creamos. En el video se muestra el movimiento de la tortuga con las teclas.

[Video] (https://drive.google.com/file/d/1ro5CO5Uaq6pIIdokvZDYKWO0m5ZmPBdu/view?usp=sharing)