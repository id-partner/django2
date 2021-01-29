from django.core.management.base import BaseCommand
from listing.crawlers.tutortop_crawler import crawl_school, crawl_course


class Command(BaseCommand):
    help = 'Запуск парсинга листинга курсов'

    def handle(self, *args, **options):
        # # добавление школ. Медленно.
        url = 'https://tutortop.ru/school-list/'
        crawl_school(url)

        # добавление курсов
        url_cat = [
            'https://tutortop.ru/courses_selection/kursy_po_reklame_u_blogerov/',
            'https://tutortop.ru/courses_selection/kursy_direktorov_po_marketingu/',
            'https://tutortop.ru/courses_selection/kursy_po_internet_marketingu/',
            'https://tutortop.ru/courses_selection/kursy_po_razrabotke_igr/',
            'https://tutortop.ru/courses_selection/kursy_po_web_dizajnu/'
        ]

        for url in url_cat:
            crawl_course(url)
