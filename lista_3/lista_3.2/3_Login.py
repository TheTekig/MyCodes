def log_in():
    login = str(input("Usuario --->"))
    return(login)

def senha_a():
    senha = str(input("Senha --->"))

    while len(senha) < 6 or login.upper() == senha.upper():
        senha = str(input("Senha Invalida tente novamente\nSenha --->"))
    return(senha)


login = log_in()
senha = senha_a()
print("Usuario ---> %s\nSenha ---> %s\nUsuaruio Cadastrado com sucesso!" %(login,senha))