class Aluno:
    universidade = 'UniGrande'

    def __init__(self, matricula: int, nome:str) -> None:
        self.matricula = matricula
        self.nome = nome
        self.creditos_cursados = 0
        self.mgp = 0.0

    def apresentar(self):
        return f'{self.matricula} - {self.nome}'

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor) -> None:
        valor = valor.strip()
        if len(valor) < 3:
            raise ValueError('Nome Inválido')
        self._nome = valor

    @property
    def mgp(self) -> float:
        return self._mgp

    @mgp.setter
    def mgp(self, valor: float) -> None:
        if not 0 <= valor <= 10:
            raise ValueError('MGP deve estar entre 0 e 10')
        self._mgp = valor

class Professor:

    def __init__(self, matricula:int, nome:str, email:str):
        self.matricula = matricula
        self.nome = nome
        self.email = email

    def apresentar_professor(self):
        return f'{self.matricula} - {self.nome} - {self.email}'

class Curso:

    def __init__(self, codigo:int, nome:str, total_creditos:int):
        self.codigo = codigo
        self.nome = nome
        self.total_creditos = total_creditos

aluno_1 = Aluno(20260001, 'David Leite')
aluno_2 = Aluno(20260002, 'Carlinhos Maia')

print(aluno_1.apresentar())
print(aluno_2.apresentar())

professor_1 = Professor(3370001, 'Igor Ramon', 'Iguinhomataporco@gmail.com')
professor_2 = Professor(3370002, 'Ana Castela', 'Anacastela.oficial@gmail.com')

print(professor_1.apresentar_professor())
print(professor_2.apresentar_professor())

curso_1 = Curso(4340, 'Enfermagem', '40')
curso_2 = Curso(2530, 'Análise e Desenvolvimento de Sistemas', '40')

