import tkinter
from tkinter import *
from tkinter import ttk

# cores ---------------------------------------
co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 = "#fcfbf7"
fundo = "#3b3b3b"  # preta / black

# criando janela principal
janela = Tk()
janela.title('')
janela.geometry('260x370')
janela.configure(bg=fundo)


# DIVIVINDO FRAMES

janela_placar = Frame(janela, width=240, height=100, bg=co1, relief=RAISED)
janela_placar.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

janela_jogo = Frame(janela, width=240, height=300, bg=fundo, relief=FLAT)
janela_jogo.grid(row=1, column=0, sticky=NW)

# PLACAR
jogador_x = Label(janela_placar, text="X", height=1, relief=FLAT,
                  anchor=CENTER, font=("Ivy 40 bold"), bg=co1, fg=co7)
jogador_x.place(x=25, y=10)

jogador_x_nome = Label(janela_placar, text="Jogador 1", height=1, relief=FLAT,
                       anchor=CENTER, font=("Ivy 7 bold"), bg=co1, fg=co0)
jogador_x_nome.place(x=17, y=70)

jogador_x_pontuacao = Label(janela_placar, text="0", height=1, relief=FLAT,
                            anchor=CENTER, font=("Ivy 30 bold"), bg=co1, fg=co0)
jogador_x_pontuacao.place(x=80, y=20)


separador = Label(janela_placar, text=":", height=1, relief=FLAT,
                  anchor=CENTER, font=("Ivy 30 bold"), bg=co1, fg=co0)
separador.place(x=110, y=20)


jogador_o = Label(janela_placar, text="O", height=1, relief=FLAT,
                  anchor=CENTER, font=("Ivy 40 bold"), bg=co1, fg=co4)
jogador_o.place(x=170, y=10)

jogador_o_nome = Label(janela_placar, text="Jogador 2", height=1, relief=FLAT,
                       anchor=CENTER, font=("Ivy 7 bold"), bg=co1, fg=co0)
jogador_o_nome.place(x=165, y=70)

jogador_o_pontuacao = Label(janela_placar, text="0", height=1, relief=FLAT,
                            anchor=CENTER, font=("Ivy 30 bold"), bg=co1, fg=co0)
jogador_o_pontuacao.place(x=130, y=20)


# PARTE LÓGICA
jogador_1 = "X"
jogador_2 = "O"

jogador_1_pontos = 0
jogador_2_pontos = 0

tabela = [["1", "2", "3"], ["4", "5", "6"], ["7", "8,", "9"]]

jogadorDaVez = "X"
cont = 0
contador_rodadas = 0


def iniciarJogo():
    def controlarJogo(event):
        global jogadorDaVez
        global cont

        if event == "1":
            if botao_1["text"] == "":
                if jogadorDaVez == "X":
                    cor = co7
                elif jogadorDaVez == "O":
                    cor = co8
            botao_1["fg"] = cor
            botao_1["text"] = jogadorDaVez
            tabela[0][0] = jogadorDaVez
            if jogadorDaVez == "X":
                jogadorDaVez = "O"
                proximoJogador = "Jogador 1"
            else:
                jogadorDaVez = "X"
                proximoJogador = "Jogador 2"
            cont += 1
        if event == "2":
            if botao_2["text"] == "":
                if jogadorDaVez == "X":
                    cor = co7
                elif jogadorDaVez == "O":
                    cor = co8
            botao_2["fg"] = cor
            botao_2["text"] = jogadorDaVez
            tabela[0][1] = jogadorDaVez
            if jogadorDaVez == "X":
                jogadorDaVez = "O"
                proximoJogador = "Jogador 1"
            else:
                jogadorDaVez = "X"
                proximoJogador = "Jogador 2"
            cont += 1
        if event == "3":
            if botao_3["text"] == "":
                if jogadorDaVez == "X":
                    cor = co7
                elif jogadorDaVez == "O":
                    cor = co8
            botao_3["fg"] = cor
            botao_3["text"] = jogadorDaVez
            tabela[0][2] = jogadorDaVez
            if jogadorDaVez == "X":
                jogadorDaVez = "O"
                proximoJogador = "Jogador 1"
            else:
                jogadorDaVez = "X"
                proximoJogador = "Jogador 2"
            cont += 1
        if event == "4":
            if botao_4["text"] == "":
                if jogadorDaVez == "X":
                    cor = co7
                elif jogadorDaVez == "O":
                    cor = co8
            botao_4["fg"] = cor
            botao_4["text"] = jogadorDaVez
            tabela[1][0] = jogadorDaVez
            if jogadorDaVez == "X":
                jogadorDaVez = "O"
                proximoJogador = "Jogador 1"
            else:
                jogadorDaVez = "X"
                proximoJogador = "Jogador 2"
            cont += 1
        if event == "5":
            if botao_5["text"] == "":
                if jogadorDaVez == "X":
                    cor = co7
                elif jogadorDaVez == "O":
                    cor = co8
            botao_5["fg"] = cor
            botao_5["text"] = jogadorDaVez
            tabela[1][1] = jogadorDaVez
            if jogadorDaVez == "X":
                jogadorDaVez = "O"
                proximoJogador = "Jogador 1"
            else:
                jogadorDaVez = "X"
                proximoJogador = "Jogador 2"
            cont += 1
        if event == "6":
            if botao_6["text"] == "":
                if jogadorDaVez == "X":
                    cor = co7
                elif jogadorDaVez == "O":
                    cor = co8
            botao_6["fg"] = cor
            botao_6["text"] = jogadorDaVez
            tabela[1][2] = jogadorDaVez
            if jogadorDaVez == "X":
                jogadorDaVez = "O"
                proximoJogador = "Jogador 1"
            else:
                jogadorDaVez = "X"
                proximoJogador = "Jogador 2"
            cont += 1
        if event == "7":
            if botao_7["text"] == "":
                if jogadorDaVez == "X":
                    cor = co7
                elif jogadorDaVez == "O":
                    cor = co8
            botao_7["fg"] = cor
            botao_7["text"] = jogadorDaVez
            tabela[2][0] = jogadorDaVez
            if jogadorDaVez == "X":
                jogadorDaVez = "O"
                proximoJogador = "Jogador 1"
            else:
                jogadorDaVez = "X"
                proximoJogador = "Jogador 2"
            cont += 1
        if event == "8":
            if botao_8["text"] == "":
                if jogadorDaVez == "X":
                    cor = co7
                elif jogadorDaVez == "O":
                    cor = co8
            botao_8["fg"] = cor
            botao_8["text"] = jogadorDaVez
            tabela[2][1] = jogadorDaVez
            if jogadorDaVez == "X":
                jogadorDaVez = "O"
                proximoJogador = "Jogador 1"
            else:
                jogadorDaVez = "X"
                proximoJogador = "Jogador 2"
            cont += 1
        if event == "9":
            if botao_9["text"] == "":
                if jogadorDaVez == "X":
                    cor = co7
                elif jogadorDaVez == "O":
                    cor = co8
            botao_9["fg"] = cor
            botao_9["text"] = jogadorDaVez
            tabela[2][2] = jogadorDaVez
            if jogadorDaVez == "X":
                jogadorDaVez = "O"
                proximoJogador = "Jogador 1"
            else:
                jogadorDaVez = "X"
                proximoJogador = "Jogador 2"
            cont += 1
        if cont >= 5:
            # LINHAS
            if tabela[0][0] == tabela[0][1] == tabela[0][2]:
                checandoVitoria(jogadorDaVez)
            elif tabela[1][0] == tabela[1][1] == tabela[1][2]:
                checandoVitoria(jogadorDaVez)
            elif tabela[2][0] == tabela[2][1] == tabela[2][2]:
                checandoVitoria(jogadorDaVez)
              # COLUNAS
            if tabela[0][0] == tabela[1][0] == tabela[2][0]:
                checandoVitoria(jogadorDaVez)
            elif tabela[0][1] == tabela[1][1] == tabela[2][1]:
                checandoVitoria(jogadorDaVez)
            elif tabela[0][2] == tabela[1][2] == tabela[2][2]:
                checandoVitoria(jogadorDaVez)
              # DIAGONAIS
            if tabela[0][0] == tabela[1][1] == tabela[2][2]:
                checandoVitoria(jogadorDaVez)
            elif tabela[0][2] == tabela[1][1] == tabela[2][0]:
                checandoVitoria(jogadorDaVez)

            # EMPATE

            if cont >= 9:
                checandoVitoria("Empate")

    def checandoVitoria(resultado):
        global contador_rodadas
        global cont
        global jogadorDaVez
        global tabela
        global jogador_1_pontos
        global jogador_2_pontos

        # bloqueando os botoes
        botao_1['state'] = 'disable'
        botao_2['state'] = 'disable'
        botao_3['state'] = 'disable'
        botao_4['state'] = 'disable'
        botao_5['state'] = 'disable'
        botao_6['state'] = 'disable'
        botao_7['state'] = 'disable'
        botao_8['state'] = 'disable'
        botao_9['state'] = 'disable'

        vencedor = Label(janela_jogo, text="", width=17, relief=FLAT,
                         anchor=CENTER, font=("Ivy 13 bold"), bg=co1, fg=co2)
        vencedor.place(x=40, y=85)

        if resultado == "X":
            jogador_2_pontos += 1
            vencedor["text"] = "Jogador 2 venceu"
            jogador_o_pontuacao["text"] = jogador_2_pontos
        elif resultado == "O":
            jogador_1_pontos += 1
            vencedor["text"] = "Jogador 1 venceu"
            jogador_x_pontuacao["text"] = jogador_1_pontos
        elif resultado == "Empate":
            vencedor["text"] = "Empatado"

        def start():
            # limpando os botoes
            botao_1['text'] = ''
            botao_2['text'] = ''
            botao_3['text'] = ''
            botao_4['text'] = ''
            botao_5['text'] = ''
            botao_6['text'] = ''
            botao_7['text'] = ''
            botao_8['text'] = ''
            botao_9['text'] = ''

            botao_1['state'] = 'normal'
            botao_2['state'] = 'normal'
            botao_3['state'] = 'normal'
            botao_4['state'] = 'normal'
            botao_5['state'] = 'normal'
            botao_6['state'] = 'normal'
            botao_7['state'] = 'normal'
            botao_8['state'] = 'normal'
            botao_9['state'] = 'normal'

            vencedor.destroy()
            botao_jogar.destroy()

        # Botao jogar
        botao_jogar = Button(janela_jogo, command=start, text='Proxima rodada', height=1,  font=(
            'Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
        botao_jogar.place(x=70, y=115)

        def fimDeJogo():
            botao_jogar.destroy()
            vencedor.destroy()

            finalizarJogo()

        if contador_rodadas > 4:
            fimDeJogo()
        else:
            contador_rodadas += 1
            # reiniciando a tabela
            tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            cont = 0

    def finalizarJogo():
        global contador_rodadas
        global cont
        global tabela
        global jogador_1_pontos
        global jogador_2_pontos

        tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        contador_rodadas = 0
        jogador_1_pontos = 0
        jogador_2_pontos = 0
        cont = 0

        # bloqueando os botoes
        botao_1['state'] = 'disable'
        botao_2['state'] = 'disable'
        botao_3['state'] = 'disable'
        botao_4['state'] = 'disable'
        botao_5['state'] = 'disable'
        botao_6['state'] = 'disable'
        botao_7['state'] = 'disable'
        botao_8['state'] = 'disable'
        botao_9['state'] = 'disable'

        fim = Label(janela_jogo, text='Jogo Acabou', width=17, relief='flat',
                    anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        fim.place(x=40, y=85)

        # jogar de novo

        def jogarDeNovo():
            jogador_x_pontuacao["text"] = '0'
            jogador_o_pontuacao["text"] = '0'
            fim.destroy()
            botao_jogar.destroy()

            # chamando a funcao iniciar o jogo
            iniciarJogo()

        # Botao jogar denovo
        botao_jogar = Button(janela_jogo, command=jogarDeNovo, text='Jogar de novo', height=1,  font=(
            'Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
        botao_jogar.place(x=70, y=115)

    # JOGO

    # LINHAS VERTICAIS
    linha_vertical = Label(janela_jogo, text="", height=24, relief=FLAT, pady=5,
                           anchor=CENTER, font=("Ivy 5 bold"), bg=co0)
    linha_vertical.place(x=90, y=12)

    linha_vertical = Label(janela_jogo, text="", height=24, relief=FLAT, pady=5,
                           anchor=CENTER, font=("Ivy 5 bold"), bg=co0)
    linha_vertical.place(x=155, y=12)

    # LINHAS HORIZONTAIS
    linha_horizontal = Label(janela_jogo, text="", width=182, relief=FLAT, padx=2, pady=1,
                             anchor=CENTER, font=("Ivy 1 bold"), bg=co0)
    linha_horizontal.place(x=30, y=65)
    linha_horizontal = Label(janela_jogo, text="", width=182, relief=FLAT, padx=2, pady=1,
                             anchor=CENTER, font=("Ivy 1 bold"), bg=co0)
    linha_horizontal.place(x=30, y=128)

    # BOTÔES LINHA 1
    botao_1 = Button(janela_jogo, command=lambda: controlarJogo("1"), text="", width=3, height=1, font=(
        "Ivy 19 bold"), overrelief=RIDGE, relief=FLAT, bg=fundo, fg=co7)
    botao_1.place(x=34, y=12)

    botao_2 = Button(janela_jogo, command=lambda: controlarJogo("2"), text="", width=3, height=1, font=(
        "Ivy 19 bold"), overrelief=RIDGE, relief=FLAT, bg=fundo, fg=co7)
    botao_2.place(x=99, y=12)

    botao_3 = Button(janela_jogo, command=lambda: controlarJogo("3"), text="", width=3, height=1, font=(
        "Ivy 19 bold"), overrelief=RIDGE, relief=FLAT, bg=fundo, fg=co7)
    botao_3.place(x=162, y=12)

    # BOTÔES LINHA 2
    botao_4 = Button(janela_jogo, command=lambda: controlarJogo("4"), text="", width=3, height=1, font=(
        "Ivy 19 bold"), overrelief=RIDGE, relief=FLAT, bg=fundo, fg=co7)
    botao_4.place(x=34, y=75)

    botao_5 = Button(janela_jogo, command=lambda: controlarJogo("5"), text="", width=3, height=1, font=(
        "Ivy 19 bold"), overrelief=RIDGE, relief=FLAT, bg=fundo, fg=co7)
    botao_5.place(x=99, y=75)

    botao_6 = Button(janela_jogo, command=lambda: controlarJogo("6"), text="", width=3, height=1, font=(
        "Ivy 19 bold"), overrelief=RIDGE, relief=FLAT, bg=fundo, fg=co7)
    botao_6.place(x=162, y=75)

    # BOTÔES LINHA 3
    botao_7 = Button(janela_jogo, command=lambda: controlarJogo("7"), text="", width=3, height=1, font=(
        "Ivy 19 bold"), overrelief=RIDGE, relief=FLAT, bg=fundo, fg=co7)
    botao_7.place(x=34, y=138)

    botao_8 = Button(janela_jogo, command=lambda: controlarJogo("8"), text="", width=3, height=1, font=(
        "Ivy 19 bold"), overrelief=RIDGE, relief=FLAT, bg=fundo, fg=co7)
    botao_8.place(x=99, y=138)

    botao_9 = Button(janela_jogo, command=lambda: controlarJogo("9"), text="", width=3, height=1, font=(
        "Ivy 19 bold"), overrelief=RIDGE, relief=FLAT, bg=fundo, fg=co7)
    botao_9.place(x=162, y=138)

# BOTÃO JOGAR


botao_jogar = Button(janela_jogo, command=iniciarJogo, text="Jogar", width=10, height=1, font=(
    "Ivy 10 bold"), overrelief=RIDGE, relief=RAISED, bg=fundo, fg=co0)
botao_jogar.place(x=85, y=210)

janela.mainloop()
