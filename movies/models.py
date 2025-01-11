from django.db import models

# Create your models here.
from django.db import models

class Trainer (models.Model):
    name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    year = models.IntegerField(default=1)
    date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    
    def __str__(self):
        return f"{self.name} {self.last_name}"

class movies (models.Model):
    name = models.CharField(max_length=30, null=False)
    MOVIES_TYPES = {
        ('A', 'Accion'),
        ('F', 'Familiar'),
        ('T', 'Terror'),
        ('U', 'Urbano'),
        ('E', 'Explisito'),
        ('D', 'Documental'),
    }
    id = models.CharField(max_length=30, choices=MOVIES_TYPES, null=False)
    title = models.DecimalField(decimal_places=4, max_digits=6)
    gender = models.DecimalField(decimal_places=4, max_digits=6)
    director = models.ForeignKey(user, on_delete=models.SET_NULL, null=True) # type: ignore
    year = models.DecimalField(decimal_places=4, max_digits=6)
    sinopsis = models.ForeignKey(user, on_delete=models.SET_NULL, null=True) # type: ignore
    picture = models.ImageField(upload_to="pokemon_images")
    
    def __str__(self):
        return self.name