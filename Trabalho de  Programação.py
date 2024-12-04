class Disciplina:
    def init(self, id: int, descricao: str, segmento: str, professor_titular: 'Professor'):
        self.__id = id
        self.__descricao = descricao
        self.__segmento = segmento
        self.__professor_titular = professor_titular

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("ID deve ser um inteiro.")
        self.__id = value

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, value):
        if not isinstance(value, str):
            raise TypeError("Descrição deve ser uma string.")
        self.__descricao = value

    @property
    def segmento(self):
        return self.__segmento

    @segmento.setter
    def segmento(self, value):
        if not isinstance(value, str):
            raise TypeError("Segmento deve ser uma string.")
        self.__segmento = value

    @property
    def professor_titular(self):
        return self.__professor_titular

    @professor_titular.setter
    def professor_titular(self, value):
        if not isinstance(value, 'Professor'):
            raise TypeError("Professor titular deve ser um objeto Professor.")
        self.__professor_titular = value


class Professor:
    def init(self, nome: str, sobrenome: str, cpf: str, endereco_residencial: str, formacao: str, disciplinas: List[Disciplina], segmentos: List[str]):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__endereco_residencial = endereco_residencial
        self.__formacao = formacao
        self.__disciplinas = disciplinas
        self.__segmentos = segmentos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        if not isinstance(value, str):
            raise TypeError("Nome deve ser uma string.")
        self.__nome = value

    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, value):
        if not isinstance(value, str):
            raise TypeError("Sobrenome deve ser uma string.")
        self.__sobrenome = value

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        if not isinstance(value, str):
            raise TypeError("CPF deve ser uma string.")
        self.__cpf = value

    @property
    def endereco_residencial(self):
        return self.__endereco_residencial

    @endereco_residencial.setter
    def endereco_residencial(self, value):
        if not isinstance(value, str):
            raise TypeError("Endereço residencial deve ser uma string.")
        self.__endereco_residencial = value

    @property
    def formacao(self):
        return self.__formacao

    @formacao.setter
    def formacao(self, value):
        if not isinstance(value, str):
            raise TypeError("Formação deve ser uma string.")
        self.__formacao = value

    @property
    def disciplinas(self):
        return self.__disciplinas

    @disciplinas.setter
    def disciplinas(self, value):
        if not isinstance(value, list):
            raise TypeError("Disciplinas deve ser uma lista.")
        self.__disciplinas = value

    @property
    def segmentos(self):
        return self.__segmentos

    @segmentos.setter
    def segmentos(self, value):
        if not isinstance(value, list):
            raise TypeError("Segmentos deve ser uma lista.")
        self.__segmentos = value


class Turma:
    def init(self, nome, segmento_ensino, opcao_curso, ano_escolar, alunos, professores, disciplinas):
        self.__nome = nome
        self.__segmento_ensino = segmento_ensino
        self.__opcao_curso = opcao_curso
        self.__ano_escolar = ano_escolar
        self.__alunos = alunos
        self.__professores = professores
        self.__disciplinas = disciplinas

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def str(self):
        return f"Turma: {self._nome} - Segmento: {self._segmento_ensino}

        class Aluno:
    def init(self, primeiro_nome, sobrenome, endereco_residencial, filiacao, email_responsavel, ra, segmento_ensino, turma, nome_usuario, email, senha):
        self.__primeiro_nome = primeiro_nome
        self.__sobrenome = sobrenome
        self.__endereco_residencial = endereco_residencial
        self.__filiacao = filiacao
        self.__email_responsavel = email_responsavel
        self.__ra = ra
        self.__segmento_ensino = segmento_ensino
        self.__turma = turma
        self.__nome_usuario = nome_usuario
        self.__email = email
        self.__senha = senha

    @property
    def primeiro_nome(self):
        return self.__primeiro_nome

    @primeiro_nome.setter
    def primeiro_nome(self, primeiro_nome):
        self.__primeiro_nome = primeiro_nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    def str(self):
        return f""Aluno: {self.primeiro_nome} {self.sobrenome} - RA: {self.__ra}"

class Gerenciador:
           
     def init(self):
        self.__alunos = []
        self.__professores = []
        self.__disciplinas = []
        self.__turmas = []

def cadastrar_aluno(self, aluno):
        self.__alunos.append(aluno)

def remover_aluno(self, ra):
        self._alunos = [aluno for aluno in self._alunos if aluno.ra != ra]

def buscar_aluno(self, ra):
        for aluno in self.__alunos:
            if aluno.ra == ra:
                return aluno
        return None
def cadastrar_professor(self, professor):
        self.__professores.append(professor)

def remover_professor(self, cpf):
        self._professores = [professor for professor in self._professores if professor.cpf != cpf]

def buscar_professor(self, cpf):
        for professor in self.__professores:
            if professor.cpf == cpf:
                return professor
        return None

def cadastrar_disciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

def remover_disciplina(self, id):
        self._disciplinas = [disciplina for disciplina in self._disciplinas if disciplina.id != id]

def buscar_disciplina(self, id):
        for disciplina in self.__disciplinas:
            if disciplina.id == id:
                return disciplina
        return None

def cadastrar_turma(self, turma):
        self.__turmas.append(turma)

def remover_turma(self, nome):
        self._turmas = [turma for turma in self._turmas if turma.nome != nome]

def buscar_turma(self, nome):
        for turma in self.__turmas:
            if turma.nome == nome:
                return turma
        return None