import string
import random
import tkinter as tk

def GeradorDeSenha():
    caracteres = string.ascii_letters + string.digits
    comprimento = 12

    senha = []
    for i in range (comprimento):
        caractere = random.choice(caracteres)
        senha.append(caractere)
    senha_final = ''.join(senha)

    label_senha.config(text=senha_final)

def centralizar_janela(janela, largura, altura):
    # Força a atualização do sistema
    janela.update_idletasks()
    
    # Pega o tamanho real da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    # Calcula o centro
    posicao_x = (largura_tela // 2) - (largura // 2)
    posicao_y = (altura_tela // 2) - (altura // 2)
    
    # Define o tamanho e a posição de uma vez só
    janela.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")

janela = tk.Tk()
janela.title("Gerador de senhas")

titulo = tk.Label(janela, text="Clique no botão para gerar uma senha:", font=("Arial", 11))
titulo.pack(pady = 10)

botao = tk.Button(janela, text="Gerar senha", command = GeradorDeSenha, font= ("Arial", 10, "bold"))
botao.pack(pady = 10)

label_senha = tk.Label(janela, text="", font=("Arial", 14, "bold"), fg="green")
label_senha.pack(pady=15)

centralizar_janela(janela, 400, 250)

janela.mainloop()
