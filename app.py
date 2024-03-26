import os

restaurantes = [{'nome':'Papas hamburgueria', 'categoria':'americana', 'ativo': False},
                {'nome':'Papas Pizzaria', 'categoria':'Italiana','ativo': True},
                {'nome':'Papas Sushi', 'categoria':'Japonesa','ativo': False}]

def iniciar():
    print('Prática CRUD\n')

def opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def sair():
    subTi('Você saiu! \n')

def voltar():
    input('Digite uma tecla para voltar para o Menu inicial! ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar()

def subTi(texto):
    os.system('cls')
    print(texto)

def cadastro():
    subTi('Cadastro de novos Restaurantes: \n')
    nomeR = input(f'Nomeie o Restaurante: \n')
    cat = input(f'Digite a Categoria do Restaurante: \n')
    dadosR = {'nome':nomeR, 'categoria':cat,'ativo':False}
    restaurantes.append(dadosR)
    
    print(f'Cadastro do restaurante: {nomeR} feito! ')
    voltar()

def listar():
    subTi('Lista de Restaurantes: \n')
    for restaurante in restaurantes:
        nomeR = restaurante['nome']
        cat = restaurante['categoria']
        ativ = restaurante['ativo']

        print(f'- {nomeR} | {cat} | {ativ}')
    voltar()

def ativar():
    subTi('Ativando o Restaurante:')
    rest = input('Digite o nome do restaurante que deseja mudar: \n')
    restAtivo = False
    for restaurante in restaurantes:
        if rest == restaurante['nome']:
            restAtivo = True
            restaurante['ativo'] = not restaurante['ativo']
            aviso = f'O restaurante {rest} foi ativado com sucesso' if restaurante['ativo'] else f'O Restaurante foi desativado com sucesso'
            print(aviso)
    if not rest:
        print('Restaurante não encontrado')
    voltar()

def escolha():
    try:
        a = int(input('Escolha uma opção: '))

        if a == 1:
           cadastro()
        elif a == 2:
            listar()
        elif a == 3:
            ativar()
        elif a == 4:
            sair()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main(): 
    os.system('cls')
    iniciar()
    opcoes()
    escolha()

if __name__ == '__main__':
    main()

#Nome vazio " " e restaurante já existente!