from django.urls import path
from . import views

app_name= 'core'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('pizza-list/', views.pizzaList, name='pizzalist'),
    path('pizza-detail/<int:pk>/', views.pizzaDetail, name='pizzadetail'),
    path('pizza-create/', views.pizzaCreate, name='createpizza'),
    path('pizza-update/<str:pk>/', views.pizzaUpdate, name='updatepizza'),
    path('pizza-delete/<str:pk>/', views.pizzaDelete, name='deletepizza'),
    path('pizza-filter/<str:key>=<str:value>', views.pizzaFilter, name='filterbytype'),
]
