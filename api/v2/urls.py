from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet

router = DefaultRouter()
router.register(r'estudantes', EstudanteViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'matriculas', MatriculaViewSet)

urlpatterns = router.urls