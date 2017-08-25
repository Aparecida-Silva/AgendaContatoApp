import json

class Agenda:
    def __init__(self, proprietario):
        self.proprietario = proprietario
        self.contatos = []

    def contarContatos(self):
        pass

    def listarContatos(self):
        pass

    def incluirContato(self, contato):
        pass

    def excluirContato(self, nome):
        pass

    def salvarEmJson(self):
        print(json.dumps(self.contatos[0].__dict__))
