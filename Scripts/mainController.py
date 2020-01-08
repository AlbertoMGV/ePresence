import time
from grove.grove_led import GroveLed
from grove.grove_button import GroveButton

estado = 0;

#Set leds

ledV = GroveLed(5)
ledA = GroveLed(16)
ledR = GroveLEd(18)

#Set "cerradura"



#Set Buttons

btn_in = GroveButton(22)
btn_out = GroveButton(24)

def on_press_in(t):
	aula_add()

def on_press_out(t):
	aula_remove()

btn_in.on_press = on_press_in
btn_out.on_press = on_press_out

#Functions

def check():
	#request to web
	#comparar el estado que viene con el que estaba para no petar a peticiones la api
	#si la hora no esta entre las dos de in y out cambiar stado "aula_stado(estado)"

def update():
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

def aula_add():
	#request a url 

def aula_remove():
	#request a url

def aula_estado(st):
	#request a url

#Main Program

while True:
	check()
	update()
	time.sleep(1)
