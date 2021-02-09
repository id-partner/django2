from .models import Category


def menu_categories(request):
    categories_menu = Category.objects.prefetch_related('parent_category').filter(parent_id__isnull= True)
    return {'categories_menu': categories_menu}
