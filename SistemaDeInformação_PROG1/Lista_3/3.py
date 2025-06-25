login = str(input("Usuario --->"))

senha = str(input("Senha --->"))

while len(senha) < 6 or login.upper() == senha.upper():
    senha = str(input("Senha Invalida tente novamente\nSenha --->"))

print("Usuario ---> %s\nSenha ---> %s\nUsuaruio Cadastrado com sucesso!" %(login,senha))