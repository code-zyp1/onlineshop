from django.shortcuts import render

# Create your views here.
from goods.serializers import GoodsSerializer,CategorySerializer
from .models import Goods,GoodsCategory
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .filters import GoodsFilter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView):
#     '商品列表页'
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
# class GoodsListView(generics.ListAPIView):
#     '商品列表页'
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 10
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100



class GoodsListViewSet(viewsets.ModelViewSet):
    '''
    list:商品列表,分页，搜索

    retrieve:
    获取详情

    '''

    # 分页
    pagination_class = GoodsPagination
    #这里必须要定义一个默认的排序,否则会报错
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('=name', 'is_new')
    #排序
    ordering_fields = ('sold_num','add_time')


class CategoryViewSet(viewsets.ModelViewSet):
    """
    list:商品分类列表数据
    """

    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer