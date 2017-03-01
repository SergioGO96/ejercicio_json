import json	

with open('contratos-menores-2014.json') as data_file:
	data = json.load(data_file)

contador=0

#Programa que lista todos los contratos.
print "Los contratos guardados son los siguientes: "
for a in data:
	print a["objeto"]
	contador = contador + 1
	print

#Programa que cuenta todos los constratos.
print "Hay", contador, "contratos registrados."

#Introducir un precio maximo y un precio minimos, y monstrar los contratos entre esos valores.
valormax = float(raw_input("Introduce un precio de contrato maximo: "))
valormin = float(raw_input("Introduce un precio de contrato minimo: "))

precio = False
for e in data:
	if float(e["Precio"])< valormax and float(e["Precio"])> valormin:
		print e["objeto"], "tiene un precio de", e["Precio"]
		precio = True
if precio == False:
	print "No hay ningun contrato entre esos valores"

#Introducir por teclado un tipo de contrato, y mostrar toda la informacion del contrato.

contrato = raw_input("Introduce un tipo de contrato: ")

for i in data:
	if contrato.lower() == i["TipoContrato"].lower():
		print "Numero expediente:", i["idexpediente"]
		print "Nombre del contrato:", i["objeto"]
		print "Contratado:", i["Nombre"]
		print "Precio:", i["Precio"]
		print "Tipo:", i["TipoContrato"]

# Mostrar por pantalla el precio medio por persona de todos sus contratos.
contratados = []
for l in data:
	contratados.append(l["Nombre"])

contratadosbien = set(contratados)
salarios = 0
cont = 0
for x in contratadosbien:
	for z in data:
		if x == z["Nombre"]:
			salarios = salarios + float(z["Precio"])
			cont = cont + 1
	print x, "tiene un gasto medio de ", salarios/cont 
	print 
	


