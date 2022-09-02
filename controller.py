# Importando as outras classes criadas para que elas se comuniquem através do Controller

from model import Model
from view import View

class Controller:
    def __init__(self):

        # Aqui estou inicializando dois objetos, um da classe Model e outro da classe View, que serão executados no construtor, assim que a classe Controller for executada

        self.model = Model()
        self.view = View(self) # Quando a view é criada pelo controller, ela já passa um argumento do controller, como é exigido na view

    def main(self):
        print("Calculator - Main")
        self.view.main() # Aqui estou chamando o método main da view, em view.py. Consigo isso porque no init do controller eu declarei self.view, que comunica com a view.

    def on_button_click(self, caption):  # A função de callback, que gerencia o clique de todos os botões
        print(f'Button {caption} clicked')
        result = self.model.calculate(caption)  # Está chamando o calculate do Model

        self.view.value_var.set(result)  # Estou usando a variável de instância criada em View para poder passar os dados.


if __name__ == '__main__':
    calculator = Controller()  # Aqui crio um objeto calculator do tipo Controller
    calculator.main()          # Aqui eu chamo a função main do objeto calculator do tipo Controller

    # Se eu chamar qualquer outro código a partir daqui, não vai ser executado, pois calculator.main() chama o mainloop
    # Código aqui só vai ser executado depois que eu fechar a janela do tkinter, que vai encerrar o mainloop