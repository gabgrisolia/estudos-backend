usuarios = []

nome = input("Digite o nome do usuário: ")
email = input("Digite o email do usuário: ")

usuario = {
    "nome": nome,
    "email": email
}

usuarios.append(usuario)

print("Usuário cadastrado:")
print(usuarios)
