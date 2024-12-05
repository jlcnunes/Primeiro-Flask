class Curso:

    def __init__(self, nome, descricao, habilidades, dificuldade):
        # note que neste exemplo , toddos os atributos são púnlicos
        self.nome = nome
        self.descricao = descricao
        self.habilidades = habilidades
        self.dificuldade = dificuldade
    

    def get_nome(self):
        return self.nome

    def get_descricao(self):
        return self.descricao
    
    def get_habilidades(self):
        return self.habilidades
    
    def get_dificuldade(self):
        return self.dificuldade

