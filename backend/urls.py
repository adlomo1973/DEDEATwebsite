from django.urls import path
from . import views

urlpatterns = [
    # API endpoints
    path('api/v1/resource/', views.ResourceList.as_view(), name='resource-list'),
    path('api/v1/resource/<int:pk>/', views.ResourceDetail.as_view(), name='resource-detail'),

    # JWT Authentication endpoints
    path('api/v1/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]