import pytest
from libpythonpro.spam.envidor_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Junior', email='jrcidade@gmail.com'),
            Usuario(nome='Edileia', email='edileia.cidade@gmail.com')
        ],
        [
            Usuario(nome='Junior', email='jrcidade@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'edileia.cidade@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantáticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao) -> object:
    usuario = Usuario(nome='Junior', email='jrcidade@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'edileia.cidade@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantáticos'
    )
    assert enviador.parametros_de_envio == (
        'edileia.cidade@gmail.com',
        'jrcidade@gmail.com',
        'Curso Python pro',
        'Confira os módulos fantásticos'
    )
