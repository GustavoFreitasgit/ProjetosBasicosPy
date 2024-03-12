print("======================================================X BEM VINDO A CALCULADORA DO GUSTAVO X=========================================================================")
print ("SELECIONE A TIPO DA OPERAÇÃO (+, -, x, /)")
tipo = input("Qual O tipo de operação? ")
op = tipo
if op == "+" : num1 = int(input("Primeiro valor: ")) ; num2 = int(input("Segundo valor: ")) ; R = num1+num2 ;  print(f"O Valor da operação é de: {R}")
if tipo == "-" : num3 = int(input("Primeiro valor: ")) ; num4 = int(input("Segundo valor: ")) ; R = num3-num4 ;  print(f"O Valor da operação é de: {R}")
if tipo == "x" : num5 = int(input("Primeiro valor: ")) ; num6 = int(input("Segundo valor: ")) ; F = num5*num6 ;  print(f"O Valor da operação é de: {F}")
if tipo == "/" : num7 = int(input("Primeiro valor: ")) ; num8 = int(input("Segundo valor: ")) ; R = num7/num8 ;  print(f"O Valor da operação é de: {R}")