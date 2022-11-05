# Lab 5 - Robotica de desarrollo - Cinemática Inversa

### Daniel Esteban Prieto Jiménez y David Felipe Silva Chacón


## Descripción de la solución planteada.

Para la realización de este laboratorio nos basamos en los realizados anteriormente, particularmente en el laboratorio 4, en el cual conectamos el robot a ROS y el computador, desde donde se le enviaban los ángulos de las articulaciones.

En un computador con Ubuntu, tras haber instalado ROS, el toolbox de robótica de Peter Corke, y demás software necesario, se creó un workspace de Catkin en el cuál se clonó el repositorio que permite el movimiento del robot. El archivo *basic.yaml* se editó para agregar las demás articulaciones del robot, ya que inicialmente solo tenía una. Fue en este archivo donde se ajustaron las ID y los valores máximos y mínimos de las articulaciones.

Para la ejecución del código en Python, se usaron tres terminales de Linux: La primera con el comando *roscore* para iniciar el servidor de ROS, la segunda con el comando *roslaunch dynamixel_one_motor one_controller.launch*, y la tercera simplemente para ejecutar el código de Python.

En el anterior laboratorio ya se habían tomado las medidas de las articulaciones y las longitudes de los eslabones para crear nuestro modelo de cinemática directa. A partir de este realizamos un modelo de cinemática inversa utilizando el método geométrico, por ser el de mayor facilidad en este caso. 
Adicionalmente en clase habíamos tratado ejemplos muy similares, lo cual nos facilitó el poder realizar la cinemática inversa por este método. 

Una vez realizada la cinemática inversa procedimos a definir una función de cinemática inversa en nuestro código de Python, el cual tomado como entradas los valores x,y, z y una apertura determinada devolviera los valores de las articulaciones para cada conjunto de valores de entrada. Además en un documento de Autocad dibujamos las trayectorias que se requerían, es decir, los ángulos internos, externos, las figuras y las letras. Para poder así determinar los puntos en x e y qué iban a utilizarse para estos. Teniendo lo anterior se podían pasar a un documento de Excel. Este documento de Excel contenía los puntos necesarios para cada una de las figuras y en cada una de las páginas tenía un vector de puntos diferentes, por ejemplo en una hoja estaban los círculos, en otra las líneas, los arcos etcétera.

Una vez realizado el mapeo de puntos de las figuras se le daba el vector de puntos a la función de cinemática inversa dependiendo del nombre de cada uno de las hojas de cálculo. Así obtenemos los vectores de las posiciones de cada una de las articulaciones para cada una de las figuras y/o letras a trazar. Finalmente se preguntaba por las letras o figura que se quisiera hacer y se procedía realizar el envío de los puntos por medio del comando publish(). A continuación podemos ver los videos de el robot realizando las trayectorias:

## Código del script utilizado:

```
import rospy
import pandas as pd
import math as m
import numpy as np
from pynput import keyboard
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def joint_publisher(tabla):
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    for fila in tabla:
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()
        point.positions = fila 
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1.5)

excelName = 'Puntos_XYZ_DD.xlsx'

if excelName == 'Puntos_XYZ_DD.xlsx':
    name = 'DD'
elif excelName == 'Puntos_XYZ_AJ.xlsx':
    name = 'AJ'
elif excelName == 'Puntos_XYZ_CIJ.xlsx':
    name = 'CIJ'
elif excelName == 'Puntos_XYZ_JO.xlsx':
    name = 'JO'
else:
    print('excelName not found')
    exit()

arriba = 5  # altura herramienta no está escribiendo
abajo = 10.5  # altura herramienta está escribiendo
base = 6  # altura tomar la herramienta de la base
apertura = 0  # valor de articulación 5 abierta
cierre = 1.3  # valor de articulación 5 cerrada


def invKine(y, x, z, o):
    if z > 19.5 and z < 20.5:
        z = arriba
    if z > 3.5 and z < 4.5:
        z = abajo
    if o > 0.9 and o < 1.1:
        th5 = apertura
    else:
        th5 = cierre
    if x == 0:
        x = 0.01
    h = 14
    l1 = 10.6
    l2 = 10.6
    l3 = 11
    R1 = m.sqrt(pow(x, 2) + pow(y, 2))
    th1 = m.atan(y/x)
    zm = z - h
    R2 = R1 - l3
    th3 = m.acos((pow(R2, 2) + pow(zm, 2) - pow(l1, 2) - pow(l2, 2)) / (2*l1*l2))
    th2 = m.atan(R2 / zm)
    th4 = -(m.pi / 2) + abs(th2) + abs(th3)
    #if th2 > 1:
    #   th2 = 0
    return [-th1, th2, -th3, th4, th5]


arcoInt = pd.DataFrame.to_numpy(pd.read_excel(excelName, sheet_name='ArcoInt'))
arcoIntInv = []
for fila in arcoInt:
    fila = np.append(fila, [0])
    arcoIntInv.append(invKine(fila[0], fila[1], fila[2], 0))

arcoExt = pd.DataFrame.to_numpy(pd.read_excel(excelName, sheet_name='ArcoExt'))
arcoExtInv = []
for fila in arcoExt:
    fila = np.append(fila, [0])
    arcoExtInv.append(invKine(fila[0], fila[1], fila[2], 0))

names = pd.DataFrame.to_numpy(pd.read_excel(excelName, sheet_name=name))
namesInv = []
for fila in names:
    fila = np.append(fila, [0])
    namesInv.append(invKine(fila[0], fila[1], fila[2], 0))

triangulo = pd.DataFrame.to_numpy(
    pd.read_excel(excelName, sheet_name='Triangulo'))
trianguloInv = []
for fila in triangulo:
    fila = np.append(fila, [0])
    trianguloInv.append(invKine(fila[0], fila[1], fila[2], 0))

circulo = pd.DataFrame.to_numpy(pd.read_excel(excelName, sheet_name='Circulo'))
circuloInv = []
for fila in circulo:
    fila = np.append(fila, [0])
    circuloInv.append(invKine(fila[0], fila[1], fila[2], 0))

lineas = pd.DataFrame.to_numpy(pd.read_excel(excelName, sheet_name='Lineas'))
lineasInv = []
for fila in lineas:
    fila = np.append(fila, [0])
    lineasInv.append(invKine(fila[0], fila[1], fila[2], 0))

puntos = pd.DataFrame.to_numpy(pd.read_excel(excelName, sheet_name='Puntos'))
puntosInv = []
for fila in puntos:
    fila = np.append(fila, [0])
    puntosInv.append(invKine(fila[0], fila[1], fila[2], 0))

figura = pd.DataFrame.to_numpy(pd.read_excel(excelName, sheet_name='Figura'))
figuraInv = []
for fila in figura:
    fila = np.append(fila, [0])
    figuraInv.append(invKine(fila[0], fila[1], fila[2], 0))

home = [-25, 12, 3, 0]
home = invKine(home[0], home[1], home[2], home[3])

herramienta = [-25, 12]
angHerramienta = m.atan(herramienta[0] / herramienta[1])

tomarHerramientaInv = []
dejarHerramientaInv = []
rangoTotal = 5
for i in range(1, rangoTotal+1):
    if i != rangoTotal:
        tomarHerramientaInv.append(
            invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, base, 1))
    else:
        tomarHerramientaInv.append(
            invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, base, 1))
        tomarHerramientaInv.append(
            invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, base, 0))
        tomarHerramientaInv.append(
            invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, arriba, 0))
        tomarHerramientaInv.append(home)


for i in range(1, rangoTotal+1):
    if i != rangoTotal:
        dejarHerramientaInv.append(
            invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, 4, 0))
    else:
        dejarHerramientaInv.append(
            invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, 4, 0))
        dejarHerramientaInv.append(
            invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, 4, 0))
        dejarHerramientaInv.append(
            invKine(i*herramienta[0]/rangoTotal, i*herramienta[1]/rangoTotal, base, 1))




while not rospy.is_shutdown():
        key=input()

        if key == 'q':
            joint_publisher(arcoIntInv)
            key=' '
        if key == 'a':
            joint_publisher(arcoExtInv)
            key=' '
        elif key == 's':
            joint_publisher(namesInv)
            key=' '
        elif key == 'd':
            joint_publisher(trianguloInv)
            key=' '
        elif key == 'f':
            joint_publisher(circuloInv)
            key=' '
        elif key == 'h':
            joint_publisher(lineasInv)
            key=' '
        elif key == 'g':
            joint_publisher(puntosInv)
            key=' '
        elif key == 'p':
            joint_publisher(figuraInv)
            key=' '
        elif key == 'i':
            joint_publisher(tomarHerramientaInv)
            key=' '
        elif key == 'j':
            joint_publisher(dejarHerramientaInv)
            key=' '
        
        


#joint_publisher([home])
#joint_publisher(tomarHerramientaInv)
#joint_publisher([home])
#joint_publisher(arcoIntInv)
#joint_publisher([home])
#joint_publisher(arcoExtInv)
#joint_publisher([home])
#joint_publisher(namesInv)
#joint_publisher([home])
#joint_publisher(trianguloInv)
#joint_publisher([home])
#joint_publisher(circuloInv)
#joint_publisher([home])
#joint_publisher(lineasInv)
#joint_publisher([home])
#joint_publisher(puntosInv)
#joint_publisher([home])
#joint_publisher(figuraInv)
#joint_publisher([home])
#joint_publisher(dejarHerramientaInv)
#joint_publisher([home])

#with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#    listener.join()

```


## Videos del Brazo realizando cada uno de los movimientos

Tomando el Marcador:

![1](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab5/media/1.PNG)
![2](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab5/media/1. Agarra.mp4)

Trazando el Arco Interno:

![3](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab5/media/2.PNG)
![4](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos2m.png)

Trazando el Arco Externo:

![5](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab5/media/3.PNG)
![6](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos3m.png)

Trazando el Triangulo:

![7](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab5/media/4.PNG)
![8](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos4m.png)

Trazando el "Circulo":

![9](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab5/media/5.PNG)
![10](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos5m.png)

Escribiendo las "Letras (D)":

![9](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab5/media/6.PNG)
![10](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos5m.png)

Trazando otro "Circulo":

![9](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab5/media/7.PNG)
![10](https://github.com/DavidFelipeSilvaChacon/Robotica-2022-II/blob/main/Lab4/media/pos5m.png)
