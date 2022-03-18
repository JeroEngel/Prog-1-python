gasto = float(input("Ingresar gasto:\n"))
costo = float(input("Dinero recibido:\n"))
vuelto = costo - gasto
centavos = (vuelto - int(vuelto))*100

print("\nVuelto\n")
print("Pesos :\n" + str(vuelto))
print("Centavos :\n" + str(centavos))