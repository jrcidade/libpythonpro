from libpythonpro.spam.envidor_de_email import Enviador

def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None

def test_remetente():
    enviador= Enviador()
    resultado = enviador.enviar(
        'jrcidade@gmail.com',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert 'jrcidade@gmail.com' in resultado