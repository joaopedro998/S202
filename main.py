class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print('O som que o : ' + self.nome + 'faz e : ' + self.som)

    def mudar_cor(self, nova_cor):
        self.cor = nova_cor


class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        self.tamanho = tamanho
        super().__init__(nome, idade, especie, cor, som)

    def Trombar(self):
        print('O som que o : ' + self.nome + 'faz e : ' + self.som)

    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho


nome = input("nome do elefante: ")
idade = int(input("idade do elefante: "))
som = input("som do elefante: ")
especie = input("especie do elefante: ")
cor = input("cor do elefante: ")
tamanho = input("tamanho do elefante: ")

elefante = Elefante(nome, idade, especie, cor, som, tamanho)
if elefante.especie == "Africano":
    if elefante.idade < 10:
        elefante.mudar_tamanho("pequeno")
        elefante.som = "Paaah"
if elefante.especie == "Africano":
    if elefante.idade >= 10:
        elefante.mudar_tamanho("grande")
        elefante.som = "PAHHHHHH"

print("Nome do elefante: " + elefante.nome)
print("Som do elefante: " + elefante.som)
print("Especie do elefante: " + elefante.especie)
print("Cor do elefante: " + elefante.cor)
print("Tamanho do elefante: " + elefante.tamanho)

