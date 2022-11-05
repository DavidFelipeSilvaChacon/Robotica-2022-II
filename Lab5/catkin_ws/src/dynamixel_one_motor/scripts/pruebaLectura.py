import pandas as pd
import numpy as np
tabla = pd.read_csv("Q_Lineas.txt")
tabla = pd.DataFrame.to_numpy(tabla)
for fila in tabla:
	fila = np.append(fila, [0.0])
	print(fila)