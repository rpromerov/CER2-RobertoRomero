from django.db import models

roles = [("0", "Estudiante"), ("1", "Profesor")]


# Usuario
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=roles)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre


# Proyecto
class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tema = models.CharField(max_length=50)
    estudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="estudiante_proyecto")
    profesor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name="profesor_proyecto")

    def __str__(self) -> str:
        return self.nombre
