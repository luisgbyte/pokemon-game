import pickle

from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):
    print("Olá {}, você poderá escolher agora o pokemon que irá lhe acompanhar nessa jornada!".format(player))

    pikachu = PokemonEletrico("Pikachu", level=1) 
    charmander = PokemonFogo("Charmander", level=1) 
    squirtle = PokemonAgua("Squirtle", level=1) 

    print("Você possui 3 escolhas: ")
    print("1 -", pikachu) 
    print("2 -", charmander) 
    print("3 -", squirtle)

    while True:
        escolha = input("Escolha o seu Pokemon: ")

        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolha inválida!")


def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso!")
    except Exception as error:
        print("Erro ao salvar jogo")
        print(error)

def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Loading feito com sucesso")
            return player
    except Exception as error:
        print("Save não encontrado!!!")
 


if __name__=="__main__":
    print('------------------------------------------')
    print("Bem vindo ao game Pokemon RPG de terminal")
    print('------------------------------------------')

    player = carregar_jogo()

    if not player:
        nome = input("Olá, qual é o seu nome: ")
        player = Player(nome)

        print("Olá {}, esse é um mundo habitado por pokemons, sua missão é se tornar um grande mestre pokemon".format(player))
        print("Capture o máximo de pokemons que conseguir e lute com seus inimigos")
        player.mostrar_dinheiro()

        if player.pokemons:
            print("Já vi que você têm alguns pokemons")
            player.mostrar_pokemons()
        else:
            print("Você não têm nenhum pokemon, portando precisa escolher um")
            escolher_pokemon_inicial(player)

        print("Pronto, agora que você já possui um pokemon, enfrente seu arqui-rival Gary desde o jardim de infância")
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print("----------------------------------")
        print("O que deseja fazer?")
        print("1 - Explorar o mapa")
        print("2 - Lutar com um inimigo")
        print("3 - Ver Pokeagenda")
        print("0 - Sair do jogo")
        escolha = input("Sua escolha:")

        if escolha == "0":
            print("Fechando o jogo...")
            break
        elif escolha =="1":
            player.explorar()
            salvar_jogo(player)
        elif escolha =="2":
            inimigo_aleatorio =Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo
        elif escolha =="3":
            player.mostrar_pokemons()
        else:
            print("Escolha inválida")
         
            