"""Exemplo 2"""


from tkinter import *


class Janela:
    """Classe da janela."""
    def __init__(self, toplevel):
        """Função de inicialização da classe."""
        self.frame1 = Frame(toplevel)
        self.frame1.pack()
        self.botao = Button(self.frame1, text="oi", background="green")
        self.botao.pack()

raiz = Tk()
Janela(raiz)
raiz.mainloop()

