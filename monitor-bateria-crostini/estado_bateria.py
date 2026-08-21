import tkinter as tk
import psutil
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def actualizar_bateria():
    bateria = psutil.sensors_battery()
    porcentaje = bateria.percent
    estado = "Cargando" if bateria.power_plugged else "Descargando"

    # Actualizar etiqueta
    etiqueta_bateria.config(text=f"Batería: {porcentaje}% ({estado})")

    # Actualizar gráfico
    axes.clear()
    
    # Barra horizontal verde que se llena de izquierda a derecha
    axes.barh("Nivel", porcentaje, color='limegreen')
    
    # Ajustes para el gráfico
    axes.set_xlim(0, 100)  # Limitar el eje X de 0 a 100%
    axes.set_yticks([])    # Ocultar la etiqueta "Nivel" del eje Y
    axes.set_xticks([])    # Ocultar los números del eje X

    # Mostrar el porcentaje en el centro de la barra
    axes.text(0.5, 0.5, f"{porcentaje}%", ha='center', va='center', 
              fontsize=10, transform=axes.transAxes)
    
    canvas.draw()
    ventana.after(1000, actualizar_bateria)  # Actualizar cada 1 segundo

ventana = tk.Tk()
ventana.title("Estado de la batería")

# Crear figura y ejes de Matplotlib (tamaño ajustado)
figura, axes = plt.subplots(figsize=(2, 0.5))  # Ajustar ancho y alto
canvas = FigureCanvasTkAgg(figura, master=ventana)
canvas.get_tk_widget().pack()

etiqueta_bateria = tk.Label(ventana, text="")
etiqueta_bateria.pack()

actualizar_bateria()

ventana.mainloop()
