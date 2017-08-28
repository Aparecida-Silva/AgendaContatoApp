import json

class Agenda:
    def __init__(self, proprietario):
        self.proprietario = proprietario
        self.contatos = []

    def contarContatos(self):
        return len(self.contatos)

    def listarContatos(self):
        for contato in self.contatos:
            print(contato)

    def incluirContato(self, contato):
        self.contatos.append(contato)

    def buscarContato(self, nome):
        for contato in self.contatos:
            if(contato.pessoa.nome.lower() == nome.lower()):
                return contato

    def excluirContato(self, nome):
        self.contatos.remove(self.buscarContato(nome))

    def salvarEmJson(self):
        f = None
        try:
            f = open(self.contatos[0].pessoa["nome"] + ".json")
        except:
            f = open(self.contatos[0].pessoa["nome"] + ".json", "w")
        f.write(json.dumps(self.contatos[0].__dict__))
        f.close()
