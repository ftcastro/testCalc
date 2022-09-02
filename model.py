class Model:

    def __init__(self):

        self.previous_value = ''   # Uma variável de instância para receber o valor do primeiro operador quando o sinal da operação for pressionado
        self.value = ''            # Uma variável de instância que vai reter o que está no display
        self.operator = ''         # Uma variável de instância para detectar qual operador foi selecionado para fazer a conta

    def calculate(self, caption):  # Método público calculate. Vai ser acessado de fora da classe.
        print(f'Calculating for {caption}')

        if caption == 'C':  # Se o usuário clicar em C, self.value (a variável de instância) vai receber uma string vazia, o que vai limpar o display
                            # Aqui estou resetando todas as variáveis que foram usadas
            self.value = ''
            self.previous_value = ''
            self.operator = ''
            print("Todas as variáveis foram resetadas")

        elif caption == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value  # Aqui eu verifico se o valor é positivo ou negativo. Caso seja negativo, transformo em positivo. Caso seja positivo, transformo em negativo. Lembrando que aqui estamos trabalhando com as strings dos valores, então vai ser só o visual. Os cálculos são feitos em outro lugar.

        elif caption == '%':
            pass

        elif caption == '=':
            pass

        elif caption == '.':
            if not caption in self.value:  # Aqui eu verifico se o número já não tem um ponto decimal. Se tiver, não faço nada. Se não tiver, eu coloco onde ele foi clicado.
                self.value += caption

        elif isinstance(caption, int):
            self.value += str(caption)  # Se o que foi clicado é um número, vou adicionar a versão string deste número no display da calculadora
            print("Foi acionado um botão com número")

        else:
            if self.value:  # Aqui eu estou verificando se o valor atual não está vazio. Ao se utilizar apenas if self.value, é o mesmo que comparar se self.value é True
                self.operator = caption

                self.previous_value = self.value

        return self.value

    def _evaluate(self):
        return eval(self.previous_value+self.operator+self.value)
