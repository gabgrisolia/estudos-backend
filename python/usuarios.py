usuarios = []

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")

    usuario = {
        "nome": nome,
        "email": email
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i} - {usuario['nome']} ({usuario['email']})")

while True:
    print("\n1 - Cadastrar usuário")
    print("2 - Listar
