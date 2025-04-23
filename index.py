##Trabalho de Python (Aprendizado de Máquina)- Professor: Marcelo Paiva
#Alunos: 
##  Julya Alfaiate - 2314290064
##  Yan Nogueira - 2314290122
##  Eduardo Castro - 


valor_investido = float(input("Digite o valor a ser investido (R$): "))
dias_aplicado = int(input("Digite por quantos dias o dinheiro ficará investido: "))


taxa_anual = 0.1415
taxa_dia = (1 + taxa_anual) ** (1 / 365) - 1

valor_final_bruto = valor_investido * ((1 + taxa_dia) ** dias_aplicado)
rendimento_bruto = valor_final_bruto - valor_investido

if dias_aplicado < 30:
 
    tabela_iof = {
        1: 0.96, 2: 0.93, 3: 0.90, 4: 0.86, 5: 0.83,
        6: 0.80, 7: 0.76, 8: 0.73, 9: 0.70, 10: 0.66,
        11: 0.63, 12: 0.60, 13: 0.56, 14: 0.53, 15: 0.50,
        16: 0.46, 17: 0.43, 18: 0.40, 19: 0.36, 20: 0.33,
        21: 0.30, 22: 0.26, 23: 0.23, 24: 0.20, 25: 0.16,
        26: 0.13, 27: 0.10, 28: 0.06, 29: 0.03
    }
    iof_percentual = tabela_iof.get(dias_aplicado, 0.0)
    valor_iof = rendimento_bruto * iof_percentual
else:
    valor_iof = 0.0


rendimento_apos_iof = rendimento_bruto - valor_iof


if dias_aplicado <= 180:
    ir_percentual = 0.225
elif dias_aplicado <= 360:
    ir_percentual = 0.20
elif dias_aplicado <= 720:
    ir_percentual = 0.175
else:
    ir_percentual = 0.15

valor_ir = rendimento_apos_iof * ir_percentual


rendimento_liquido = rendimento_apos_iof - valor_ir
valor_total_final = valor_investido + rendimento_liquido


print("\n--- Resumo da aplicação ---")
print("Valor investido: R$ {:.2f}".format(valor_investido))
print("Rendimento bruto: R$ {:.2f}".format(rendimento_bruto))
print("Desconto IOF: R$ {:.2f}".format(valor_iof))
print("Desconto IR: R$ {:.2f}".format(valor_ir))
print("Valor final com rendimento líquido: R$ {:.2f}".format(valor_total_final))
