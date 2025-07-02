from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from powerUp.views.ProdutoView import ProdutoViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # isso expõe /produtos/
]
