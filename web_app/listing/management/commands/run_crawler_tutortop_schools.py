from django.core.management.base import BaseCommand
from listing.crawlers.crawler_tutortop import crawl_school


class Command(BaseCommand):
    help = 'Запуск парсинга школ'

    def handle(self, *args, **options):
        url = 'https://tutortop.ru/school-list/'
        crawl_school(url)
