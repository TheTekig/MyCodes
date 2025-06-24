import tkinter as tk

def clicar(tecla):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual + str(tecla))

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

def limpar():
    entrada.delete(0, tk.END)

janela = tk.Tk()
janela.title("Calculadora")

entrada = tk.Entry(janela, width=16, font=("Arial", 24), justify="right")
entrada.grid(row=0, column=0, columnspan=4)

botoes = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
    ("C",5,0)
]

for (texto, linha, coluna) in botoes:
    if texto == "=":
        cmd = calcular
    elif texto == "C":
        cmd = limpar
    else:
        cmd = lambda t=texto: clicar(t)
    tk.Button(janela, text=texto, width=5, height=3, font=("Arial", 18), command=cmd).grid(row=linha, column=coluna)

janela.mainloop()