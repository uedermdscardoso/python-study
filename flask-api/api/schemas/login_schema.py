#Como o Model tarefa está funcionando
from api import marshmallow
from api.models import usuario_model
from marshmallow import fields

#Serializer
class LoginSchema(marshmallow.ModelSchema):
    class Meta:
        model = usuario_model.Usuario
        fields = ( 'id', 'nome', 'email', 'senha' )

    #Regras de validação
    nome = fields.String(required=False)
    email = fields.String(required=True)
    senha = fields.String(required=True)