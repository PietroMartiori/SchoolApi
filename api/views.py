from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Estudante, Curso, Matricula
from .serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer


class EstudanteViewSet(ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [OrderingFilter]
    ordering_fields = ['nome', 'email']


class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [OrderingFilter]
    ordering_fields = ['nome']


class MatriculaViewSet(ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['estudante', 'curso']
    ordering_fields = ['id']