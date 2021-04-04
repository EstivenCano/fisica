from vpython import *
#GlowScript 2.9 VPython
#-------------------------------------------------------------------------------
#    Preparación  Escena
from visual import *

scene = canvas(background=color.white, align='left')
scene.width = 600
scene.height = 400
scene.background = color.black
scene.ambient = color.gray(0.5)

p1 = sphere(pos=vec(-6,0,0),radius=1.5,texture = textures.earth, emissive = False)
p2 = sphere(pos=vec(6,0,0),radius=1.5,texture = textures.earth, emissive = False)
p3 = sphere(pos=vec(-14,6.8,-9),radius=1,texture = textures.metal, emissive = False)
p4 = sphere(pos=vec(14,6.8,-9),radius=1,texture = textures.metal, emissive = False)
ligth1 = local_light(pos=p3.pos, color= color.red)
ligth2 = local_light(pos=p4.pos, color= color.blue)
w1 = box(pos=vec(-15,-1,0),length=0.5, height=18, width=20,  texture = textures.wood)
w2 = box(pos=vec(15,-1,0),length=0.5, height=18, width=20,  texture = textures.wood)
w3 = box(pos=vec(0,-10,0),length=30.5, height=0.3, width=20,  texture = textures.wood)
w4 = box(pos=vec(0,8,0),length=30.5, height=0.3, width=20,  texture = textures.wood)
spring1 = helix(pos=vector(-15,0,0), axis=vector(9,0,0), radius=1 , color = color.white)
spring2 = helix(pos=vector(-5.5,0,0), axis=vector(11,0,0), radius=1 , color = color.white)
spring3 = helix(pos=vector(15,0,0), axis=vector(-9,0,0), radius=1 , color = color.white)
g1 = graph(width=400,height=200,title='Posición  vs  Tiempo',align='left',xtitle='<b>Tiempo(s)<b>', ytitle='<b>Posición(m)<b>')
fp1 = gcurve(color=color.red, width=4, markers=False, marker_color=color.orange)
fp2 = gcurve(color=color.blue, width=4, markers=False, marker_color=color.orange)


#-----------------------------------------------------------------------------------
# Variables Físicas 

#Masa de las esferas
m = 1
#Constante de resortes laterales
k = 20 
#Constante de resorte central
kc = 30
#Posición inicial de esfera a
x0a = -6
#Posición inicial de esfera b
x0b = 6
#Posicion en tiempo t 1
x1 = 0
#Posicion en tiempo t 2
x2 = 0
#Velocidad esfera 1 
v1 = 0
#Velocidad esfera 2 
v2 = 0
#Energia esfera 1 
e1 = 0
#Energia esfera 2 
e2 = 0
# Tiempo inicial
t = 0
# Incremento de tiempo
dt = 0.01
 
#----------------------------------------------------------
# Variables de control

#Variable para iniciar o detener la simulación
running= True
#Variable para reiniciar la simulación
reset = False
#Movimiento horizontal o vertical
hor = True
#Gráfica a mostrar
grafic = True


#----------------------------------------------------------
#Controles 

def setbRun(b):
    global running    
    running = not running
    if running:
        bRun.text="Pausar"
    else:
        bRun.text="Iniciar"
        
bRun=button( bind=setbRun, text="Pausar" )

def setbHor():
    global hor
    #Movimiento horizontal
    #Función para cambiar la posicion de la esfera 1
    p1.pos = vec(x0a + x1,0,0)
    #Función para cambiar la posición de la esfera 2
    p2.pos = vec(x0b + x2,0,0)
    #Eje de resorte 1
    spring1.axis = vec(9+ x1,0,0)
    #Eje de resorte 3
    spring3.axis = vec(-9 + x2,0,0)
    #Posición de resorte central
    spring2.pos = vec(-5.5 + x1,0,0)
    #Eje resorte central
    spring2.axis = vec(11 + (x2 - x1) ,0,0)
    hor = True

    
bHor=button( bind=setbHor , text="Horizontal" )

def setbVer():
    global hor
    #Movimiento vertical
    p1.pos = vec(-6,x1,0)
    p2.pos = vec(6,x2,0)
    spring1.axis = vec(9,x1,0)
    spring3.axis = vec(-9,x2,0)
    spring2.pos = vec(-5.5,x1,0)
    spring2.axis = vec(11,(x2 - x1) ,0)
    hor = False
        
bVer=button( bind= setbVer, text="Vertical" )

def setMass():
  global m,reset
  m = massSlider.value
  reset=True

scene.append_to_caption('\nMasa de las esferas\n')
massSlider = slider(min=0.1, max=2.0, value=1, bind=setMass)

def setElasticConstantK():
  global k,reset
  k = stiffSlider.value
  reset=True

scene.append_to_caption('\n\nConstante elástica laterales\n')    
stiffSlider = slider(min=5, max=100, value=20, bind=setElasticConstantK)

def setElasticConstantKc():
  global kc,reset
  kc = stiffSlider.value
  reset=True

scene.append_to_caption('\n\nConstante elástica central\n')    
stiffSlider = slider(min=5, max=100, value=30, bind=setElasticConstantKc)

def setbGraf():
    global grafic,reset
    if grafic:
        grafic = False
        bGraf.text = "Posición vs Tiempo"
        g1.title = "Energía vs Tiempo"
        g1.ytitle= "<b>Energía(J)<b>"
    else: 
        grafic = True
        bGraf.text = "Energía vs Tiempo"
        g1.title = "Posición vs Tiempo"
        g1.ytitle= "<b>Posición(m)<b>"
    reset = True
    fp1.delete()
    fp2.delete()

scene.append_to_caption('\n')
bGraf=button( bind= setbGraf, text="Energia vs Tiempo" )

while(True):
  rate(60)
  if running:
      if not reset :
          #Frecuencia esfera 1
          wa = sqrt(k/m)
          #Frecuencia esfera 2
          wb = sqrt((2*kc+k)/m)
          #Posición de esfera 1 en tiempo t 
          xa = x0a * cos(wa * t)
          #Posición de esfera 2 en tiempo t
          xb = x0b * cos(wb * t)
          #Velocidad esfera 1
          v1 = (1/2)*(-(x0a*wa) * sin(wa * t) + (x0b*wb) * sin(wb * t))
          #Velocidad esfera 2 
          v2 = (1/2)*(-(x0a*wa) * sin(wa * t) - (x0b*wb) * sin(wb * t))        
          #Posición de esfera 1
          x1 = (xa + xb)/2
          #Posición de esfera 2
          x2 = (xa - xb)/2 
          #Energia esfera 1 
          e1 = (1/2)*m*(v1**2)+(1/2)k*(x1**2)
          #Energia esfera 2 
          e2 = (1/2)*m*(v2**2)+(1/2)k*(x2**2)
          #Eje de movimiento 
          if hor:
            setbHor()
          else:
            setbVer()
          #Gráficas       
          if grafic:
              if t<5:
                fp1.plot(t,x1)
                fp2.plot(t,x2)
          else:
              if t<5:
                fp1.plot(t,e1)
                fp2.plot(t,e2)
          
          #Aumento de tiempo en intervalos de 0.01
          t += dt
      else:
          #Restablece valores iniciales
          t=0
          fp1.delete()
          fp2.delete()
          reset=False