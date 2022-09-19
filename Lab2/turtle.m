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