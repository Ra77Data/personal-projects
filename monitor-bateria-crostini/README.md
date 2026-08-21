## Monitor de batería para ChromeOS (Crostini)

Este pequeño script en Python te permite visualizar el estado de la batería de tu Chromebook en tiempo real, mostrando el porcentaje de carga con una barra horizontal dinámica. 

### Requisitos

* **Chromebook con Crostini habilitado:** Asegúrate de tener el entorno Linux (Beta) activado en tu Chromebook. 
* **Terminal de Linux:** Accederás a ella desde el cajón de aplicaciones de ChromeOS una vez que Crostini esté instalado.

### Instalación

 **Instalar las bibliotecas necesarias:**
   ```bash
   sudo apt update
   sudo apt install python3 python3-tk python3-psutil python3-matplotlib
   ```

### Ejecución

 **Ejecutar el script:**
   ```bash
   python3 estado_bateria.py
   ```

### Detalles de la aplicación

- El script utiliza `psutil` para acceder a la información de la batería del sistema.
- La biblioteca `matplotlib` se emplea para crear el gráfico de barras dinámico.
- `Tkinter` proporciona la ventana principal de la aplicación y los elementos de la interfaz gráfica. 

### Autor 

@Ra77Data

### Licencia 

GPL-3.0

