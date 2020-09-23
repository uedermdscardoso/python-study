from ..models import usuario_model
from api import db

def cadastrarUsuario(usuario):
    usuario_bd = usuario_model.Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
    usuario_bd.gen_senha()
    db.session.add(usuario_bd)
    db.session.commit();
    return usuario_bd

def listarUsuarioPorEmail(email):
    return usuario_model.Usuario.query.filter_by(email = email).first()