# Lab 3 - Robótica Industrial 2, Entradas y Salidas

### Daniel Esteban Prieto Jiménez y David Felipe Silva Chacón

## Herramienta

Para el desarrollo del laboratorio se empleó la herramienta creada anteriormente. Esta se fabricó empleando anillos de madera obtenidos mediante corte láser, los cuales se sostienen empleando tuercas y tornillos M6 de 90mm. Se usó un resorte que soporta el marcador y le proporciona movilidad. Una vez fabricada la herramienta, se realizó el modelo en CAD de la misma en el software Autodesk Inventor. En este mismo software se creó el tablero que contiene las letras que serán usadas posteriormente para crear las trayectorias.

## Uso de RobotStudio

En el software RobotStudio se creó una estación con el robot IRB140 y el controlador IRC5, y se importaron los modelos de la herramienta y del tablero. Se creó una herramienta a partir del modelo tridimensional, se le asignó un TCP y se conectó al robot. El tablero se usó para crear un Workobject y se estableció un sistema de coordenadas por tres puntos.
Se definió un punto de Home, y se crearon las trayectorias para cada letra, empleando movimientos lineales.

Con las trayectorias definidas, se creó el código de RAPID a partir de la información del controlador, y se modificó la función *MAIN* para que iniciara desde la posición Home. Se emplearon condiciones *if* para que el robot tomara la posición de mantenimiento al presionar el botón 1, y que iniciara la rutina de escritura al presionar el botón 2. También se añadieron, al momento de llamar las rutinas, las indicaciones para encender (o apagar) el indicador correspondiente. Adicionalmente, se añadió un sistema de seguridad al momento de retirar el robot de la posición de mantenimiento: el operario debe presionar dos veces los dos botones simultáneamente para retirarla y volver a la posición de Home, con el fin de evitar accidentes por mover el robot mientras se le está cambiando la herramienta.

Como se puede observar en el video, el resultado es que tanto en la simulación como en la práctica el robot sigue el comportamiento deseado, y el operador lo controla desde el tablero de mando que contiene los pulsadores. Se ve también que se encienden los botones.

[Video] (https://drive.google.com/file/d/1DsU00eRs1pSPnUV2a_-L5mDsIW8nfiMx/view?usp=sharing)

### Código de RAPID:

```
% Código
```