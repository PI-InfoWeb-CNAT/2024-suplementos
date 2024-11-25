from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .Carrinho import Carrinho
from .Cliente import Cliente
from .Produto import Produto
from .Endereco import Endereco
from .Notificacao import Notificacao