from rest_framework import viewsets
from powerUp.models.Produto import Produto
from powerUp.serializers.produto import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
