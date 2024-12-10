from loja.models import *

class Cliente(models.Model):
    PERFIL = [
        ('admin', 'Admin'),
        ('user', 'Usuário')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    perfil = models.CharField(null=False, max_length=10, choices=PERFIL, default='user')
    nome = models.CharField(null=False, max_length=100)
    cpf = models.CharField(null=False, max_length=11, unique=True)
    telefone_celular = models.CharField(null=False, max_length=11)

    def __str__(self):
        return f'{self.nome}'
    
    @receiver(post_save, sender=User)
    def create_user_usuario(sender, instance, created, **kwargs):
        try:
            if created:
                Cliente.objects.create(user=instance)
        except:
            pass
    
    @receiver(post_save, sender=User)
    def save_user_usuario(sender, instance, **kwargs):
        try:
            instance.usuario.save()
        except:
            pass

    def delete(self, *args, **kwargs):
        self.user.delete()  
        super().delete(*args, **kwargs)  
