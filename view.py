# Importo as coisas na view porque é onde vai ser executado

import tkinter as tk
from tkinter import ttk


class View(tk.Tk):  # Aqui a classe View está herdando os atributos de tk, assim eu tenho acesso a tudo do tkinter direto nela

    PAD = 10  # Isso é uma variável de classe. Ela não é específica a uma instância, mas todos os objetos dessa classe a possuem.

    MAX_BUTTONS_PER_ROW = 4  # Indica o máximo de botões que cada linha terá. Isso é feito para criar a matriz corretamente. O layout está sendo feito dinamicamente.

    button_captions = ['C', '+/-', '%', '/',                # Aqui estou criando os botões dinamicamente, não preciso criar tudo individualmente
                       7, 8, 9, '*',
                       4, 5, 6, '-',
                       1, 2, 3, '+',
                       0, '.', '='
                       ]

    def __init__(self, controller):     # Quando inicializar a view, ele vai exigir que passemos a variável controller


             # Eu tenho acesso a esses métodos por causa da herança!
        super().__init__()  # Aqui eu estou chamando o método inicializador da superclasse, que no caso é tk, uma vez que View herda de tk. View é subclasse de tk
        self.title("Calculator")

        self.controller = controller  # Agora a view tem acesso ao controller

        self.value_var = tk.StringVar()  # Ao invés de criar a variável direto na Entry, ela está aqui. Essa é a variável do Entry.



        self._make_main_frame()
        self._make_entry()  # O método privado é chamado só dentro da própria classe!
        self._make_buttons()


    def main(self):
        print("Main - View")
        self.mainloop()  # Aqui eu invoco o loop infinito que faz a interface carregar, ele fica rodando até eu fechar a janela. Qualquer código depois dele não é executado.


    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)  # Esse self aqui é a classe View, que herda tk.Tk. Ele é um atributo da classe, feito para ser acessado de fora dessa função.
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)


    def _make_entry(self):                                                             # Indica que o método deve ser tratado como privado. Conveção do Python. Não será chamado em model e controller
        ent = ttk.Entry(self.main_frm, justify="right", textvariable=self.value_var, state='disabled')   # Aqui eu estou passando o main frame da classe logo acima como um atributo em entry. Veja que é necessário colocar o self. Aqui estou amarrando a textvariable do Entry com a variável criada. Onde quer que eu altere esse Entry, vai ser naquela variável que vou mexer. Por isso o Entry não precisa ser um atributo da classe View.
        ent.pack(fill='x')                                                                     # A entry estará em main_frm


    def _make_buttons(self):
        outer_frm = ttk.Frame(self.main_frm)  # Estou criando um frame para os botões e colocando ele no nosso main frame. O outer_frm vai ter nested frames para cada uma das linhas
        outer_frm.pack()

        frm = ttk.Frame(outer_frm)  # Inner frame nested no outer frame
        frm.pack()

        buttons_in_row = 0

        for caption in self.button_captions:  # Aqui estou criando os botões dinamicamente e dando pack nos mesmos
            if buttons_in_row == self.MAX_BUTTONS_PER_ROW:  # Aqui estou fazendo uma verificação pra poder colocar os quatro botões no máximo por linha
                frm = ttk.Frame(outer_frm)
                frm.pack()

                buttons_in_row = 0

            btn = ttk.Button(frm, text=caption, command=(lambda button=caption: self.controller.on_button_click(button)))  # Lambda é usado quando é necessário chamar uma função de callback passando parâmetros. O button que é passado dentro da função on_button_click é o button que acabamos de criar.
            btn.pack(side='left')
            # Esse trecho de código nos salva um monte de tempo, pois não é necessário criar uma função de callback para cada botão, dado que a função é alterada dinamicamente a depender do botão clicado.
            buttons_in_row += 1  # Incrementando a buttons in row
