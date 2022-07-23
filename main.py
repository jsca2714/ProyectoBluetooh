from gpiozero import LED,Motor
from bluedot.btcomm import BluetoothServer
from signal import pause
from time import sleep


motor = Motor(forward=26, backward=19)
velocidad=0.6
direccion=1

global cadena




def leer(data):
	global dato
	global velocidad
	dato=data.strip()
	l=len(dato)
	print(dato+" "+str(l))
	if dato=="$":
		print("Giro Derecha")
		motor.backward(velocidad)
	elif dato=="°":
		print("Giro Izquierda")
		motor.forward(velocidad)
	elif dato=="#":
		print("STOP")
		motor.stop()
	else:
		Desemp(dato)

def Desemp(dato):
		global Str_value 
		print("secuencia")
		string1= ''.join( x for x in dato if x not in car1)
		print(string1)
		Str_value=string1.strip('""')
		l2=len(Str_value)
		print(Str_value)
		print(l2)
		Trama(dato,velocidad)
		VerifTram(Str_value)
		
def VerifTram(Str_value):
	global velocidad
	global direccion
	chararray=list(Str_value)
	lc=len(chararray)
	print(lc)
	print(""+str(chararray))
	lista1=[]
	lista2=[]
	lista3=[]
	lista4=[]
	lista5=[]
	flag=0
	cont=0
	count=0
	pcc=0
	cont1=0
	a=''
	cont2=0
	cont3=0
	cont4=0
	cont_1=0
	cont_2=0
	cont_3=0
	cont_4=0
	contc=0
	for pc in range ( lc ):
		print ( Str_value[pc])
		b=Str_value[pc].isalpha()
		print(b)
		if b==1:
				lista1.clear()
				lista2.clear()
				lista3.clear()
				lista4.clear()	
				contc=0
				if Str_value[pc]=='S' or Str_value[pc]=='D' or Str_value[pc]=='I' or Str_value[pc]=='V':
					if Str_value[pc]=='S':
						print("S")
						flag=1
						cont1+=1
					elif Str_value[pc]=='D':
							print("I")
							flag=2
							cont2+=1
					elif Str_value[pc]=='I':
						print("D")
						flag=3
						cont3+=1
					elif Str_value[pc]=='V':
						print("V")
						flag=4
						cont4+=1
				else:
					print("error de trama")
					break
		if b==0:
			contc+=1
			#print("el valor de contc es"+str(contc))
			if flag==1:
				lista1.append(Str_value[pc])
				#print("largo de la lista"+str(len(lista1)))
				StrA = "".join(lista1)
				#print(StrA)
				#if StrA=='':
				#	print("error de trama1")
				#	break
				if contc==len(lista1):
					motor.stop()
					sleep(int(StrA))
					cont_1+=1
			if flag==2:
				lista2.append(Str_value[pc])
				StrB = "".join(lista2)
				#if StrB=='':
				#	print("error de trama2")
				#	break
				direccion=1
				motor.forward(velocidad)
				sleep(int(StrB))
				motor.stop()
				cont_2+=1
			if flag==3:
				lista3.append(Str_value[pc])
				StrC = "".join(lista3)
				#if StrC=='':
				#	print("error de trama3")
				#	break
				cont_3+=1
				direccion=2
				motor.backward(velocidad)
				sleep(int(StrC))
				motor.stop()
			if flag==4:
				lista4.append(Str_value[pc])
				StrD= "".join(lista4)
				#if StrD=='':
				#	print("error de trama4")
				#	break
				cont_4+=1
				velocidad=int(StrD)*0.01
				sleep(0.1)

		else:
			pass
		motor.stop()

	if cont1>cont_1:
		print("error de trama1")
	if cont2>cont_2:
		print("error de trama2")
	if cont3>cont_3:
		print("error de trama3")
	if cont4>cont_4:
		print("error de trama4")
    
	print(""+str(lista1))
	print(""+str(lista2))
	print(""+str(lista3))
	print(""+str(lista4))
	StrA = "".join(lista1)
	print(StrA)
	StrB = "".join(lista2)
	print(StrB)
	StrC = "".join(lista3)
	print(StrC)
	StrD = "".join(lista4)
	print(StrD)
	lista5.append(StrA)
	lista5.append(StrB)
	lista5.append(StrC)
	lista5.append(StrD)
	print(""+str(lista5))
	a=sorted(lista5)
	print(a)
