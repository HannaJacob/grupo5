'''
==========================================================================================================

Projeto em Grupo - Módulo 1 - Senac & Resilia Educação - 27 de Setembro de 2023

Grupo 5 - Faculdade do Senac (Cinelândia)

Integrantes do grupo:   Arthur Lorran     -   Co-Facilitador
                        Ederson Macedo    -   Gestor de Conhecimento
                        Hanna Jacob       -   Gestora de Pessoas
                        Fernando Barbosa  -   Colaborador

==========================================================================================================  
DESCRIÇÃO DAS FUNÇÕES:
                        
Arthur Lorran: Pessoa responsável pela verificação das tarefas e visão crítica do que está sendo feito.

Ederson Macedo: Pessoa responsável em certificar que todos estão compreendendo o que está sendo feito
                e coletar a opinião de todos.

Hanna Jacop: Pessoa responsável pela interação do grupo e garantia de que todos os integrantes
             estão se entendendo (gestão de pessoal).

Fernando Barbosa: Pessoa responsável pelo acompanhamento das tarefas que foram solicitadas, a fim de
                  prestar assistência à execução delas.

===========================================================================================================
O TRABALHO NA PRÁTICA:

Detalhamento:  Todos os integrantes do grupo atuaram na confecção do trabalho. Cada um em sua
               função. O Ederson Macedo ficou responsável pela digitalização do código e certificar-se
               que todos estavam compreendendo e  se dispondo a tirar dúvidas sobre o código, já o
               Arthur Lorran ficou responsável pelo olhar crítico para o melhoramento do código,
               bem como garantir que todos estavam exercendo corretamente suas funções no tabalho, 
               enquanto a Hanna ficou responsável em certificar-se que todos os membros do grupo
               estavam de acordo com o que estava sendo feito e auxiliando na elaboração do código,
               e o Fernando Barbosa auxiliou na digitalização do código e assistiu em opiniões, 
               além de colocar-se a disposição para execuções de tarefas ao decorrer do trabalho.

=============================================================================================         
PROPOSTA DO TRABALHO:

======================    Atendimento virtual de uma hamburgueria    ======================

Iniciar um atendimento ao cliente para que ele possa fazer o seu pedido.
Durante o atendimento ele terá 3 opções de pedidos: Hambuguers, Bebidas e Acompanhamentos, onde
para cada pedido, ele dirá se gostaria de continuar pedindo ou se passará para a próxima opção.
Ao final do pedido, retornará: nome, endereço, tempo de entrega, itens e o total do pedido.

==============================================================================================
'''

bem_vindo = "OLÁ, SEJA BEM VINDO AO NOSSO TRABALHO. O CÓDIGO COMEÇA AQUI! ESPERO QUE GOSTE!!!"

#SUBPROGRAMA

#Definindo função para inicialização do pedido
def escolha_opcoes(opcoes):

#Definindo variáveis que ajudaram na manipulação do looping
    pedido = []
    valortotal = []
    pedindo = True
    total = 0
    escolha = 0

#Imprime a lista de opções para um pedido.
    for i in range(len(opcoes)):
        print(opcoes[i][0],"\n")

#A intenção desse looping é que o cliente possa fazer mais de 1 pedido, caso ele deseja.
#Por isso, perguntamos se ele deseja continuar pedindo ou não. Utilizamos True ou False
#Como continuidade ou trava do looping. Preferimos não usar o break.
    while pedindo:
        escolha = int(input("\n Escolha a opção que melhor te agrade: "))
        if escolha != opcoes[-1][2]:
            pedido.append(opcoes[escolha-1][0])
            total += opcoes[escolha-1][1]
            pergunta = int(input("\nDeseja continuar pedindo ? \nDigite (1) para SIM ou (2) para NAO: "))
            if pergunta == 1:
                pedindo = True
            else:
                pedindo = False
        else:
            pedindo = False
#Essa função retorna o pedido e, para nos facilitar, utilizei o TOTAL na posição[-1] para
#Ficar mais facil de acessar. Poderá verificar isto no código principal, quando declararei
#Uma variável chamada SOMA
    pedido.append(total)
    return pedido

#Estamos declarando o cardápio da hamburgueria. 
# [Alimento, preço, número correspondente à opção do cliente]
hamburguers = [
    ["1 - CreatBurguer - R$7,00 \n(pão, carne, ovo, queijo)", 7.00, 1], 
    ["2 - CreatCheddar - R$9,00 \n(pão, carne, ovo, cheddar)", 9.00, 2], 
    ["3 - CreatBrasil - R$10,00 \n(pão, carne, queijo, salada, maionese, ovo, presunto, batata palha)", 10.00, 3], 
    ["4 - CreatBancon - R$13,00 \n(pão, carne, queijo, bancon, barbecue)", 13.00, 4], 
    ["5 - CreatChicken Salada - R$16,00 \n(pão gergelim, frango, queijo, salada de alho poro, molho tartaro, batata palha)", 16.00, 5], 
    ["6 - CreatBlack - R$26,00 \n(pão australiano, costela bovina, cebola caramelizada, cheddar, barbecue)", 26.00, 6], 
    ["7 - CreatRoom - R$28,00 \n(pão brioche, picanha, cheddar,barbecue, anéis de cebola, bacon)", 28.00, 7], 
    ["8 - CreatSurprise - R$30,00 \n(pão de abóbora, carne seca, queijo coalho, anéis de cebola)", 30.00, 8], 
    ["9 - CreatMaster - R$32,50 \n(pão brioche, costela bovina, picanha ,queijo empanado, bacon, barbecue)", 32.50, 9], 
    ["10 - CreatFULL - R$24,00 \n(pão gergelim, carne, frango, calabresa, bacon, barbecue, salada, ovo, anéis de cebola)", 24.00, 10],["11 - Não desejo pedir mais hamburguer", 0.00, 11]
]
bebidas = [
    ["1 - Coca-Cola 400ml - R$6,00", 6.00, 1], 
    ["2 - Sprite 400ml - R$5,00", 5.00, 2], 
    ["3 - Fanta 400ml (uva, guaraná, laranja) - R$4,00", 4.00, 3], 
    ["4 - Pepsi 400ml - R$5,00", 5.00, 4], 
    ["5 - Guaraná Jesus 400ml - R$6,00", 6.00, 5], 
    ["6 - Guaraná Antarctica 400ml - R$6,00", 6.00, 6], 
    ["7 - Coca-Cola 2l - R$10,00", 10.00, 7], 
    ["8 - Fanta (uva, guaraná, laranja) 2l - R$8,00", 8.00, 8], 
    ["9 - Pesi 2l - R$8,00", 8.00, 9], 
    ["10 - Guaraná Antarctica 2l - R$9,00", 9.00, 10], 
    ["11 - Laranjada - R$5,00", 5.00, 11], 
    ["12 - Limonada Suiça - R$6,50", 6.50, 12], 
    ["13 - Acerola - R$6,00", 6.00, 13], 
    ["14 - Abacaxi com hortelã - R$8,00", 8.00, 14], 
    ["15 - Manga - R$6,00", 6.00, 15], 
    ["16 - Laranja com Acerola - R$6,50", 6.50, 16], 
    ["17 - Laranja com Limão - R$6,50", 6.50, 17], 
    ["18 - Abacaxi sem hortelã - R$6,80", 6.80, 18], 
    ["19 - Sem bebida", 0, 19]
]
acompanha = [
    ["1 - Batata P - R$6,00", 6.00, 1], 
    ["2 - Batata M - R$8,00", 8.00, 2], 
    ["3 - Batata G - R$10,00", 10.00, 3], 
    ["4 - Batata Turbinada P - R$10,00", 10.00, 4], 
    ["5 - Batata Turbinada M - R$15,00", 15.00, 5], 
    ["6 - Batata Turbinada G - R$18,00", 18.00, 6],
    ["7 - Sem acompanhamentos", 0, 7]
]

#PROGRAMA PRINCIPAL - Aqui usaremos a função denfinida acima para cada tipo de pedido.
print("\nSeja bem vindo(a) à Hamburgueria *** Creativity & Flavor ***\n")

#Aqui, estamos verificando a distância do cliente até nossa loja e criando variáveis para me ajudar.
#Elas vão me ajudar a declarar o total do pedido (soma), o tempo de entrega e o pedido em si.
localCliente = float(input("\nSua residência se encontra à quantos KM de uma de nossas loja? \n Caso você esteja em nossa loja, basta digitar o número zero 0: "))
tempo = []
soma = 0
pedidototal = []

#Se o cliente mora próximo, iremos atendê-lo. Primeiro, colata-se as informações para estimar
#O tempo de entrega de seu pedido.
if localCliente <= 10:
    infoCliente = input("\nPor favor, digite o seu nome e seu endereço. \n(Exemplo: Getúlio Vargas, Avenida Presidente Vargas, 435): ")
    if localCliente <= 4:
            tempo.append("20 minutos")
    elif localCliente <= 6:
            tempo.append("25 minutos")
    elif localCliente <= 8:
            tempo.append("30 minutos")
    elif localCliente <= 10:
        tempo.append("40 minutos")

#Nessa parte do código, estamos anotando o pedido do cliente em uma lista, utilizando a função criada.
    pedidototal.append(escolha_opcoes(hamburguers))
    pedidototal.append(escolha_opcoes(bebidas))
    pedidototal.append(escolha_opcoes(acompanha))

#Agora, estamos imprimindo o seu pedido com suas informações (nome, endereço, pedidos, total, tempo).
    for i in range(len(pedidototal)):
         soma += pedidototal[i][-1]
    print("----------------------------------------------------------------\n")
    print(infoCliente, "\n")

#Esse looping for, foi feito para que todos os elementos da lista sejam imprimidos, exceto o último.
    for lista in pedidototal:
         for elemento in lista[:-1]:
              print(elemento,"\n")

#Retornando o tempo estimado e o tempo de entrega.
    print("\n","Pedido finalizado com sucesso!\nO tempo estimado para entrega é de: ", tempo[0],"\n")
    print("O total do pedido foi de: R$"+str(soma)+" reais")
    print("---------------------------------------------------------------")
    print("\n", "Ficamos muitos felizes por você ter nos escolhido! Volte sempre!")

#Pesquisa de satisfação e dúvidas do cliente.
    atendimentoFinal = int(input("\nSeleciona um das opções a seguir:\n1 - Feedback\n2 - Reclamação\n3 - Dúvidas\n4 - Instituição\n5 - Finalizar Atendimento\nR: "))
    if atendimentoFinal == 1:
         atendimentoFinal = input("Por favor, descreva aqui a sua experiência: ")
         print("\nMuito obrigado pelo seu feedback! Sua opinião é muito bem vinda e certamente estamos em melhoria contínua!!!")
    elif atendimentoFinal == 2:
         atendimentoFinal = int(input("\n1 - Pedido errado\n2 - Atraso na entrega\n3 - Mal atendimento\nR: "))
         if atendimentoFinal == 1:
              respota = input("Pedimos desculpas pelo transtorno. Iremos enviar o seu pedido o mais rapido possível. Você aceita ? S ou N: ")
              if respota == "S":
                   print("Muito obrigado pela confiança! O seu pedido será entregue em, no máximo, 20 minutos.")
              else:
                   print("Tudo bem! Sem problemas! Estaremos fazendo o estorno de seu dinheiro.")
         elif atendimentoFinal == 2:
              respota = int(input("1 - O meu pedido chegou, mas atrasou\n2 - O meu pedido não chegou\nR: "))
              if respota == 1:
                   print("Pedimos desculpas pelo transtorno, iremos apurar o que pode ter acontecido e este problema será solucionado!")
              else:
                   respota = int(input("1 - Gostaria de receber meu pedido\n2 - Gostaria de receber o estorno\nR: "))
                   if respota == 1:
                        print("Muito obrigado pela confiança! O seu pedido será entregue em, no máximo, 20 minutos.")
                   else:
                        print("Tudo bem! Sem problemas! Estaremos fazendo o estorno de seu dinheiro.")
         elif atendimentoFinal == 3:
              print("Pedimos desculpas pelo mal atendimento. Iremos averiguar melhor a situação para que a sua experiência seja a melhor de todas!")
    elif atendimentoFinal == 3:
         respota = int(input("1 - Como o tempo de entrega é estimado?\n2 - O hamburguer é artesanal ?\n3 - Horário de funcionamento\nR: "))
         if respota == 1:
              print("\nO tempo é estimado com base na distância entre a sua residência e nossa loja.")
         elif respota == 2:
              print("\nTemos opções de hamburgueres artesanais e não artesanais. Os artesanais estão contidos da opção 5 até a 10")
         else:
              print("Funcionamos de quarta à domingo, de 18h até 00h")
    elif atendimentoFinal == 4:
         respota = int(input("1 - Qual a nossa missão?\n2 - Nossos valores\n3 - Carreiras (trabalhe conosco)\nR: "))
         if respota == 1:
              print("\nEntregar sabor e criatividade ao paladares de nossos clientes. Queremos ser diferentes e fazer isso com atitude, criando cardápios irreverentes, ousados e, sobretudo, lhe dar uma excelente experiência. Sermos marcantes!!!")
         elif respota == 2:
              print("Acreditamos que todos nós temos um sonho e a nossa preocupação é sobre 'De que maneira estamos agindo para alcançar esse sonho?' Acreditamos que a humildade, confiança e o comprometimento, além da visão estratégica são excelentes valores para nós e sempre nos preocupamos em estar a disposição de nossos clientes. Vocês são os melhores!")
         else:
              print("Basta pesquisar por: Creativity & Flavor , vá em TRABLHE CONOSCO e deixe seu currículo em nosso banco de dados!\nFicaremos felizes em saber do seu interesse para conosco!!!")
    else:
         print()
#Caso o cliente more num lugar longe (acima de 10km), não conseguiremos atendê-lo
else:
     print("Infelizmente não atendemos o seu local, mas ficaremos felizes em ter receber em uma de nossas lojas!")
