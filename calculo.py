import numpy as np

x = [1,1,1]  # Coordenada inicial
#Ciclo iterativo para el calculo
for i in range (1,10):
    #Definición de funciones a considerar
    F = lambda x1,x2,x3:[
    (((x1-48.85)**2)+((x2-100.15)**2)+((x3-0)**2)-(179.04)**2),
    (((x1+44.30)**2)+((x2-98.45)**2)+((x3-0)**2)-(178.44)**2),
    (((x1-50.30)**2)+((x2-57.66)**2)+((x3-0)**2)-(160.83)**2)
    ]   
    #Definicion de la matriz jacobiana
    Matriz_jaconbiana = lambda x1,x2,x3: [
        [2*(x1-48.48),2*(x2-100.15),2*(x3)],
        [2*(x1+44.30),2*(x2-98.45),2*(x3)],
        [2*(x1-50.30),2*(x2-57.66),2*(x3)]
    ]
    dx = -np.linalg.solve(Matriz_jaconbiana(*x),F(*x)) # resolución del sistema lineal
    x = x + dx # renovacion para el valor de la solución
    if np.linalg.norm(F) < 1e-15:
        break
print("Valores obtenidos con respecto a la ubicación y altura de la montaña")
print(x)
print("Valores redondeados para mayor precición ")
print(round(x[0]),",",round(x[1]),",",round(x[2]))