from rest_framework.pagination import *

class MyPagination(PageNumberPagination):
    page_size = 3
    page_query_description = 'p'
    page_size_query_param = 'num'
