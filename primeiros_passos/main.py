from usuario import Usuario

continuar = 1
lista_usuarios = []

while continuar !=0:
    try:
        nome = input("Digite seu nome: ")
        sobrenome = input("Digite seu sobrenome: ")
        idade = int(input("Digite sua idade: "))
        usuario = Usuario(nome,sobrenome,idade)

        if(usuario.idade == 98):
            continue
        lista_usuarios.append(usuario)

        continuar =int(input("Deseja Continuar? Sim - 1. Nã0 -0"))
    except ValueError:
        print("Digite um numero valido")

else:
    print("Lista de Suarios")
    for usuarios in lista_usuarios:
        print(f"{usuarios.nome} {usuarios.sobrenome} - {usuarios.idade} ")
