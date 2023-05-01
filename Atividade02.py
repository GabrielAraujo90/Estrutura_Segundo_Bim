#Gabriel Araujo 
#Atividade 02

class Time:
    def __init__(self, nome, jogadores):
        self.nome = nome
        self.jogadores = jogadores
    
    def adiciona_jogador(self, nome, camisa):
        self.jogadores.append([nome, camisa])
    
    def imprime_jogadores(self):
        print(f"Jogadores do time {self.nome}:")
        for jogador in self.jogadores:
            print(f"Nome: {jogador[0]}, Camisa: {jogador[1]}")



jogadores_santos = [["Angelo", 11], ["Lucas Braga", 30], ["Marcos Leonardo", 9]]
santos = Time("Santos", jogadores_santos)


santos.adiciona_jogador("João Paulo", 34)
santos.adiciona_jogador("Lucas Lima", 23)


santos.imprime_jogadores()
