salario_bruto = float(input())
horas_de_trabalho = float(input())

hora_bruta = salario_bruto / horas_de_trabalho
IR=0.11*salario_bruto
INSS = 0.08*salario_bruto
sind = 0.05*salario_bruto
salario_liq = salario_bruto - IR - INSS - sind
hora_liq = salario_liq/horas_de_trabalho

print('Salário Bruto = {:.2f}'.format(salario_bruto))
print('Hora Bruta = {:.2f}' .format(hora_bruta))
print('Desconto IR = {:.2f}' .format(IR))
print('Desconto INSS = {:.2f}' .format(INSS))
print('Desconto Sindicato = {:.2f}' .format(sind))
print('Salário Líquido = {:.2f}'.format(salario_liq))
print('Hora Líquida = {:.2f}'.format(hora_liq))
