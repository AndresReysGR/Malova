from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

rotacion = 0.0

#cpara calcular color (Numero del colorRGB)/255*1
#Grados a radiales 1° × π/180

#---------------------------Anillo--------------------------

#orillasBase
def dibujarOrillaBase():
    glColor3f(0.564, 0.047, 0.247)
    glBegin(GL_QUADS)
    glVertex(-0.66,-0.82,0.0)
    glVertex(0.66,-0.82,0.0)
    glVertex(0.67,-0.84,0.0)
    glVertex(-0.67,-0.84,0.0)
    glEnd()

def dibujarOrillaBaseDerecha():
    glColor3f(0.564, 0.047, 0.247)
    glBegin(GL_QUADS)
    glVertex(0.48,-0.1,0.0)
    glVertex(0.49,-0.1,0.0)
    glVertex(0.68,-0.84,0.0)
    glVertex(0.665,-0.82,0.0)
    glEnd()

def dibujarOrillaBaseIzquierda():
    glColor3f(0.564, 0.047, 0.247)
    glBegin(GL_QUADS)
    glVertex(-0.48,-0.1,0.0)
    glVertex(-0.49,-0.1,0.0)
    glVertex(-0.68,-0.84,0.0)
    glVertex(-0.665,-0.82,0.0)
    glEnd()

#orilasArriba
def dibujarOrillaArriba():
    glColor3f(0.564, 0.047, 0.247)
    glBegin(GL_QUADS)
    glVertex(-0.66,0.62,0.0)
    glVertex(0.66,0.62,0.0)
    glVertex(0.67,0.64,0.0)
    glVertex(-0.67,0.64,0.0)
    glEnd()

def dibujarOrillaArribaDerecha():
    glColor3f(0.564, 0.047, 0.247)
    glBegin(GL_QUADS)
    glVertex(0.48,-0.1,0.0)
    glVertex(0.49,-0.1,0.0)
    glVertex(0.68,0.635,0.0)
    glVertex(0.665,0.615,0.0)
    glEnd()

def dibujarOrillaArribaIzquierda():
    glColor3f(0.564, 0.047, 0.247)
    glBegin(GL_QUADS)
    glVertex(-0.48,-0.1,0.0)
    glVertex(-0.49,-0.1,0.0)
    glVertex(-0.68,0.635,0.0)
    glVertex(-0.665,0.615,0.0)
    glEnd()


#Bases
def dibujarBaseAnillo():
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex(-0.5,-0.1,0.0)
    glVertex(0.5,-0.1,0.0)
    glVertex(0.69,-0.85,0.0)
    glVertex(-0.69,-0.85,0.0)
    glEnd()

def dibujarparteAlta():
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex(-0.5,-0.1,0.0)
    glVertex(0.5,-0.1,0.0)
    glVertex(0.69,0.65,0.0)
    glVertex(-0.69,0.65,0.0)
    glEnd()

#Cascara
def dibujarparteAltaCascara():
    glColor3f(0.564, 0.047, 0.247)
    glBegin(GL_QUADS)
    glVertex(-0.5,0.9,0.0)
    glVertex(0.5,0.9,0.0)
    glVertex(0.69,0.65,0.0)
    glVertex(-0.69,0.65,0.0)
    glEnd()

def dibujarBaseAnilloCascara():
    glColor3f(0.564, 0.047, 0.247)
    glBegin(GL_QUADS)
    glVertex(-0.5,-0.9,0.0)
    glVertex(0.5,-0.9,0.0)
    glVertex(0.69,-0.85,0.0)
    glVertex(-0.69,-0.85,0.0)
    glEnd()

#Agarre
def dibujarBaseAnilloAgarre():
    glColor3f(1,0.478,0.698)
    glBegin(GL_QUADS)
    glVertex(-0.25,-0.1,0.0)
    glVertex(0.25,-0.1,0.0)
    glVertex(0.3,-0.15,0.0)
    glVertex(-0.3,-0.15,0.0)
    glEnd()

def dibujarparteAltaAgarre():
    glColor3f(1,0.478,0.698)
    glBegin(GL_QUADS)
    glVertex(-0.25,-0.1,0.0)
    glVertex(0.25,-0.1,0.0)
    glVertex(0.3,0.05,0.0)
    glVertex(-0.3,0.05,0.0)
    glEnd()

#Forma de Anillo

def dibujarAnilloAbajo():
    glColor3f(0.980,0.831,0)
    glBegin(GL_POLYGON)
    for x in range(360): 
        angulo = x * 3.14159 / 180.0
        #mismo numero salen igual, diferente, diferente proporcion
        #Agregar resta (Angulo/coseno) hace que la figura baje
        #Agregar suma (Angulo/coseno) hace que la figura suba
        glVertex3f(cos(angulo) * 0.15 - 0.01 , sin(angulo) * 0.15 - 0.4, 0.0)
    glEnd()

def dibujarAnilloArriba():
    glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    for x in range(360): 
        angulo = x * 3.14159 / 180.0
        #mismo numero salen igual, diferente, diferente proporcion
        #Agregar resta (Angulo/coseno) hace que la figura baje
        #Agregar suma (Angulo/coseno) hace que la figura suba
        glVertex3f(cos(angulo) * 0.13 - 0.01 , sin(angulo) * 0.1 - 0.4, 0.0)
    glEnd()

def dibujarTaparAnillo():
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex(-0.5,-0.38,0.0)
    glVertex(0.5,-0.38,0.0)
    glVertex(0.69,-0.85,0.0)
    glVertex(-0.69,-0.85,0.0)
    glEnd()

#Diamante
    #Triangulo1
def dibujarDiamante1(): 
    glBegin(GL_TRIANGLES)
    glColor3f(0.0,0.933,1.0)
    glVertex3f(-0.01,-0.4,0.0)
    glColor3f(0.0,0.968,1.0)
    glVertex3f(0.08,-0.25,0.0)
    glColor3f(0.0,1.0,0.933)
    glVertex3f(-0.1,-0.25,0.0)
    glEnd()    

    #Triangulo2

def dibujarDiamante2():
    glBegin(GL_POLYGON)
    glVertex(-0.1,-0.17,0.0)
    glVertex(-0.12,-0.24,0.0)
    glVertex(0.1,-0.24,0.0)
    glVertex(0.08,-0.17,0.0)
    glEnd()

#Brillo
def dibujarBrillo(): 
    glPushMatrix()
    glTranslatef(0.4,0,0)
    glRotatef(rotacion,0,0,1)
    
    glBegin(GL_TRIANGLES)
    glColor3f(0.980,0.831,0)
    glVertex3f(-0.485,-0.25,0)
    #glColor3f(1.0,0.0,0.0)
    glVertex3f(-0.5,-0.19,0)
    #glColor3f(0.0,0.0,1.0)
    glVertex3f(-0.46,-0.15,0)
    glEnd()
    glPopMatrix()


def dibujar():
    dibujarBaseAnillo()
    dibujarparteAlta()
    dibujarparteAltaAgarre()
    dibujarBaseAnilloAgarre()
    dibujarparteAltaCascara()
    dibujarBaseAnilloCascara()
    dibujarAnilloAbajo()
    dibujarAnilloArriba()
    dibujarTaparAnillo()
    dibujarOrillaBase()
    dibujarOrillaBaseDerecha()
    dibujarOrillaBaseIzquierda()
    dibujarOrillaArriba()
    dibujarOrillaArribaDerecha()
    dibujarOrillaArribaIzquierda()
    dibujarDiamante1()
    dibujarDiamante2()
    dibujarBrillo()
   
    

#----------------------------Anillo------------------------

def main():
    #inicia glfw
    ancho = 1920
    alto = 1080
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
        glViewport(0,0,1920,1080)
        #Establece color de borrado
        glClearColor(1,0.478,0.698,0)
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