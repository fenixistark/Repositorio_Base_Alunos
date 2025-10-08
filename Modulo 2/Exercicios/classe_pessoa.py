class Pessoa:
    def __init__(self, idade, nome, cpf, nacionalidade, email, numero, animais_de_estimação, QI, trabalha_em, salario):
        self._nome = 'ana'
        self._idade = '32'
        self._cpf = '4873589723'
        self._nacionalidade = 'brasileira'
        self._email = 'aninha123@gmail.com'
        self._numero = '+55118763429'
        self._animais_de_estimação = '4'
        self._QI = '93'
        self._trabalha_em = 'sendo caixa em um super mercado'
        self._salario = '1300'
        #getter
        @property
        def nome(self):
            return self._nome
        #setter
        @nome.setter
        def nome(self, ana):
            self._nome = 'ana'
        pessoa = Pessoa(30, "ana", 4873589723, "brasileira", "aninha123@gmail.com", "+55118763429", 4, "sendo caixa em um super mercado", 1300)
        print(pessoa.nome)
        print(pessoa.nome)
        