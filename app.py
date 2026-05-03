preco_social = 120.00
preco_noiva = 350.00
preco_artistica = 200.00
preco_aula = 180.00

taxa_domicilio = 30.00
desconto_manha = 0.10

# LAÇO PRINCIPAL DO PROGRAMA
while True:

    print("=============AGENDAMENTO DE MAQUIAGEM=============") 

    # Laço para validação do Nome
    while True:
        nome = input("Digite seu nome: ").strip()
        if nome != "":
            break
        print("Erro: Nome inválido! Por favor, digite um nome.")


    print("")
    print("Servicos disponiveis:")
    print("1 - Maquiagem Social             R$ 120.00")
    print("2 - Maquiagem para Noiva         R$ 350.00")
    print("3 - Maquiagem Artistica          R$ 200.00")
    print("4 - Aula de Maquiagem Individual R$ 180.00")

    # Inicializamos a variável com um valor que obriga a entrada no laço
    opcao = 0
    # ATENÇÃO: fazer correção, ao escolher letra na opção de número e vice versa, o código é encerrado (crashado)
    # O laço continuará repetindo ENQUANTO a opção for menor que 1 OU maior que 4
    while opcao < 1 or opcao > 4:
        opcao = int(input("Escolha o numero do servico (1 a 4): "))
        
        if opcao < 1 or opcao > 4:
            print("Opcao invalida! Tente novamente.")

    # Inicializamos a variável vazia para entrar no laço
    resposta_domicilio = ""

    # O laço repete enquanto a resposta não for 's' E não for 'n'
    while resposta_domicilio != "s" and resposta_domicilio != "n":
        resposta_domicilio = input("Atendimento em domicilio? (s/n): ").lower().strip()
        
        if resposta_domicilio != "s" and resposta_domicilio != "n":
            print("Opcao invalida! Digite apenas 's' ou 'n'.")

    # O programa só chega aqui quando o usuário digita 's' ou 'n'

    print("Turnos disponiveis:")
    print("1 - Manha (10% de desconto)")
    print("2 - Tarde")
    #turno = int(input("Escolha o turno: "))

    # Inicializamos com 0 para garantir a entrada no laço
    turno = 0

    while turno != 1 and turno != 2:
        turno = int(input("Escolha o turno (1 - Manha / 2 - Tarde): "))
        
        if turno != 1 and turno != 2:
            print("Turno invalido! Escolha 1 ou 2.")

    # O programa continua normalmente após a validação


    if resposta_domicilio == "s":
        em_domicilio = True
    else:
        em_domicilio = False


    if turno == 1:
        horario_promocional = True
    else:
        horario_promocional = False


    match opcao:#entrada da condicional match case
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

    # PERGUNTA PARA REPETIR O PROGRAMA TODO
    continuar = ""
    while continuar != "s" and continuar != "n":
        continuar = input("\nDeseja fazer mais um agendamento? (s/n): ").lower().strip()
        if continuar != "s" and continuar != "n":
            print("Opção inválida! Digite 's' para sim ou 'n' para não.")
    
    if continuar == "n":
        print("\nEncerrando o sistema. Até logo!")
        break # Sai do laço principal e encerra o programa