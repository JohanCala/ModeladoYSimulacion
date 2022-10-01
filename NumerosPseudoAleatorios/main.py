
##### paquetes de graficos

import matplotlib.pyplot as plot
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from scipy import stats
import statistics
#####   paquetes de interfaz grafica
import tkinter as tk
from tkinter import ttk

##### metodos

from Funciones.Metodos import *
from Funciones.Pruebas import *
from Funciones.VariablesAleatorias import *

# - - - - - - - - - - - - - - - - - Funciones - - - - - - - - - - - - - - - - - - - - - - - -

def validacion_1(event):
    
    entrada_num_1['state'] = "disabled"
    entrada_num_2['state'] = "disabled"
    entrada_num_3['state'] = "disabled"
    entrada_num_4['state'] = "disabled"
    entrada_num_5['state'] = "disabled"
    entrada_num_6['state'] = "disabled"
    if combo_1.get() == 'Normal':
        entrada_num_1['state'] = "normal"
        entrada_num_2['state'] = "normal"
    if combo_1.get() == 'Logaritmica Normal':
        entrada_num_1['state'] = "normal"
        entrada_num_2['state'] = "normal"
    if combo_1.get() == 'Chi Cuadrada':
        entrada_num_1['state'] = "normal"
        entrada_num_2['state'] = "normal"
        entrada_num_3['state'] = "normal"
        entrada_num_4['state'] = "normal"
        entrada_num_5['state'] = "normal"
        entrada_num_6['state'] = "normal"
    if combo_1.get() == 'Distribucion T':
        entrada_num_1['state'] = "normal"
        entrada_num_2['state'] = "normal"
        entrada_num_3['state'] = "normal"
        entrada_num_4['state'] = "normal"
        entrada_num_5['state'] = "normal"
        entrada_num_6['state'] = "normal"
    if combo_1.get() == 'Distribucion F':
        entrada_num_1['state'] = "normal"
        entrada_num_2['state'] = "normal"
        entrada_num_3['state'] = "normal"
        entrada_num_4['state'] = "normal"
    
    if combo_1.get() == 'Distribucion Exponencial':
        entrada_num_1['state'] = "normal"
        entrada_num_2['state'] = "normal"
    if combo_1.get() == 'Distribucion Gamma':
        entrada_num_1['state'] = "normal"
        entrada_num_2['state'] = "normal"
        
        
    
        
        

def validacion_2(event):
    entrada_num_7['state'] = "disabled"
    entrada_num_8['state'] = "disabled"
    entrada_num_9['state'] = "disabled"
    entrada_num_10['state'] = "disabled"
    entrada_num_11['state'] = "disabled"
    entrada_num_12['state'] = "disabled"
    
    if combo_2.get() == 'MetodoProductosMedios':
        if combo_1.get() == 'Normal':
            entrada_num_7['state'] = "normal"
            entrada_num_8['state'] = "normal"
        if combo_1.get() == 'Logaritmica Normal':
            entrada_num_7['state'] = "normal"
            entrada_num_8['state'] = "normal"
        if combo_1.get() == 'Chi Cuadrada':
            entrada_num_7['state'] = "normal"
            entrada_num_8['state'] = "normal"
            entrada_num_9['state'] = "normal"
            entrada_num_10['state'] = "normal"
            entrada_num_11['state'] = "normal"
            entrada_num_12['state'] = "normal"
        if combo_1.get() == 'Distribucion T':
            entrada_num_7['state'] = "normal"
            entrada_num_8['state'] = "normal"
            entrada_num_9['state'] = "normal"
            entrada_num_10['state'] = "normal"
            entrada_num_11['state'] = "normal"
            entrada_num_12['state'] = "normal"
        if combo_1.get() == 'Distribucion F':
            entrada_num_7['state'] = "normal"
            entrada_num_8['state'] = "normal"
            entrada_num_9['state'] = "normal"
            entrada_num_10['state'] = "normal"
        
        if combo_1.get() == 'Distribucion Exponencial':
            entrada_num_7['state'] = "normal"
            entrada_num_8['state'] = "normal"
        if combo_1.get() == 'Distribucion Gamma':
            entrada_num_7['state'] = "normal"
            entrada_num_8['state'] = "normal"


def Dnormal():
    if combo_2.get() == 'MetodoCuadradosMedios':
        r1 = MetodoCuadradosMedios(semilla_1.get(), cantidad.get())
        r2 = MetodoCuadradosMedios(semilla_2.get(), cantidad.get())
    
        
    if combo_2.get() == 'MetodoProductosMedios':
        r1 = MetodoProductosMedios(semilla_1.get(), semilla_7.get(), cantidad.get())
        r2 = MetodoProductosMedios(semilla_2.get(), semilla_8.get(), cantidad.get())
        
    if combo_2.get() == 'Fortran':
        r1 = fortran(semilla_1.get(), cantidad.get())
        r2 = fortran(semilla_2.get(), cantidad.get())
        
    if combo_2.get() == 'Visual Basic':
        r1 = visual_basic(semilla_1.get(), cantidad.get())
        r2 = visual_basic(semilla_2.get(), cantidad.get())
        
    
    dNormal = ziboxmullersen(r1, r2)
    return dNormal

def DlNor():
    if combo_2.get() == 'MetodoCuadradosMedios':
        r1 = MetodoCuadradosMedios(semilla_1.get(), cantidad.get())
        r2 = MetodoCuadradosMedios(semilla_2.get(), cantidad.get())
        
        
    if combo_2.get() == 'MetodoProductosMedios':
        r1 = MetodoProductosMedios(semilla_1.get(), semilla_7.get(), cantidad.get())
        r2 = MetodoProductosMedios(semilla_2.get(), semilla_7.get(), cantidad.get())
        
    if combo_2.get() == 'Fortran':
        r1 = fortran(semilla_1.get(), cantidad.get())
        r2 = fortran(semilla_2.get(), cantidad.get())
        
    if combo_2.get() == 'Visual Basic':
        r1 = visual_basic(semilla_1.get(), cantidad.get())
        r2 = visual_basic(semilla_2.get(), cantidad.get())
        
    dLnor = distribucionlognormal(ziboxmullersen(r1, r2))
    return dLnorl 

def ChiCuadr():
    if combo_2.get() == 'MetodoCuadradosMedios':
        r1 = MetodoCuadradosMedios(semilla_1.get(), cantidad.get())
        r2 = MetodoCuadradosMedios(semilla_2.get(), cantidad.get())
        r3 = MetodoCuadradosMedios(semilla_3.get(), cantidad.get())
        r4 = MetodoCuadradosMedios(semilla_4.get(), cantidad.get())
        r5 = MetodoCuadradosMedios(semilla_5.get(), cantidad.get())
        r6 = MetodoCuadradosMedios(semilla_6.get(), cantidad.get())
        
        
        
    if combo_2.get() == 'MetodoProductosMedios':
        r1 = MetodoProductosMedios(semilla_1.get(), semilla_7.get(), cantidad.get())
        r2 = MetodoProductosMedios(semilla_2.get(), semilla_8.get(), cantidad.get())
        r3 = MetodoProductosMedios(semilla_3.get(), semilla_9.get(), cantidad.get())
        r4 = MetodoProductosMedios(semilla_4.get(), semilla_10.get(), cantidad.get())
        r5 = MetodoProductosMedios(semilla_5.get(), semilla_11.get(), cantidad.get())
        r6 = MetodoProductosMedios(semilla_6.get(), semilla_12.get(), cantidad.get())
        
    if combo_2.get() == 'Fortran':
        r1 = fortran(semilla_1.get(), cantidad.get())
        r2 = fortran(semilla_2.get(), cantidad.get())
        r3 = fortran(semilla_1.get(), cantidad.get())
        r4 = fortran(semilla_2.get(), cantidad.get())
        r5 = fortran(semilla_1.get(), cantidad.get())
        r6 = fortran(semilla_2.get(), cantidad.get())
        
    if combo_2.get() == 'Visual Basic':
        r1 = visual_basic(semilla_1.get(), cantidad.get())
        r2 = visual_basic(semilla_2.get(), cantidad.get())
        r3 = visual_basic(semilla_3.get(), cantidad.get())
        r4 = visual_basic(semilla_4.get(), cantidad.get())
        r5 = visual_basic(semilla_5.get(), cantidad.get())
        r6 = visual_basic(semilla_6.get(), cantidad.get())
        
    chiCuadra = distribucionchicuadrado(ziboxmullersen(r1, r2), ziboxmullersen(r3, r4), ziboxmullersen(r5, r6))
    return chiCuadra

def Dt():
    if combo_2.get() == 'MetodoCuadradosMedios':
        r1 = MetodoCuadradosMedios(semilla_1.get(), cantidad.get())
        r2 = MetodoCuadradosMedios(semilla_2.get(), cantidad.get())
        r3 = MetodoCuadradosMedios(semilla_3.get(), cantidad.get())
        r4 = MetodoCuadradosMedios(semilla_4.get(), cantidad.get())
        r5 = MetodoCuadradosMedios(semilla_5.get(), cantidad.get())
        r6 = MetodoCuadradosMedios(semilla_6.get(), cantidad.get())
        
        
        
    if combo_2.get() == 'MetodoProductosMedios':
        r1 = MetodoProductosMedios(semilla_1.get(), semilla_7.get(), cantidad.get())
        r2 = MetodoProductosMedios(semilla_2.get(), semilla_8.get(), cantidad.get())
        r3 = MetodoProductosMedios(semilla_3.get(), semilla_9.get(), cantidad.get())
        r4 = MetodoProductosMedios(semilla_4.get(), semilla_10.get(), cantidad.get())
        r5 = MetodoProductosMedios(semilla_5.get(), semilla_11.get(), cantidad.get())
        r6 = MetodoProductosMedios(semilla_6.get(), semilla_12.get(), cantidad.get())
        
    if combo_2.get() == 'Fortran':
        r1 = fortran(semilla_1.get(), cantidad.get())
        r2 = fortran(semilla_2.get(), cantidad.get())
        r3 = fortran(semilla_1.get(), cantidad.get())
        r4 = fortran(semilla_2.get(), cantidad.get())
        r5 = fortran(semilla_1.get(), cantidad.get())
        r6 = fortran(semilla_2.get(), cantidad.get())
        
    if combo_2.get() == 'Visual Basic':
        r1 = visual_basic(semilla_1.get(), cantidad.get())
        r2 = visual_basic(semilla_2.get(), cantidad.get())
        r3 = visual_basic(semilla_3.get(), cantidad.get())
        r4 = visual_basic(semilla_4.get(), cantidad.get())
        r5 = visual_basic(semilla_5.get(), cantidad.get())
        r6 = visual_basic(semilla_6.get(), cantidad.get())
        
    dT = distribuciont(ziboxmullersen(r1, r2), ziboxmullersen(r3, r4), ziboxmullersen(r5,r6))
    
    return dT


def Df():
    if combo_2.get() == 'MetodoCuadradosMedios':
        r1 = MetodoCuadradosMedios(semilla_1.get(), cantidad.get())
        r2 = MetodoCuadradosMedios(semilla_2.get(), cantidad.get())
        r3 = MetodoCuadradosMedios(semilla_3.get(), cantidad.get())
        r4 = MetodoCuadradosMedios(semilla_4.get(), cantidad.get())
        
        
        
        
    if combo_2.get() == 'MetodoProductosMedios':
        r1 = MetodoProductosMedios(semilla_1.get(), semilla_7.get(), cantidad.get())
        r2 = MetodoProductosMedios(semilla_2.get(), semilla_8.get(), cantidad.get())
        r3 = MetodoProductosMedios(semilla_3.get(), semilla_9.get(), cantidad.get())
        r4 = MetodoProductosMedios(semilla_4.get(), semilla_10.get(), cantidad.get())
        
        
    if combo_2.get() == 'Fortran':
        r1 = fortran(semilla_1.get(), cantidad.get())
        r2 = fortran(semilla_2.get(), cantidad.get())
        r3 = fortran(semilla_1.get(), cantidad.get())
        r4 = fortran(semilla_2.get(), cantidad.get())
        
        
    if combo_2.get() == 'Visual Basic':
        r1 = visual_basic(semilla_1.get(), cantidad.get())
        r2 = visual_basic(semilla_2.get(), cantidad.get())
        r3 = visual_basic(semilla_3.get(), cantidad.get())
        r4 = visual_basic(semilla_4.get(), cantidad.get())
    
    dF = distribucionF(ziboxmullersen(r1, r2), ziboxmullersen(r3, r4))
    return dF

def Dexpo():
    if combo_2.get() == 'MetodoCuadradosMedios':
        r1 = MetodoCuadradosMedios(semilla_1.get(), cantidad.get())
        r2 = MetodoCuadradosMedios(semilla_2.get(), cantidad.get())
    
        
    if combo_2.get() == 'MetodoProductosMedios':
        r1 = MetodoProductosMedios(semilla_1.get(), semilla_7.get(), cantidad.get())
        r2 = MetodoProductosMedios(semilla_2.get(), semilla_8.get(), cantidad.get())
        
    if combo_2.get() == 'Fortran':
        r1 = fortran(semilla_1.get(), cantidad.get())
        r2 = fortran(semilla_2.get(), cantidad.get())
        
    if combo_2.get() == 'Visual Basic':
        r1 = visual_basic(semilla_1.get(), cantidad.get())
        r2 = visual_basic(semilla_2.get(), cantidad.get())
    
    dExpo = distribucionexponencial(ziboxmullersen(r1, r2))
    
    return dExpo

def Dgamma():
    if combo_2.get() == 'MetodoCuadradosMedios':
        r1 = MetodoCuadradosMedios(semilla_1.get(), cantidad.get())
        r2 = MetodoCuadradosMedios(semilla_2.get(), cantidad.get())
    
        
    if combo_2.get() == 'MetodoProductosMedios':
        r1 = MetodoProductosMedios(semilla_1.get(), semilla_7.get(), cantidad.get())
        r2 = MetodoProductosMedios(semilla_2.get(), semilla_8.get(), cantidad.get())
        
    if combo_2.get() == 'Fortran':
        r1 = fortran(semilla_1.get(), cantidad.get())
        r2 = fortran(semilla_2.get(), cantidad.get())
        
    if combo_2.get() == 'Visual Basic':
        r1 = visual_basic(semilla_1.get(), cantidad.get())
        r2 = visual_basic(semilla_2.get(), cantidad.get())
        
    dGamma = distribuciongamma(r1, r2)
    
    return dGamma


def Graph():
    if combo_1.get() == 'Normal':
        datos = Dnormal()
    if combo_1.get() == 'Logaritmica Normal':
        datos = DlNor()
    if combo_1.get() == 'Chi Cuadrada':
        datos = ChiCuadr()
    if combo_1.get() == 'Distribucion T':
        datos = Dt()
    if combo_1.get() == 'Distribucion F':
        datos = Df()
    if combo_1.get() == 'Distribucion Exponencial':
        datos = Dexpo()
    if combo_1.get() == 'Distribucion Gamma':
        datos = Dgamma()
    
    
    ventana_graf = tk.Tk()
    ventana_graf.title("Grafica De Distribucion")
    
    fig = Figure(figsize=(5, 4), dpi=100)
    plot=fig.add_subplot(111)
    plot.hist(datos)
    canvas = FigureCanvasTkAgg(fig, master=ventana_graf)
    canvas.draw()
    canvas.get_tk_widget().pack() 
    canvas.get_tk_widget().pack()
    
        
        

        
    
    
    
    
    
        
    
    


# - - - - - - - - - - - - - - - - - Main - - - - - - - - - - - - - - - - - - - - - - - -
distribuciones= ['Normal','Logaritmica Normal','Chi Cuadrada','Distribucion T','Distribucion F',
                 'Distribucion Exponencial','Distribucion Gamma']

generadores = ['MetodoCuadradosMedios','MetodoProductosMedios','Fortran','Visual Basic']


ventana = tk.Tk()
ventana.title("Modelado y Simulacion")
ventana.configure(bg="lightblue")
ventana.geometry("1380x980")

titulo = tk.Label(ventana,text='Generador de Variables Aleatorias',bg="lightblue",
                              fg="blue",
                              font="consolas 25 bold")
titulo.grid(padx=20, pady=20, row=0, column=0, columnspan=4)


#### Rotulos
rotulo_entry_1 = tk.Label(ventana,text='Ingrese Semilla: ',
                          bg="lightblue",fg="black",
                          font="consolas 14 bold")
rotulo_entry_1.grid(padx=1, pady=1, row=3, column=0, )

rotulo_entry_2 = tk.Label(ventana,text='Ingrese Semilla: ',
                          bg="lightblue",fg="black",
                          font="consolas 14 bold")
rotulo_entry_2.grid(padx=1, pady=1, row=4, column=0, )

rotulo_entry_3 = tk.Label(ventana,text='Ingrese Semilla: ',
                          bg="lightblue",fg="black",
                          font="consolas 14 bold")
rotulo_entry_3.grid(padx=1, pady=1, row=5, column=0, )

rotulo_entry_4 = tk.Label(ventana,text='Ingrese Semilla: ',
                          bg="lightblue",fg="black",
                          font="consolas 14 bold")
rotulo_entry_4.grid(padx=1, pady=1, row=6, column=0, )

rotulo_entry_5 = tk.Label(ventana,text='Ingrese Semilla: ',
                          bg="lightblue",fg="black",
                          font="consolas 14 bold")
rotulo_entry_5.grid(padx=0, pady=0, row=7, column=0, )

rotulo_entry_6 = tk.Label(ventana,text='Ingrese Semilla: ',
                          bg="lightblue",fg="black",
                          font="consolas 14 bold")
rotulo_entry_6.grid(padx=1, pady=1, row=8, column=0,)

rotulo_entry_6 = tk.Label(ventana,text='Cantidad ',
                          bg="lightblue",fg="black",
                          font="consolas 14 bold")
rotulo_entry_6.grid(padx=1, pady=1, row=9, column=0,)


rotulo_combo_1 = tk.Label(ventana,text='Distribucion: ',
                          bg="lightblue",fg="black",
                          font="consolas 14 bold")
rotulo_combo_1.grid(padx=5, pady=5, row=1, column=0, )
rotulo_combo_2 = tk.Label(ventana,text='Generador: ',
                          bg="lightblue",fg="black",
                          font="consolas 14 bold")
rotulo_combo_2.grid(padx=5, pady=5, row=2, column=0, )

### ComboBox's
combo_1 = ttk.Combobox(ventana,font="consolas 14 bold",
                                  width=16,
                                  values=distribuciones,
                                  state="readonly")
combo_1.grid(padx=10, pady=10, row=1, column=1)
combo_1.set('')
combo_1.bind("<<ComboboxSelected>>", validacion_1)


combo_2 = ttk.Combobox(ventana,font="consolas 14 bold",
                                  width=16,
                                  values=generadores,
                                  state="readonly")
combo_2.grid(padx=10, pady=10, row=2, column=1)
combo_2.set('')
combo_2.bind("<<ComboboxSelected>>", validacion_2)


### Entradas

semilla_1=tk.IntVar()
entrada_num_1 = tk.Entry(ventana,bg="White",fg="black",font="consolas 14 bold",state="disabled",textvariable =semilla_1)
entrada_num_1.grid(padx=1, pady=1, row=3, column=1)

semilla_2=tk.IntVar()
entrada_num_2 = tk.Entry(ventana,bg="White",fg="black",font="consolas 14 bold",state="disabled",textvariable =semilla_2)
entrada_num_2.grid(padx=1, pady=1, row=4, column=1)


semilla_3=tk.IntVar()
entrada_num_3 = tk.Entry(ventana,bg="White",fg="black",font="consolas 14 bold",state="disabled",textvariable =semilla_3)
entrada_num_3.grid(padx=1, pady=1, row=5, column=1)


semilla_4=tk.IntVar()
entrada_num_4 = tk.Entry(ventana,bg="White",fg="black",font="consolas 14 bold",state="disabled",textvariable =semilla_4)
entrada_num_4.grid(padx=1, pady=1, row=6, column=1)


semilla_5=tk.IntVar()
entrada_num_5 = tk.Entry(ventana,bg="White",fg="black",font="consolas 14 bold",state="disabled",textvariable =semilla_5)
entrada_num_5.grid(padx=1, pady=1, row=7, column=1)


semilla_6=tk.IntVar()
entrada_num_6 = tk.Entry(ventana,bg="White",fg="black",font="consolas 14 bold",state="disabled",textvariable =semilla_6)
entrada_num_6.grid(padx=1, pady=1, row=8, column=1)


#cuadrados medios 
semilla_7=tk.IntVar()
entrada_num_7 = tk.Entry(ventana,bg="White",fg="black",font="consolas 14 bold",state="disabled",textvariable =semilla_7)
entrada_num_7.grid(padx=1, pady=1, row=3, column=2)


semilla_8=tk.IntVar()
entrada_num_8 = tk.Entry(ventana,bg="White",fg="black",font="consolas 14 bold",state="disabled",textvariable =semilla_8)
entrada_num_8.grid(padx=1, pady=1, row=4, column=2)


semilla_9=tk.IntVar()
entrada_num_9 = tk.Entry(ventana,bg="White",fg="black",font="consolas 14 bold",state="disabled",textvariable =semilla_9)
entrada_num_9.grid(padx=1, pady=1, row=5, column=2)


semilla_10=tk.IntVar()
entrada_num_10 = tk.Entry(ventana,bg="White",fg="black",font="consolas 14 bold",state="disabled",textvariable =semilla_10)
entrada_num_10.grid(padx=1, pady=1, row=6, column=2)


semilla_11=tk.IntVar()
entrada_num_11 = tk.Entry(ventana,bg="White",fg="black",font="consolas 14 bold",state="disabled",textvariable =semilla_11)
entrada_num_11.grid(padx=1, pady=1, row=7, column=2)


semilla_12=tk.IntVar()
entrada_num_12 = tk.Entry(ventana,bg="White",fg="black",font="consolas 14 bold",state="disabled",textvariable =semilla_12)
entrada_num_12.grid(padx=1, pady=1, row=8, column=2)

#cantidad
cantidad=tk.IntVar()
entrada_num_13 = tk.Entry(ventana,bg="White",fg="black",font="consolas 14 bold",state="normal",textvariable =cantidad)
entrada_num_13.grid(padx=1, pady=1, row=9, column=1)

#Botones

my_button_1 = tk.Button(ventana, text="Generar", font="consolas 14 bold",command=Graph)
my_button_1.grid(padx=10, pady=10, row=4, column=4, columnspan=2)




ventana.mainloop()


