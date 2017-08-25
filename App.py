from models.Agenda import Agenda
from models.Contato import Contato
from models.Telefone import Telefone

def main():
    agenda = Agenda("Rennan")
    agenda.contatos.append(Contato("25/08", "Pedro", [Telefone("333", 83, "+55").__dict__]))

    agenda.salvarEmJson()

if __name__ == "__main__":
    main()
