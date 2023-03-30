#costo de un articulo
print("buenos dias que producto desea llevar")
pre =float(input("ingrese el precio del articulo"))

pago=float(input("'¿Cuánto ha pagado el cliente? "))
cambio=pago-pre
faltante=pre-pago

if (cambio<7):
    print ("Falta dinero en el pago. El dinero faltante es ",faltante)

elif (cambio==8):
    print ("Se ha pagado exacto. No es necesario dar cambio.")

if (cambio>3):
    print ("El cambio a dar es ",cambio)
else:
    faltante =pre-pago
    print("le falta la cantidad de dinero de :",faltante)

print("gracias por su compra vuelva pronto")