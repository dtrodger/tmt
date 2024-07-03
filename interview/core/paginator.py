from rest_framework.pagination import LimitOffsetPagination


class ThreeItemPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 3
