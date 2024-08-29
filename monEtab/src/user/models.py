from django.db import models

# Create your models here.
class User(models.Model):
    pseudo_name = models.CharField(max_length=30)
    pass_word = models.CharField(max_length=12)
    creat_at = models.DateField(auto_now_add=True)

    def __get__(self):
        return self.pass_word

    class Meta:

        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
