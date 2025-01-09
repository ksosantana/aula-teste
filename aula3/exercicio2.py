AnoNascimento = int(input("informe seu ano de nascimento :"))

AnoAtual = 2025
idade = AnoAtual - AnoNascimento
# tempoAlistamento = idade >= 18 if,  idade > 18 else 18
if AnoNascimento >= 18:
    sub =  idade - 18
    print(f"ja se passaram {sub} anos do alistamento ")
else:
    sub = idade - 18
    print(f"ainda falta {soma} anos para se alistar")