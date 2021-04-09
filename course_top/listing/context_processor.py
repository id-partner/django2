from .models import Category


def menu_categories(request):
    categories_menu = Category.objects.prefetch_related('child_category').filter(order=1)
    return {'categories_menu': categories_menu}
