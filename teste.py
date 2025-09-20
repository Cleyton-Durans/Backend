funcionariosParaCadastrar = [
    {"nome": "Cleyton", "sobrenome": "Durans", "idade": 25}
    {"nome": "Lucas", "sobrenome": "Santos", "idade": 25}
    {"nome": "Luiz", "sobrenome": "Nascimento", "idade": 25}
]

cadastrosParaEnviarParaOBanco = [ 
    
]​

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def salvar(self):
        print(f"Foi salvo o  usuário {self.nome} {self.nome} de idade {self.nome} foi salvo com sucesso!")


    