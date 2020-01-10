# ePresence 🎓

<!-- TABLE OF CONTENTS -->
## Tabla de Contenidos

* [Sobre el proyecto](#sobre-el-proyecto)
  * [Hecho con](#hecho-con)
* [Documentación](#documentación)
* [Contribuidores](#contribuidores)
* [Créditos](#creditos)


<!-- ABOUT THE PROJECT -->
## Sobre el proyecto

ePresence es un sistema IoT para gestionar las aulas de cualquier centro de estudios. Consiste en saber cuántas personas entran, permanecen y salen del aula a tiempo real, así sabremos si una clase está ocupada o libre. Mediante un semáforo led sabremos si la clase está abierta (verde), ocupada (amarillo) o cerrada (rojo). Para saber si una clase esta cerrada bastará con saber si está fuera del horario establecido a ese aula.


### Hecho con
* [DjangoRest](https://www.django-rest-framework.org/) - Serverside
* [Grove Base Hat for Raspberry Pi](http://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/) - Hardware
* [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) - Hardware

<!-- GETTING STARTED -->
## Documentación

### Server
### IoT

En cuanto al hardware, hemos utilizado una Raspberry Pi 3 junto con una Grove Base Hat que nos permite añadir varios componentes como tres LED Sockets que hemos utilizado para hacer un semáforo y dos botones que hemos utilizado para sumar y restar en el contador de personas.

Para hacer uso de los componentes así como desarrollar sus funcionalidades, hemos creado la clase mainController en lenguaje python donde hemos desarrollado todo el código para poder hacer uso del hardware. 

Hemos inicializado 3 leds uno para cada color del semáforo (ledV, ledA y ledR) donde asignaremos el número de puerto al que está concectado en la Raspberry Pi.

```python
ledV = GroveLed(5)
ledA = GroveLed(16)
ledR = GroveLed(18)
```

También hemos inicializado los 2 botones, uno tiene el método de añadir una persona y el otro de restar una persona

```python
btn_in = GroveButton(22)
btn_out = GroveButton(24)

def on_press_in(t):
	aula_add()

def on_press_out(t):
	aula_remove()

btn_in.on_press = on_press_in
btn_out.on_press = on_press_out
```

El probrama principal se basa en un bucle de los métodos check() y update() que explicaremos a continuación.

```python
#Main Program
while True:
	check()
	update()
```

El método check() comprueba constantemente mediante una petición a la URL del aula. Para definir en que estado debe estar el aula debemos comprobar en primer lugar si estamos dentro del horario, para ello hemos creado 3 variables de tiempo : la hora de entrada (h_in), la hora de salida (h_out) y la hora actual (h_act). De esta manera, sabremos si la hora actual está dentro o fuera del horario establecido a ese aula.

```python
def check():
	res = requests.get('http://localhost:8000/api/Aula/1/')
	testJson = json.loads(res.text)
	global estado
	if estado!=testJson['estado']:
		estado = testJson['estado']

	h_in = datetime.strptime(testJson['hora_in'],'%H:%M:%S').time()
	h_out = datetime.strptime(testJson['hora_out'],'%H:%M:%S').time()
	h_act = datetime.now().time()

	if h_out > h_in:
		if h_act > h_in and h_act < h_out:
			if testJson['personas']==0:
				aula_estado(0)
			else:
				aula_estado(1)
		else:
			aula_estado(2)
	else:
		if h_act > h_in or h_act < h_out:
			if testJson['personas']==0:
				aula_estado(0)
			else:
				aula_estado(1)
		else:
			aula_estado(2)
```
Las condiciones que hemos creado para establecer el estado del aula son: si la hora actual está dentro del horario y el número de personas que hay dentro es 0, el estado será aula_estado(0); si dentro del horario hubiese alguna persona sería aula_estado(1); si no se cumple ninguna de estas condiciones el estado será aula_estado(2).

Los diferentes casos para aula_estado() son los siguientes:

```python
def aula_estado(st):
	if st==0:
		requests.get('http://localhost:8000/aulaVerde/1/')
	elif st==1:
		requests.get('http://localhost:8000/aulaAmarillo/1/')
	elif st==2:
		requests.get('http://localhost:8000/aulaRojo/1/')

```
Donde aula_estado(0) sería para el verde, aula_estado(1) para el amarillo y aula_estado(2) para el rojo.

En cuanto al método update(), actualiza constantemente el estado de los leds comprobando el estado del aula ( aula_estado() ) y dependiendo del estado del aula enciende su led correspondiente.

```python
def update():
	global estado
	if estado == 0:
		ledV.on()
		ledA.off()
		ledR.off()
		#abrir puerta
	elif estado == 1:
		ledV.off()
		ledA.on()
		ledR.off()
		#abrir puerta
	elif estado == 2:
		ledV.off()
		ledA.off()
		ledR.on()
		#bloquear puerta
```

<!-- CONTRIBUTORS -->
## Contribuidores

* **Alberto Miranda**	-	*alberto.miranda@opendeusto.es*	-	[@AlbertoMGV](https://github.com/AlbertoMGV)
* **Iñigo de Mingo**	-	*inigo.demingo@opendeusto.es*	-	[@InigodeMingo](https://github.com/InigodeMingo)

## Creditos

- Gracias al template [ Gentelella ](https://github.com/ColorlibHQ/gentelella) by ColorlibHQ.



