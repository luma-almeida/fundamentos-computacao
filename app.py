preco_social = 120.00
preco_noiva = 350.00
preco_artistica = 200.00
preco_aula = 180.00

taxa_domicilio = 30.00
desconto_manha = 0.10


print("==================================================")
print("=============AGENDAMENTO DE MAQUIAGEM=============")
print("==================================================")


nome = input("Digite seu nome: ")

if nome == "":
    print("Nome invalido! Digite um nome.")
    print("Encerrando o programa.")
    exit()


print("")
print("Servicos disponiveis:")
print("1 - Maquiagem Social             R$ 120.00")
print("2 - Maquiagem para Noiva         R$ 350.00")
print("3 - Maquiagem Artistica          R$ 200.00")
print("4 - Aula de Maquiagem Individual R$ 180.00")

opcao = int(input("Escolha o numero do servico: "))

if opcao < 1 or opcao > 4:
    print("Opcao invalida! Escolha um numero de 1 a 4.")
    print("Encerrando o programa.")
    exit()


resposta_domicilio = input("Atendimento em domicilio? (s/n): ")

if resposta_domicilio != "s" and resposta_domicilio != "n":
    print("Opcao invalida! Digite apenas 's' ou 'n'.")
    print("Encerrando o programa.")
    exit()


print("")
print("Turnos disponiveis:")
print("1 - Manha (10% de desconto)")
print("2 - Tarde")
turno = int(input("Escolha o turno: "))

if turno != 1 and turno != 2:
    print("Turno invalido! Escolha 1 ou 2.")
    print("Encerrando o programa.")
    exit()


if resposta_domicilio == "s":
    em_domicilio = True
else:
    em_domicilio = False


if turno == 1:
    horario_promocional = True
else:
    horario_promocional = False


match opcao:
    case 1:
        nome_servico = "Maquiagem Social"
        preco_base = preco_social
    case 2:
        nome_servico = "Maquiagem para Noiva"
        preco_base = preco_noiva
    case 3:
        nome_servico = "Maquiagem Artistica"
        preco_base = preco_artistica
    case 4:
        nome_servico = "Aula de Maquiagem Individual"
        preco_base = preco_aula


if em_domicilio and horario_promocional:
    preco_com_taxa = preco_base + taxa_domicilio
    valor_desconto = preco_com_taxa * desconto_manha
    valor_total = preco_com_taxa - valor_desconto
elif em_domicilio:
    valor_total = preco_base + taxa_domicilio
elif horario_promocional:
    valor_desconto = preco_base * desconto_manha
    valor_total = preco_base - valor_desconto
else:
    valor_total = preco_base


print("")
print("--------------------------------------------------")
print("AGENDAMENTO CONFIRMADO!")
print("--------------------------------------------------")
print("Cliente:    " + nome)
print("Servico:    " + nome_servico)

if em_domicilio:
    print("Domicilio:  Sim (+ R$ 30.00)")
else:
    print("Domicilio:  Nao")

if horario_promocional:
    print("Turno:      Manha (10% de desconto)")
else:
    print("Turno:      Tarde")

print(f"Valor total: R$ {valor_total:.2f}")

print("--------------------------------------------------")
print("Obrigada pela preferencia, " + nome + "!")