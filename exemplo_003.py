"""Exemplo 3."""


from tkinter import *


class Janela:
    """Classe que implementa as funções da janela."""
    def __init__(self, toplevel):
        """Função que inicializa a classe janela."""
        self.fr1 = Frame(toplevel)
        self.fr1.pack()

        self.botao1 = Button(self.fr1, text='oi!')
        self.botao1['background'] = 'green'
        self.botao1['height'] = 3
        self.botao1.pack()

        self.botao2 = Button(self.fr1, bg='red', font=('Times', '16'))
        self.botao2['text'] = 'Tchau!'
        self.botao2['fg'] = 'yellow'
        self.botao2['width'] = 12
        self.botao2.pack()

raiz = Tk()
Janela(raiz)
raiz.mainloop()


