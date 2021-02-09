from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

#cpara calcular color (Numero del colorRGB)/255*1
#Grados a radiales 1° × π/180
#---------------------------CASA--------------------------
def dibujarNube3():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360): 
        angulo = x * 3.14159 / 180.0
        #mismo numero salen igual, diferente, diferente proporcion
        #Agregar resta (Angulo/coseno) hace que la figura baje
        #Agregar suma (Angulo/coseno) hace que la figura suba
        glVertex3f(cos(angulo) * 0.15 + 0.5 , sin(angulo) * 0.05 + 0.8, 0.0)
    glEnd()

def dibujarNube2():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360): 
        angulo = x * 3.14159 / 180.0
        #mismo numero salen igual, diferente, diferente proporcion
        #Agregar resta (Angulo/coseno) hace que la figura baje
        #Agregar suma (Angulo/coseno) hace que la figura suba
        glVertex3f(cos(angulo) * 0.15 - 0.3 , sin(angulo) * 0.05 + 0.8, 0.0)
    glEnd()

def dibujarNube1():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360): 
        angulo = x * 3.14159 / 180.0
        #mismo numero salen igual, diferente, diferente proporcion
        #Agregar resta (Angulo/coseno) hace que la figura baje
        #Agregar suma (Angulo/coseno) hace que la figura suba
        glVertex3f(cos(angulo) * 0.15 + 0.125 , sin(angulo) * 0.05 + 0.7, 0.0)
    glEnd()

def dibujarHojasdeArbol5():
    glColor3f(0.133,0.741,0.223)
    glBegin(GL_POLYGON)
    for x in range(360): 
        angulo = x * 3.14159 / 180.0
        #mismo numero salen igual, diferente, diferente proporcion
        #Agregar resta (Angulo/coseno) hace que la figura baje
        #Agregar suma (Angulo/coseno) hace que la figura suba
        glVertex3f(cos(angulo) * 0.2 + 0.9, sin(angulo) * 0.2 - 0.1, 0.0)
    glEnd()

def dibujarHojasdeArbol4():
    glColor3f(0.133,0.741,0.223)
    glBegin(GL_POLYGON)
    for x in range(360): 
        angulo = x * 3.14159 / 180.0
        #mismo numero salen igual, diferente, diferente proporcion
        #Agregar resta (Angulo/coseno) hace que la figura baje
        #Agregar suma (Angulo/coseno) hace que la figura suba
        glVertex3f(cos(angulo) * 0.2 + 0.85, sin(angulo) * 0.2 + 0.2, 0.0)
    glEnd()

def dibujarHojasdeArbol3():
    glColor3f(0.133,0.741,0.223)
    glBegin(GL_POLYGON)
    for x in range(360): 
        angulo = x * 3.14159 / 180.0
        #mismo numero salen igual, diferente, diferente proporcion
        #Agregar resta (Angulo/coseno) hace que la figura baje
        #Agregar suma (Angulo/coseno) hace que la figura suba
        glVertex3f(cos(angulo) * 0.2 + 0.75, sin(angulo) * 0.2 + 0.25, 0.0)
    glEnd()

def dibujarHojasdeArbol2():
    glColor3f(0.133,0.741,0.223)
    glBegin(GL_POLYGON)
    for x in range(360): 
        angulo = x * 3.14159 / 180.0
        #mismo numero salen igual, diferente, diferente proporcion
        #Agregar resta (Angulo/coseno) hace que la figura baje
        #Agregar suma (Angulo/coseno) hace que la figura suba
        glVertex3f(cos(angulo) * 0.2 + 0.65, sin(angulo) * 0.2 + 0.2, 0.0)
    glEnd()

def dibujarHojasdeArbol1():
    glColor3f(0.133,0.741,0.223)
    glBegin(GL_POLYGON)
    for x in range(360): 
        angulo = x * 3.14159 / 180.0
        #mismo numero salen igual, diferente, diferente proporcion
        #Agregar resta (Angulo/coseno) hace que la figura baje
        #Agregar suma (Angulo/coseno) hace que la figura suba
        glVertex3f(cos(angulo) * 0.2 + 0.6, sin(angulo) * 0.2 - 0.1, 0.0)
    glEnd()

def dibujarOyodelArbol():
    glColor3f(0.549,0.321,0.003)
    glBegin(GL_POLYGON)
    for x in range(360): 
        angulo = x * 3.14159 / 180.0
        #mismo numero salen igual, diferente, diferente proporcion
        #Agregar resta (Angulo/coseno) hace que la figura baje
        #Agregar suma (Angulo/coseno) hace que la figura suba
        glVertex3f(cos(angulo) * 0.05 + 0.77, sin(angulo) * 0.05 - 0.4, 0.0)
    glEnd()

def dibujarBasedelArbol():
    glColor3f(0.741, 0.509, 0.184)
    glBegin(GL_QUADS)
    glVertex(0.85,-0.1,0.0)
    glVertex(0.7,-0.1,0.0)
    glVertex(0.7,-0.75,0.0)
    glVertex(0.85,-0.75,0.0)
    glEnd()

def dibujarTecho(): 
 #rutinas de dibujo
    glBegin(GL_TRIANGLES)
    glColor3f(0.549,0.321,0.003)
    glVertex3f(-0.6,0.3,0.0)
    glVertex3f(0.0,0.7,0.0)
    glVertex3f(0.6,0.3,0.0)
    glEnd()

def dibujarVentana1():
    glColor3f(0.0,0.764,1.0)
    glBegin(GL_QUADS)
    glVertex(0.12,0.07,0.0)
    glVertex(0.23,0.07,0.0)
    glVertex(0.23,-0.09,0.0)
    glVertex(0.12,-0.09,0.0)
    glEnd()


def dibujarVentana4():
    glColor3f(0.0,0.764,1.0)
    glBegin(GL_QUADS)
    glVertex(0.27,-0.12,0.0)
    glVertex(0.38,-0.12,0.0)
    glVertex(0.38,-0.28,0.0)
    glVertex(0.27,-0.28,0.0)
    glEnd()


def dibujarVentana3():
    glColor3f(0.0,0.764,1.0)
    glBegin(GL_QUADS)
    glVertex(0.12,-0.12,0.0)
    glVertex(0.23,-0.12,0.0)
    glVertex(0.23,-0.28,0.0)
    glVertex(0.12,-0.28,0.0)
    glEnd()


def dibujarVentana2():
    glColor3f(0.0,0.764,1.0)
    glBegin(GL_QUADS)
    glVertex(0.27,0.07,0.0)
    glVertex(0.38,0.07,0.0)
    glVertex(0.38,-0.09,0.0)
    glVertex(0.27,-0.09,0.0)
    glEnd()

def dibujarBaseVentana():
    glColor3f(0.549,0.321,0.003)
    glBegin(GL_QUADS)
    glVertex(0.1,0.1,0.0)
    glVertex(0.401,0.1,0.0)
    glVertex(0.401,-0.3,0.0)
    glVertex(0.1,-0.3,0.0)
    glEnd()

def dibujarPuerta():
    glColor3f(0.949, 0.552, 0.0)
    glBegin(GL_QUADS)
    glVertex(-0.3,-0.2,0.0)
    glVertex(-0.0,-0.2,0.0)
    glVertex(-0.0,-0.6,0.0)
    glVertex(-0.3,-0.6,0.0)
    glEnd()

def dibujarCasaBase():
    glColor3f(1, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex(-0.5,0.3,0.0)
    glVertex(0.5,0.3,0.0)
    glVertex(0.5,-0.6,0.0)
    glVertex(-0.5,-0.6,0.0)
    glEnd()
    

def dibujarPasto():
    glColor3f(0.427, 0.819, 0.321)
    glBegin(GL_QUADS)
    glVertex(-1.0,-0.4,0.0)
    glVertex(1.0,-0.4,0.0)
    glVertex(1.0,-1.0,0.0)
    glVertex(-1.0,-1.0,0.0)
    glEnd()

def dibujarSol():
    glColor3f(0.949,0.874,0.047)
    glBegin(GL_POLYGON)
    for x in range(360): 
        angulo = x * 3.14159 / 180.0
        #mismo numero salen igual, diferente, diferente proporcion
        #Agregar resta (Angulo/coseno) hace que la figura baje
        #Agregar suma (Angulo/coseno) hace que la figura suba
        glVertex3f(cos(angulo) * 0.2 - 0.7 , sin(angulo) * 0.2 + 0.7, 0.0)
    glEnd()

def dibujarRallos1():
    glBegin(GL_TRIANGLES)
    glColor3f(0.949,0.874,0.047)
    glVertex3f(-0.95,0.7,0.0)
    glVertex3f(-0.7,0.95,0.0)
    glVertex3f(-0.45,0.7,0.0)
    glEnd()

def dibujarRallos2():
    glBegin(GL_TRIANGLES)
    glColor3f(0.949,0.874,0.047)
    glVertex3f(-0.82,0.9,0.0)
    glVertex3f(-0.52,0.85,0.0)
    glVertex3f(-0.55,0.5,0.0)
    glEnd()

def dibujarRallos3():
    glBegin(GL_TRIANGLES)
    glColor3f(0.949,0.874,0.047)
    glVertex3f(-0.95,0.7,0.0)
    glVertex3f(-0.7,0.45,0.0)
    glVertex3f(-0.45,0.7,0.0)
    glEnd()

def dibujarRallos4():
    glBegin(GL_TRIANGLES)
    glColor3f(0.949,0.874,0.047)
    glVertex3f(-0.82,0.9,0.0)
    glVertex3f(-0.9,0.55,0.0)
    glVertex3f(-0.55,0.5,0.0)
    glEnd()

def dibujarPerilla():
    glColor3f(0.549,0.321,0.003)
    glBegin(GL_POLYGON)
    for x in range(360): 
        angulo = x * 3.14159 / 180.0
        #mismo numero salen igual, diferente, diferente proporcion
        #Agregar resta (Angulo/coseno) hace que la figura baje
        #Agregar suma (Angulo/coseno) hace que la figura suba
        glVertex3f(cos(angulo) * 0.02 - 0.04 , sin(angulo) * 0.02 - 0.4, 0.0)
    glEnd()

def dibujarBanqueta():
    glColor3f(0.435, 0.450, 0.439)
    glBegin(GL_QUADS)
    glVertex(-0.5,-0.6,0.0)
    glVertex(0.5,-0.6,0.0)
    glVertex(1.0,-1.0,0.0)
    glVertex(-1.0,-1.0,0.0)
    glEnd()

def dibujar():
    dibujarPasto()
    dibujarSol()
    dibujarCasaBase()
    dibujarNube1()
    dibujarNube2()
    dibujarNube3()
    dibujarTecho()
    dibujarPuerta()
    dibujarPerilla()
    dibujarBaseVentana()
    dibujarVentana1()
    dibujarVentana2()
    dibujarVentana3()
    dibujarVentana4()
    dibujarBanqueta()
    dibujarBasedelArbol()
    dibujarOyodelArbol()
    dibujarHojasdeArbol1()
    dibujarHojasdeArbol2()
    dibujarHojasdeArbol3()
    dibujarHojasdeArbol4()
    dibujarHojasdeArbol5()
    dibujarRallos1()
    dibujarRallos2()
    dibujarRallos3()
    dibujarRallos4()
    

#----------------------------CASA------------------------

def dibujarTriangulos(): 
 #rutinas de dibujo
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0,0,)
    glVertex3f(-0.5,0.0,0.0)
    #glColor3f(1.0,0.8,0,)
    glVertex3f(0.0,0.5,0.0)
    #glColor3f(1.0,0.0,1.0,)
    glVertex3f(0.5,0.0,0.0)

    glColor3f(0.0,0,1.0)
    glVertex3f(-0.4,-0.2,0.0)
    glColor3f(0.0,1.0,0.0)
    glVertex3f(-0.6,-0.4,0.0)
    glColor3f(1.0,0.0,0.0)
    glVertex3f(-0.2,-0.4,0.0)
    glEnd()

def dibujarPuntos():    
    glBegin(GL_POINTS)
    glVertex3f(0.0,0.0,0.0)
    glEnd()

def dibujarLineas():
    glBegin(GL_LINES)
    glVertex3f(-0.8,0.5,0.0)
    glVertex3f(-0.8,0.3,0.0)

    glVertex3f(-0.6,0.5,0.0)
    glVertex3f(-0.5,0.3,0.0)
    glEnd()

def dibujarLineasContinua():
    glBegin(GL_LINE_STRIP)
    glVertex3f(-0.8,0.5,0.0)
    glVertex3f(-0.8,0.3,0.0)

    glVertex3f(-0.6,0.5,0.0)
    glVertex3f(-0.5,0.3,0.0)

    glVertex3f(-0.3,0.5,0.0)
    glEnd()

def dibujarCicloLinea():
    glBegin(GL_LINE_LOOP)
    glVertex3f(-0.8,0.5,0.0)
    glVertex3f(-0.8,0.3,0.0)

    glVertex3f(-0.6,0.5,0.0)
    glVertex3f(-0.5,0.3,0.0)

    glVertex3f(-0.3,0.5,0.0)
    glEnd()

def dibujarRectangulos():
    glBegin(GL_QUADS)
    glVertex3f(-0.2,0.2,0.0)
    glVertex3f(0.4,0.2,0.0)
    glVertex3f(0.4,-0.2,0.0)
    glVertex3f(-0.2,-0.2,0.0)
    glEnd()

def dibujarPoligono():
    glBegin(GL_POLYGON)
    #glVertex3f(-0.8,0.5,0.0)
    #glVertex3f(-0.8,0.3,0.0)
    #glVertex3f(-0.6,0.5,0.0)
    #glVertex3f(-0.5,0.3,0.0)
    #glVertex3f(-0.3,0.5,0.0)

    glVertex(0.0,0.0,0.0)
    glVertex(0.0,0.2,0.0)
    glVertex(0.2,0.2,0.0)
    glVertex(0.2,0.0,0.0)
    glEnd()


#def dibujar():
 #   glColor3f(1.0,0.0,0.0)
    #dibujarTriangulos()
    #dibujarPuntos()
    #dibujarLineas()
    #dibujarLineasContinua()
    #dibujarCicloLinea()
    #dibujarRectangulos()
    #dibujarPoligono()

def main():
    #inicia glfw
    ancho = 800
    alto = 800
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(ancho,alto,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0.0,0.764,1.0,0)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()