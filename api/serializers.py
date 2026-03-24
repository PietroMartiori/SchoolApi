from rest_framework import serializers
from .models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'

    def validate_cpf(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("CPF deve ter apenas numeros")

        if len(value) != 11:
            raise serializers.ValidationError("CPF deve ter 11 digitos")

        return value


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
    def validate_carga_horaria(self, value):
        if value <= 0:
            raise serializers.ValidationError("Carga horaria deve ser positiva")
        return value

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'