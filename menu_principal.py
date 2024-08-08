
def menu():
      
    #Menu para escolher tipo de usuário da Escolha
      print("########### 'Escola Moderna' ##########")
      print("Você deseja entrar como?")
      print(""" 1 - Aluno:
          \n 2 - Diretor
          \n 3 - Professor
          \n 4 - Sair """)   
      print("####################################")
      global opcao
      opcao = input()
      return opcao

def menu_aluno():
 while True:
                  
      print('###### Seja Bem vindo a Escola Moderna! #######')
      print("""O que você deseja fazer?
      \n  1- Consultar Boletim Escolar
      \n 2- Atualizar informações
      \n 3- Sair
            """)
      if opcao == '1':
            print('Consultando boletim...')
      elif opcao == '2':
            print('Atualizando Informações...')
      elif opcao == '3':
            print('Saindo...')
            break
      else:
           print(' Digite um valor válido ')


def menu_professor():
     print('####### Seja Bem vindo a Escolha Moderna #######')
     print("""O que você deseja fazer?
           \n 1- Consultar notas de alunos
           \n 2- Mudar notas
           \n 3- Adicionar nota
           \n 4- Deletar notas
           
           \n 5- Sair


      
           



     