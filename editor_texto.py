import os
lista_de_texto=[]


def menu():
    print(f'\n---- Menu de Opções ----')
    print(' 1. Adicionar Texto')
    print(' 2. Listar Textos')
    print(' 3. Contar Vogais')
    print(' 4. Deletar Texto')
    print(' 5. Encontrar Textos Por Tamanho')
    print(' 6. Verificar Letra no Texto')
    print(' 7. Modificar Texto')
    print(' 8. Sair')
    print('---------------------------')
def adicionar_texto(lista_de_texto):
    adicionar = str(input('digite o texto a ser adicionado: '))
    lista_de_texto.append(adicionar)
    
    print(f'\n--- Texto Adicionado ---')
    
    
def listar_textos(lista_de_texto):
    contador = 1
    if not lista_de_texto:
        print('-----------------------------')
        print('Erro: Não há texto adicionado')
        print('-----------------------------')
    else:
        for x in lista_de_texto:
            print('-----------------')
            print(f'{contador}. {x}')
            print('-----------------')
            contador +=1    

def remover_tarefa(lista_de_texto):
        listar_textos(lista_de_texto)
        if not lista_de_texto:
            print('-------------------------')
            print('Nenhuma Tarefa Adicionada')
            print('-------------------------')
        else:
            try:
                tarefa_remover = int(input('digite o indice a ser removido: '))
                if tarefa_remover < 1 and tarefa_remover < len(lista_de_texto):
                    print('Erro: Tarefa Invalida')
                else:
                    lista_de_texto.pop(tarefa_remover-1)
                    print('-------------------------------')
                    print(f'Elemento removido com sucesso')
                    print('-------------------------------')
            except IndexError:
                print('-------------------------------------------')
                print('Error: Indice Inexistente, Tente Novamente')
                print('-------------------------------------------')

    
def contar_vogais(lista_de_texto):
    vogais='aeiouAEIOU'
    quantidade_total = 0
    texto_vogal = int(input('Digite o Indice a se contar as vogais: '))
    if lista_de_texto[texto_vogal-1]:
        for texto in lista_de_texto[texto_vogal-1]:
            for caractere in texto:
                if caractere in vogais:
                    quantidade_total +=1
    print('-----------------------------------------------------------------------')
    print(f'As vogais aparecem {quantidade_total} de vezes no {texto_vogal}º texto')
    print('-----------------------------------------------------------------------')
    
def encontrar_tamanho(lista_de_texto):
    if not lista_de_texto:
        print('---------------------------------')
        print('Erro: Nenhum Texto foi Adicionado')
        print('---------------------------------')
        return
    try:
        tamanho = int(input('Digite o Tamanho do Texto a ser Encontrado: '))
    except ValueError:
        print('------------------------------------')
        print('Erro: O Número Digitado não é Valido')
        print('------------------------------------')
        return
    
    textos_encontrado=[]
    for texto in lista_de_texto:
        if len(texto) == tamanho:
            textos_encontrado.append(texto)
            
    if textos_encontrado:
        print('---------------------------------------------------------')
        print(f'\n--- Textos com {tamanho} caracteres de comprimento ---')
        print('---------------------------------------------------------')
        for i, texto in enumerate(textos_encontrado):
            print('---------------------------------------------')
            print(f'{i+1}. "{texto}" (Comprimento: {len(texto)})')
            print('---------------------------------------------')
        
    else:
        print('---------------------------------')
        print('Erro: Nenhum Texto Foi Encontrado')
        print('---------------------------------')
        
        
def verificar_letra(lista_de_texto):
    if not lista_de_texto:
        print('---------------------------------')
        print('Erro: Nenhum Texto foi Adicionado')
        print('---------------------------------')
        return
    
    while True:
        letra = input('Digite Apenas Uma Letra: ')
        if len(letra) == 1 and letra.isalpha:
            break
        else:
            print('-----------------------------------------------')
            print('Erro: Entrada Inválida, Digite apenas Uma Letra')
            print('-----------------------------------------------')
    
    quantidade_total = 0
    
    
    for texto in lista_de_texto:
        for caractere_do_texto in texto:
            if caractere_do_texto == letra.lower():
                quantidade_total+=1
                
            
        if quantidade_total >= 1:
            print('------------------------------------------------------------')
            print(f'A letra {letra} foi encontrada {quantidade_total} de vezes.')
            print('------------------------------------------------------------')
        else:
            print('----------------------------------------------------')
            print(f'A letra {letra} não foi encontrada, tente novamente')
            print('----------------------------------------------------')
            
def editar_texto(lista_de_texto):
    if not lista_de_texto:
        print('---------------------------------')
        print('Erro: Nenhum Texto foi Adicionado')
        print('---------------------------------')
        return
    
    while True:
        listar_textos(lista_de_texto)
        remover = int(input('Digite o Indice a ser Modificado: '))
        if remover < 1 and remover > len(lista_de_texto):
            print('Erro: Número Inválido')
        else: 
            lista_de_texto.pop(remover-1)
            novo_texto = str(input('Digite a nova palavra: '))
            lista_de_texto.append(novo_texto)
            print('--- Palavra Modificada ---')
            listar_textos(lista_de_texto)
        break   
        
    
def main():
    while True:
        menu()
        try:
             opção = int(input('Digite o que deseja fazer: '))
        except ValueError:
            print('----------------------------------')
            print('Entrada inválida, digite um número')
            print('----------------------------------')
            continue
        os.system('cls')
    
        if opção == 1:
            adicionar_texto(lista_de_texto)
        elif opção == 2:
            listar_textos(lista_de_texto)
        elif opção == 3:
            contar_vogais(lista_de_texto)
        elif opção == 4:
            remover_tarefa(lista_de_texto)
        elif opção == 5:
            encontrar_tamanho(lista_de_texto)
        elif opção == 6:
            verificar_letra(lista_de_texto)
        elif opção == 7:
            editar_texto(lista_de_texto)
        elif opção == 8:
            print('-----------------------')
            print('Até Logo, Volte Sempre')
            print('-----------------------')
            break
        else:
            print('Erro: Valor Digitado Inválido')
            
main()