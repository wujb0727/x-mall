"""xmall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/api-token-auth/', obtain_auth_token),  # DRF   token认证
    path('api/jwt-auth/', obtain_jwt_token, name='jwt-token'),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # 后台富文本编辑器上传图片
    path('api-auth/', include('rest_framework.urls')),
    path('api/user/', include(('account.urls', 'account'), namespace='accounts')),
    path('api/goods/', include(('goods.urls', 'goods'), namespace='goods')),
    path('api/home/', include(('home.urls', 'home'), namespace='home')),
    path('api/address/', include(('address.urls', 'address'), namespace='address')),
    path('api/cart/', include(('cart.urls', 'cart'), namespace='carts')),
    path('api/order/', include(('order.urls', 'order'), namespace='orders')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
