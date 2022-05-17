# API Edad Poblacional

**ADJUNTO DOCUMENTACIÓN DE LA API**
*LINK https://documenter.getpostman.com/view/18843205/Uyxkk5s8 *

*Esta es una API que usa datos de INEGI*

## Comenzamos! 🚀

*Estas instrucciones te ayudarán a ejecutar el proyecto localmente.*

## Requisitos 📋

*Usa git clone o descarga el zip para tener este proyecto en tu equipo.*
*Navega a la raíz del proyecto.*

### Virtual environments
*Necesitas crear un entorno virtual (Windows): *
```
pip install virtualenv
virtualenv venv 
```
*Ahora, activamos el entorno virtual (Windows and PowerShell): *
```
.\venv\Scripts\activate
```

*Necesitas crear un entorno virtual (Linux): *
```
pip3 install virtualenv
virtualenv venv 
```
*Ahora, activamos el entorno virtual (Bash): *
```
. venv/bin/activate
```

### Cómo instalamos las dependencias del proyecto?
*Dentro del proyecto hay un archivo llamado **requirements.txt**, este archivo te ayudará para instalar todos los paquetes necesarios.*

*Escribe el siguiente comando en una terminal: **CMD or Powershell**: *
```
pip install -r requirements.txt
```
**Recuerda que debes estar en la raíz del proyecto.**


## Cómo ejecutar el proyecto? ⚙️

### Forma 1

*Puedes correr el proyecto con los siguientes comandos (CMD): *
```
> set FLASK_APP=app.py
> flask run
 * Running on http://IP:5000/
 ...
 ...
```

*Si usas PowerShell: *
```
> $env:FLASK_APP = "app.py"
> flask run
 * Running on http://IP:5000/
 ...
 ...
```

*Si usas bash de Linux: *
```
> export FLASK_APP = "app.py"
> flask run
 * Running on http://IP:5000/
 ...
 ...
```

### Forma 2

*Usa el archivo app.py para correr el proyecto (Windows): *
```
> python app.py
 * Running on http://IP/
 ...
 ...
```

*Usa el archivo app.py para correr el proyecto (Linux): *
```
> python3 app.py
 * Running on http://IP/
 ...
 ...
```

### Forma 3

*Dentro del proyecto esta un archivo llamado **Dockerfile**. Usa este archivo para crear una imagen y después ejecutar un contenedor dentro de tu equipo.*

**Para ejecutar el archivo Dockerfiel debes tener instalado Docker en tu equipo. Dirigite a la página oficial de Docker y navega en la documentación para ver como 
instalar Docker en tu máquina.**

*Nos colocamos dentro de la raíz del proyecto y ejecutamos lo siguiente: *
```
> docker build --tag [nombre_de_nuestra_imagen] .
...
...
...
```
**Este comando creará una imagen de tu proyecto e instalará las dependencias del proyecto.**

*Verificamos que la imagen se haya creado con el comando: *
```
> docker images 
```

*Vamos a crear nuestro contenedor y ejectuar el proyecto exponiendolo en un puerto para realizar peticiones HTTP*
```
> docker run -d -p 5000:5000 [nombre_de_nuestra_imagen]
```

**Ahora podemos testear la API con POSTMAN escribiendo la ruta http://127.0.0.1:5000/api/edad **
**No olvides pasar el JSON como body para obtener la edad poblacional de la entidad federativa que deseas**







