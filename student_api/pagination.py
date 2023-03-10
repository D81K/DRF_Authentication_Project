# from rest_framework import pagination
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class SmallPageNumberPagination(PageNumberPagination):
    page_size = 8
    page_query_param = 'sayfa'
    max_page_size = 15


class LargePageNumberPagination(PageNumberPagination):
    page_size = 5
    # page_query_param = 'sayfa'


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    # limit_query_param = 'sayfadaki_eleman_sayisi'  # defaults to "limit"
    # offset_query_param = "baslangic"  # defaults to `offset`

class MyCursorPagination(CursorPagination):
    ordering = "createdDate"
    page_size = 10