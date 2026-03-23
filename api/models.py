from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()

    def __str__(self):
        return self.titulo

class Matricula(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_matricula = models.DateField(auto_now_add=True)
