from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128)

    def serialize_hook(self, hook):
        # optional, there are serialization defaults
        # we recommend always sending the Hook
        # metadata along for the ride as well
        print("ESTOU AQUI")
        return {
            'hook': hook.dict(),
            'data': {
                'id': self.id,
                'name': self.nome,
            }
        }
