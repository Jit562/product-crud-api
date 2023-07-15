from django.urls import path
from prod.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('product/', ProductAdd.as_view(), name='product'),
    path('product/details/', ProductViews.as_view(), name='product'),
    path('product/details/<int:pk>/', ProductDetail.as_view()),
    
    path('', Registerdemo.as_view()),
    
]
