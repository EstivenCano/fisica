from vpython import *
#GlowScript 2.9 VPython
#-------------------------------------------------------------------------------
#    Preparacion  Escena
from visual import *

scene = canvas(background=color.white, align='left')
scene.width = 600
scene.height = 350
scene.background = color.gray(0.9)
scene.ambient = color.gray(0.5)

p1 = sphere(pos=vec(0,0.2,0),radius=1,texture = textures.metal, emissive = False)
p4 = simple_sphere(pos=vec(0,0.2,0),radius=0.08,color=color.red)
ligth1 = local_light(pos=p4.pos, color=p4.color)
w1 = box(pos=vec(-2.5,-1,0),length=0.3, height=2, width=1,  texture = textures.wood)
w2= box(pos=vec(2.5,-1,0),length=0.3, height=2, width=1,  texture = textures.wood)
w3= box(pos=vec(0,-2,0),length=5.3, height=0.1, width=1, texture = textures.wood)
w4= box(pos=vec(0,-1,0),length=0.1, height=2, width=0.25, texture = textures.wood)
p2 = sphere(pos=vec(2.5,0.2,0),radius=0.2,color=color.red)
p3 = sphere(pos=vec(-2.5,0.2,0),radius=0.2,color=color.blue)
l1 = label( pos=vec(2.5,0.2,0), text='+', opacity = 0, box = False, color = color.white, height=20) 
l2 = label( pos=vec(-2.5,0.2,0), text='-', opacity = 0, box = False, color = color.white, height=20) 
a1 = arrow(pos=vec(2,0.2,0.2),axis=vec(-3,0,1), shaftwidth=0.1, color = color.red, length= 1)
a2 = arrow(pos=vec(-1.2,0.2,0.5),axis=vec(-3,0,-1), shaftwidth=0.1, color = color.blue, length= 1)
g1 = graph(width=600,height=300,title='Posición vs Tiempo',align='left',xtitle='<b>Tiempo t(s)<b>', ytitle='<b>Posicion<b>')
fpos = gcurve(color=color.red, width=3, markers=False)
fpos1 = gcurve(color=color.blue, width=3, markers=False)



#--------------------------------------------------------------------------------------------------------
#                  Variables fisicas



#Masa
m = 0.5
#Radio
r = 1
ø = 0
#Tiempo
t = 0
t0 = 0
#Momento de inercia Esfera hueca
I = (2/3)*(m)*(r**2)
#Carga positiva
q1 = 1
#Carga negativa
q2 = -1
#Carga inducida en esfera
q3 = 0.3 
#Distancia entre q1 y q2 a la carga q3
d = 1.3
#Fuerza entre las cargas q1 y q2
f1 = (1/(4*pi*1.00054))* ((q1*q3)/d**2)
#Fuerza entre las cargas q2 y q3
f2 = (1/(4*pi*1.00054))* ((q2*q3)/d**2)
#Torques ejercidos 
tor1 = f1*r
tor2  = -(f2*r)
#Aceleracion angular
a = (tor1 + tor2)/I
le = 0.001

while(True): 
    rate(20)
    le +=0.000835
    #Aceleracion angular
    a = (tor1 + tor2)/I
    ø = (1/2)*(a*(t-t0)**2)
    w = a*t
    #Distancia en x
    disx = r*cos(ø)
    #Distancia en y 
    disy = r*sin(ø)
    ligth1.pos = p4.pos = vec(disx,0.2,disy)    
    p1.rotate(angle=le, origin = vec(0.01,0.01,0), axis = vec(0,-0.001,0))
    
    t = t + 0.1
    if disy < 0: 
        p4.color = color.blue
        ligth1.color = color.blue

    if disy > 0:
        p4.color = color.red
        ligth1.color = color.red

        
    if t < 27.5:
        fpos.plot(t,disx)
        fpos1.plot(t,disy)
        #fpos.plot(t,w)