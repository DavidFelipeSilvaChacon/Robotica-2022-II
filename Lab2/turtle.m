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
posePub = rospublisher("/turtle1/pose", "turtlesim/Pose");
poseMsg = rosmessage(posePub);
poseMsg.X = 5;
poseMsg.Y = 5;
poseMsg.Theta = 0;
poseMsg.LinearVelocity = 1;
poseMsg.AngularVelocity = 1;
send(posePub, poseMsg);
pause(1)