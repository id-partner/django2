from django import template
register = template.Library()


@register.filter
def rupluralize(value, arg="дурак,дурака,дураков"):
    """
    :param value: число
    :param arg: слово в именительном, винительный ед.число, винительный мн.число
    :return: слово в нужном падеже
    """
    args = arg.split(",")
    number = abs(int(value))
    a = number % 10
    b = number % 100

    if (a == 1) and (b != 11):
        return args[0]
    elif (a >= 2) and (a <= 4) and ((b < 10) or (b >= 20)):
        return args[1]
    else:
        return args[2]


@register.filter
def rating_percentages(value, cnt_rating):
    """
    Отдает процент, который используется для отрисовки прогресс бара

    :param value: общее количесвто отзывов
    :param cnt_rating: количество отзывов по конкретному кол-ву звезд
    :return: округленный процент
    """
    a = cnt_rating / value * 100
    return round(a)
