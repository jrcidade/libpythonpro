from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Junior', email='jrcidade@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao) -> object:
    usuarios = [Usuario(nome='Junior', email='jrcidade@gmail.com'),
                Usuario(nome='Edileia', email='edileia.cidade@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()