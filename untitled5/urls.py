"""untitled5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import xadmin
from django.urls import path,include,re_path
from goods.views import CategoryViewSet,GoodsListViewSet
from user_operation.views import UserFavViewset
from users.views import SmsCodeViewset,UserViewset
from user_operation.views import LeavingMessageViewset,AddressViewset
from trade.views import ShoppingCartViewset,OrderViewset

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()

router.register(r'goods',GoodsListViewSet,basename='goods')
router.register(r'categorys',CategoryViewSet,basename='categorys')
router.register(r'userfavorite',UserFavViewset,basename='userfavorite')
router.register(r'code',SmsCodeViewset,basename='code')
router.register(r'users', UserViewset, basename="users")
router.register(r'messages', LeavingMessageViewset, basename="messages")
router.register(r'address',AddressViewset , basename="address")
router.register(r'shopcarts', ShoppingCartViewset, basename="shopcarts")
router.register(r'orders', OrderViewset, basename="orders")


urlpatterns = [
    re_path('',include(router.urls)),
    path('admin/', xadmin.site.urls),
    path('ueditor/',include('DjangoUeditor.urls')),
    path('api-auth/',include('rest_framework.urls')),
    #path('goods/',GoodsListView.as_view(),name='goods-list'),
    path('docs',include_docs_urls(title='电商平台学习测试使用')),
    path('api-token-auth/',views.obtain_auth_token),
    #jwt的认证接口
    path('login/',obtain_jwt_token),

]