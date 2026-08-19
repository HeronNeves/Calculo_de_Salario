#Desafio01 14/08/26
import unicodedata

def remover_acentos(texto):
  return unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode("utf-8")
print(" CÁLCULO DE FOLHA DE PAGAMENTO ".center(46,"-"))

folha_pagamento = []
contador = 0
funcionarios = int(input("Digite o numero de funcionários a ser consultada: "))

while contador < funcionarios:

  nome = str(input("Digite o nome do Funcionário: "))
  salarioBase = float(input("Digite o salário base do funcionário: "))
  horasTrab = int(input("Digite a quantidade de horas que o funcionário trabalhou: "))
  faltas = int(input("Quantidade de faltas (não justificadas): "))
  planoSaude = (input("Funcionário aderiu ao plano de saúde? (sim/não): ")).lower().strip()
  resposta_plano = remover_acentos(planoSaude)
  salarioDia = salarioBase / 30
  salarioHora = salarioBase / 220
  extra = 0
  tetovt = 220


  if horasTrab > 220:
    extra = horasTrab - 220
  hora_extra = (extra * salarioHora) * 1.5
  desconto_faltas = faltas * salarioDia

  salarioBruto = salarioBase + hora_extra
  
  base_calculo_imposto = salarioBruto - desconto_faltas
  desconto_imposto = 0
  
  if base_calculo_imposto <= 1500:
    desconto_imposto =  base_calculo_imposto  * 0.075
  elif base_calculo_imposto > 1500 and base_calculo_imposto <= 3000:
    desconto_imposto =  base_calculo_imposto * 0.12
  elif base_calculo_imposto > 3000:
    desconto_imposto = base_calculo_imposto * 0.15

  descontovt = salarioBase * 0.06
  if descontovt > tetovt:
    descontovt = tetovt

  desconto_saude = 0
  if planoSaude == "sim":
    desconto_saude = 150

  salarioLiquido = salarioBruto - desconto_faltas - desconto_imposto - descontovt - desconto_saude

  print(f"O Salário Liquido desse funcionário é de: R$ {salarioLiquido:.2f}")  

  dados_funcionario = {
        "nome": nome,
        "bruto": salarioBruto,
        "extras": hora_extra,
        "faltas": desconto_faltas,
        "impostos": desconto_imposto,
        "vt": descontovt,
        "saude": desconto_saude,
        "liquido": salarioLiquido
    }
  folha_pagamento.append(dados_funcionario)

  contador += 1

print("="*46)
print(" RELATÓRIO FINAL DE FOLHA DE PAGAMENTO ".center(40, "="))
print("="*46)

for f in folha_pagamento:
    print(f"Funcionário: {f['nome']}")
    print(f"Salário Bruto:   R$ {f['bruto']:.2f}") 
    print(f"Extras:  R${f['extras']:.2f}")
    print(f"Desc. Faltas:    R$ {f['faltas']:.2f}")
    print(f"Vale Transporte: R$ {f['vt']:.2f}")
    print(f"Salário Liquido: R$ {f['liquido']:.2f}")
    print("-" * 46)

