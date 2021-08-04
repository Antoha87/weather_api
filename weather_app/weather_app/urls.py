"""weather_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from weather.views import WeatherViewSet
from relations.views import CategoryViewSet
from relations.views import GoodsViewSet
from relations.views import CartViewSet
from relations.views import CreateCartViewSet
from relations.views import TagViewSet
from currency.views import CryptoDataViewSet
from currency.views import CryptoViewSet
from currency.views import CurrencyAverageViewSet
from currency.views import currency_sum
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

Router = routers.DefaultRouter()
Router.register('weather', WeatherViewSet)
Router.register('category', CategoryViewSet)
Router.register('goods', GoodsViewSet)
Router.register('cart', CartViewSet, 'Cart')
Router.register('create_cart', CreateCartViewSet)
Router.register('tag', TagViewSet)
Router.register('crypto_data', CryptoDataViewSet)
Router.register('crypto', CryptoViewSet)
Router.register('currency_average', CurrencyAverageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(Router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('api/sum_of_currencies/', currency_sum),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
