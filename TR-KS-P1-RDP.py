class Disciplina:
	def __init__(self, id: int, descricao: str, segmento: str, professor_titular: 'Professor'):
		self.id = id
		self.descricao = descricao
		self.segmento = segmento
		self.professor_titular = professor_titular

	def editar_descricao(self, nova_descricao: str):
		if not nova_descricao.strip():
			raise ValueError("A descrição não pode ser vazia.")
		self.descricao = nova_descricao

	def desativar(self):
		"""Desativa a disciplina removendo o segmento."""
		self.segmento = None

	def __str__(self):
		return f"Disciplina(ID: {self.id}, Descrição: {self.descricao}, Segmento: {self.segmento})"


class Professor:
	def __init__(self, primeiro_nome: str, sobrenome: str, cpf: str, email: str, disciplinas: list = None):
		self.primeiro_nome = primeiro_nome
		self.sobrenome = sobrenome
		self.cpf = cpf  # Usa o setter para validar o CPF
		self.email = email
		self.disciplinas = disciplinas if disciplinas else []
	
	@property
	def cpf(self):
		return self.__cpf

	@cpf.setter
	def cpf(self, novo_cpf: str):
		if len(novo_cpf) != 11 or not novo_cpf.isdigit():
			raise ValueError("CPF inválido. Deve conter 11 dígitos numéricos.")
		self.__cpf = novo_cpf

	def adicionar_disciplina(self, disciplina: Disciplina):
		self.disciplinas.append(disciplina)

	def __str__(self):
		return f"Professor: {self.primeiro_nome} {self.sobrenome}, Email: {self.email}"


class Estudante:
	def __init__(self, primeiro_nome: str, sobrenome: str, ra: str, segmento: str, turma: str = None):
		self.primeiro_nome = primeiro_nome
		self.sobrenome = sobrenome
		self.ra = ra  # Usa o setter para validar o RAself.segmento = segmentoself.turma = turma

	@property
	def ra(self):
		return self.__ra

	@ra.setter
	def ra(self, novo_ra: str):
		if not novo_ra.isdigit():
			raise ValueError("O RA deve ser numérico.")
		self.__ra = novo_ra

	def transferir_turma(self, nova_turma: str):
		if not nova_turma:
			raise ValueError("A turma não pode ser vazia.")
		self.turma = nova_turma

	def __str__(self):
		return f"Estudante: {self.primeiro_nome} {self.sobrenome}, RA: {self.ra}, Segmento: {self.segmento}"


class Turma:
	MAX_ALUNOS_EM = 20
	MAX_ALUNOS_SUPERIOR = 5

	def __init__(self, nome: str, segmento: str, opcao_curso: str, ano_escolar: int):
		self.nome = nome
		self.segmento = segmento
		self.opcao_curso = opcao_curso
		self.ano_escolar = ano_escolar
		self.alunos = []
		self.professores = []

	def adicionar_aluno(self, aluno: Estudante):
		if self._excede_limite_alunos():
			raise ValueError(self._mensagem_erro_limite())
		self.alunos.append(aluno)

	def _excede_limite_alunos(self):
		"""Verifica se a turma excedeu o limite de alunos dependendo do segmento."""
		if self.segmento == "EM" and len(self.alunos) >= Turma.MAX_ALUNOS_EM:
			return True
		if self.segmento == "Superior" and len(self.alunos) >= Turma.MAX_ALUNOS_SUPERIOR:
			return True
		return False

	def _mensagem_erro_limite(self):
		"""Mensagem de erro dependendo do segmento da turma."""
		if self.segmento == "EM":
			return "Turma de Ensino Médio não pode exceder 20 alunos."
		return "Turma de Ensino Superior não pode exceder 5 alunos."

	def __str__(self):
		return f"Turma: {self.nome}, Segmento: {self.segmento}, Curso: {self.opcao_curso}, Ano: {self.ano_escolar}"
