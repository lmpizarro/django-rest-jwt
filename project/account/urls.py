from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from account import views

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', views.CreateUserView.as_view(), name='account_create'),

]

