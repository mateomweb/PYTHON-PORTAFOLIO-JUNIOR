print(" CAJERO AUTOMATICO ")

saldo_inicial = 1000000

retiro_usuario=int(input("ingrese el retiro deseado: "))

if retiro_usuario<=saldo_inicial:
    print("RETIRO EXITOSO")
    total=saldo_inicial-retiro_usuario
    print(f"lo que procedio a retirar fue de: {retiro_usuario}")
    print(f"lo que le sobra de saldo es de: {total}")

else:
    print("retiro fallido, saldo insuficiente")
