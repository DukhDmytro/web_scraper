import json
from django.conf import settings
from django.core.paginator import Paginator


class MyPaginator(Paginator):
    """
    Custom paginator class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def my_get_page(self, *args, **kwargs):
        """
        Get specified page and load it from json
        :param args:
        :param kwargs:
        :return:
        """
        page = super().get_page(*args, **kwargs)
        for vacancy in page:
            vacancy.description = json.loads(vacancy.description)
        return page


def make_pagination(request, to_paginate, items_per_page=settings.ITEMS_PER_PAGE):
    """
    Function to create pagination for specified object
    :param request:
    :param to_paginate: the django paginated queryset
    :param items_per_page: number of items to show on page
    :return: specified page and last page as tuple
    """
    pages = MyPaginator(to_paginate, items_per_page)
    last_page = pages.num_pages
    page = pages.my_get_page(request.GET.get('p'))
    return page, last_page
