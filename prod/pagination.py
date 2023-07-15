from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'record'
    page_query_param = 'p'
    max_page_size = 15
    last_page_strings = 'end'