from rest_framework import generics, authentication, permissions, mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer, AuthTokenSerializer
from .serializers import ListPizza, SizeList
from .models import PizzaTypes,Pizza_size


@api_view(['GET'])
def pizzaList(request):
    pizzas = PizzaTypes.objects.all()
    serializer = ListPizza(pizzas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pizzaDetail(request, pk):
    pizzas = PizzaTypes.objects.get(id=pk)
    serializer = ListPizza(pizzas, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def pizzaCreate(request):
    serializer = ListPizza(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def pizzaUpdate(request, pk):
    pizza = PizzaTypes.objects.get(id=pk)
    serializer = ListPizza(instance=pizza, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def pizzaDelete(request, pk):
    pizza = PizzaTypes.objects.get(id=pk)
    pizza.delete()

    return Response(serializer.data)

@api_view(['GET'])
def pizzaFilter(request,key,value):
    pizzas = []
    if key == "size":
        pizzas = PizzaTypes.objects.filter(pizza_size=value)
    elif key == "type":
        pizzas = PizzaTypes.objects.filter(pizza_type=value)
    else:
        pizzas = PizzaTypes.objects.all()
    serializer = ListPizza(pizzas, many=True)
    return Response(serializer.data)


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):

        return self.request.user



