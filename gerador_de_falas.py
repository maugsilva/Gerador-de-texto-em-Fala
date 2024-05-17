from tkinter import *
from playsound import playsound
from gtts import *
import os
import time 

# Configurando os parâmetros da janela do tkinter
 
root = Tk()
root.title('Conversor de Texto em Fala')
root.geometry('600x520')
root.maxsize(600,520)
root.minsize(600,520)
root.configure(bg='#1d1d1d')

# Função para definir tamanho da margem
def margem(altura):
    tela = Canvas(root, 
                  width=600,
                  height=altura,
                   bg='#1d1d1d',
                    bd=0,
                    highlightthickness=0,
                    relief='ridge')
    tela.pack()

# Função dos botões
def botao(texto, comando, padx):
    botao = Button(root,
                   text=texto,
                   padx=padx,
                   pady=20,
                   command=comando,
                   fg='#FFFFFF',
                   activebackground='#FFFFFF',
                   bg='#C69749',
                   activeforeground='#C69749',
                   relief=FLAT,
                   font=('Montserrat', 12, 'bold'))
    botao.pack()
# Função do botão INICIAR     
def inicia():
    texto_inserido = entrada.get()
    fala = gTTS(text=texto_inserido, lang='pt', tld='com.br')
    arquivo_fala = 'arquivo_fala.mp3'
    fala.save(arquivo_fala)
    time.sleep(0.5)
    playsound(arquivo_fala)
    
# Função do botão RESETAR
def resetar():
    entrada.delete(0, END)
    os.remove('arquivo_fala.mp3')

margem(20)
title = Label(root, 
              bg='#1d1d1d',
              fg='#FFFFFF',
              font=('Montserrat', 18, 'bold'),
              text='Conversor de Texto em Fala')

title.pack()
margem(30)

# Subtítulo 
inserir_texto = Label(root, 
            bg='#1d1d1d',
            fg='#FFFFFF',
            font=('Montserrat', 18),
            text='Insira o seu texto')
inserir_texto.pack()

# Entrada aonde vai aparecer o texto quando escrever
entrada = Entry(root,
                width=25, 
                borderwidth=4,
                relief=FLAT,
                foreground='#FFFFFF',
                bg='#000000',
                font=('Montserrat', 21, 'bold'),
                justify=CENTER)
entrada.pack()
margem(20)
botao_iniciar = botao('INICIAR', inicia, 37)
margem(10)
botao_reset = botao('RESETAR', resetar, 30)
root.mainloop()