import time
from grove.grove_led import GroveLed
#from grove.grove_button import GroveButton
import requests
from io import BytesIO
import json
from datetime import datetime

estado = 69


#Set leds

ledV = GroveLed(5)
ledA = GroveLed(16)
ledR = GroveLed(18)

#Set "cerradura"



#Set Buttons

#btn_in = GroveButton(22)
#btn_out = GroveButton(24)

def on_press_in(t):
	aula_add()

def on_press_out(t):
	aula_remove()

#btn_in.on_press = on_press_in
#btn_out.on_press = on_press_out

#Functions

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

def aula_add():
	requests.get('http://localhost:8000/aulaAdd/1/')

def aula_remove():
	requests.get('http://localhost:8000/aulaRemove/1/')

def aula_estado(st):
	if st==0:
		requests.get('http://localhost:8000/aulaVerde/1/')
	elif st==1:
		requests.get('http://localhost:8000/aulaAmarillo/1/')
	elif st==2:
		requests.get('http://localhost:8000/aulaRojo/1/')

#Main Program

while True:
	check()
	update()
#	time.sleep(1)
