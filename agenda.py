

class Contato:
    def __init__(self, id, nome, telefone, email):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
    def __repr__(self):
        return f"<Contato {self.nome}>"

class AgendaDeContatos:
    def __init__(self):
        self.contatos = {}
        self.proximo_id = 1
    def adicionar(self):
        nome = input('Nome: ')
        telefone = input('Telefone: ')
        email = input('Email: ')
        contato = Contato(self.proximo_id, nome, telefone, email)
        self.contatos[self.proximo_id] = contato
        print(f'Contato adicionado! ID: {self.proximo_id}')
        self.proximo_id += 1
    def alterar(self):
        try:
            id_contato = int(input('Digite o ID do contato a alterar: '))
        except ValueError:
            print('ID inválido.')
            return
        if id_contato not in self.contatos:
            print('Contato não encontrado.')
            return
        contato = self.contatos[id_contato]
        nome = input(f'Novo nome [{contato.nome}]: ') or contato.nome
        telefone = input(f'Novo telefone [{contato.telefone}]: ') or contato.telefone
        email = input(f'Novo email [{contato.email}]: ') or contato.email
        contato.nome = nome
        contato.telefone = telefone
        contato.email = email
        print('Contato alterado!')
    def apagar(self):
        try:
            id_contato = int(input('Digite o ID do contato a apagar: '))
        except ValueError:
            print('ID inválido.')
            return
        if id_contato in self.contatos:
            del self.contatos[id_contato]
            print('Contato apagado!')
        else:
            print('Contato não encontrado.')
    def listar(self):
        if not self.contatos:
            print('Agenda vazia.')
            return
        for contato in self.contatos.values():
            print(f'ID: {contato.id} | Nome: {contato.nome} | Telefone: {contato.telefone} | Email: {contato.email}')

def menu():
    agenda = AgendaDeContatos()
    while True:
        print('\n--- Agenda de Contatos ---')
        print('1. Adicionar contato')
        print('2. Alterar contato')
        print('3. Apagar contato')
        print('4. Listar contatos')
        print('0. Sair')
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            agenda.adicionar()
        elif opcao == '2':
            agenda.alterar()
        elif opcao == '3':
            agenda.apagar()
        elif opcao == '4':
            agenda.listar()
        elif opcao == '0':
            print('Saindo...')
            break
        else:
            print('Opção inválida!')

if __name__ == '__main__':
    menu()
