from django.core.management.base import BaseCommand
from listing.crawlers.crawler_tutortop import crawl_course


class Command(BaseCommand):
    help = 'Запуск парсинга листинга курсов'

    def handle(self, *args, **options):
        # добавление курсов
        url_cat = [
            'https://tutortop.ru/courses_selection/kursy_po_web_dizajnu/',
            'https://tutortop.ru/courses_selection/kursy_po_graficheskomu_dizajnu/',
            'https://tutortop.ru/courses_selection/ux-ui/',
            'https://tutortop.ru/courses_selection/kursy_po_3d_modelirovaniyu/',
            'https://tutortop.ru/courses_selection/kursy_po_dizajnu_intererov/',
            'https://tutortop.ru/courses_selection/kursy_po_sozdaniyu_illyustracij/',
            'https://tutortop.ru/courses_selection/kursy_po_montazhu_video/',
            'https://tutortop.ru/courses_selection/kursy_po_adobe_photoshop/',
            'https://tutortop.ru/courses_selection/3d-max/',
            'https://tutortop.ru/courses_selection/kursy_po_motion_dizajnu/',
            'https://tutortop.ru/courses_selection/kursy_gejmdizajna/',
            'https://tutortop.ru/courses_selection/kursy_po_3d_animaciya/',
            'https://tutortop.ru/courses_selection/kursy_po_dizajnu_mobilnyh_prilozhenij/',
            'https://tutortop.ru/courses_selection/kursy_po_sketchingu/',
            'https://tutortop.ru/courses_selection/landshaftnyj-dizajn/',
            'https://tutortop.ru/courses_selection/figma/',
            'https://tutortop.ru/courses_selection/illustrator/',
            'https://tutortop.ru/courses_selection/landing/',
            'https://tutortop.ru/courses_selection/autocad/',
            'https://tutortop.ru/courses_selection/after-effects/',
            'https://tutortop.ru/courses_selection/kursy_upravleniyu_v_dizajne/',
            'https://tutortop.ru/courses_selection/kursy_po_tipografike/',
        ]

        for url in url_cat:
            crawl_course(url)
