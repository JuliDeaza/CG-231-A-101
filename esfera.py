import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#################          ESFERA           #####################
#pasar de esféricas a cartesianas
def esf_a_car(r, theta, phi):
    x = r*np.cos(theta)*np.sin(phi)
    y = r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(phi)
    return x,y,z

#definir el rango de los angulos y el radio de la esfera
theta = np.arange(0, 2*np.pi, 0.01)
phi = np.arange(0, np.pi, 0.01)
r=1

theta, phi = np.meshgrid(theta,phi)

#pasando a cartesianas
x,y,z= esf_a_car(r,theta,phi)

#crear la figura
figura = plt.figure()
eje = figura.add_subplot(111, projection='3d')

#dibujar la superficie
eje.plot_surface(x,y,z,color='y')
plt.title("Esfera")


##############           CILINDRO             ################
#pasar de cilíndricas a cartesianas
def cil_a_car(rho,phi,z):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    z=z
    return x,y,z

#definir rango y altura del cilindro
phi = np.arange(0, 2*np.pi, 0.01)
z = np.arange(0,2,0.01)
rho = 1

phi,z = np.meshgrid(phi,z)

#pasar a coordenadar cartesianas
x,y,z = cil_a_car(rho,phi,z)

#crear la figura
figura1 = plt.figure()
eje1 = figura1.add_subplot(111, projection='3d')

#crear superficie
eje1.plot_surface(x,y,z,color ='b')
plt.title("Cilindro")


###############              HÉLICE         ##########
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# rotar al rededor de z en cilíndricas
def rotar_cil(rho,phi,z,angulo):
    phi_p=phi+angulo
    return phi_p

#crear la figura
figura2 = plt.figure()
eje2 = figura2.add_subplot(111, projection='3d')

x=0
z=0
y = 1
phi = 0
rho=1000

while phi <rho:
    #rotar con respecto a z
    phi = rotar_cil(rho, phi, z, 4)
    #pasar a cartesianas
    x=np.sin(np.deg2rad(phi))
    y=np.cos(np.deg2rad(phi))
    #graficar los puntos
    eje2.scatter([x],[y],[z])
    #aumento en z para que vaya hacia arriba
    z=z+2

#titulo de la imagen
plt.title("Hélice")

#mostrar el gráfico
plt.show()

################             INTEGRAL           ##################
from sympy import integrate
from sympy.abc import rho
from sympy.abc import phi
from sympy.abc import theta
from sympy import sin

'''Dado que la esfera se encuentra completamente dentro del cilindro
se puede asumir que el volumen de interseccion entre ambos elementos
es el mismo volumen de la esfera'''
#funcion de volumen de un octavo de la esfera
funcion = (rho**2)*(sin(phi))
#primera integral, con respecto a rho de 0 a 4 que es el radio
integralrho = integrate(funcion,(rho,0,4))
#ssegunda integral, con respecto a theta de 0 a pi medios
integraltheta = integrate(integralrho,(theta,0,np.pi/2))
#tercera integral, con respecto a phi de 0 a pi medios
integralphi = integrate(integraltheta,(phi,0,np.pi/2))
#se multiplica la integral por ocho para hallar el volumen total
volumen = integralphi * 8
print("El volumen de la intersección entre un cilindro de radio 7 y altura 10 y una esfera de radio 4 es: ")
print(volumen)
