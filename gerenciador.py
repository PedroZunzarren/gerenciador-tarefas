tarefas = []

def exibir_titulo():
    print('*' * 25)
    print('Gerenciador de tarefas')
    print('*' * 25)


def executar_gerenciador():
    exibir_titulo()
    
    while True:

        opcao_escolhida = mostrar_menu()
        
        if opcao_escolhida == 1:
            cadastrar_tarefa()
        elif opcao_escolhida == 2:
            listar_tarefas()
        elif opcao_escolhida == 3:
            mudar_status()
        elif opcao_escolhida == 4:
            excluir_tarefa()
        elif opcao_escolhida == 5:
            print('Encerrando programa...') 
            break
        else:
            print('Opção inválida')



def mostrar_menu():

    print('\n1. Cadastrar Tarefa')
    print('2. Listar tatefas')
    print('3. Mudar Status da Tarefa')
    print('4. Excluir Tarefa')
    print('5. Sair')
    
    try:
        opcao_escolhida = int(input('Digite um número: '))
        return opcao_escolhida
    except ValueError:
        return 0

def cadastrar_tarefa():
    
    print('oi')

if __name__ == '__main__':
    executar_gerenciador()
