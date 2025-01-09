diasAlugados = int(input("informe por quantos dias o carro foi alugado :"))
kmPercorrido = float(input("informe quantos km o veiculo percorreu :"))
 
valorDia = diasAlugados * 90
valorKm = kmPercorrido * 0.20

total = valorDia + valorKm
print("O valor total a ser pago é :", total,"R$")