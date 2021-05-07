from django.core.management.base import BaseCommand
from blog.crawlers.dnews_crawler import run


class Command(BaseCommand):
    help = 'Запуск парсинга новостей.ru'

    def handle(self, *args, **options):
        run()
