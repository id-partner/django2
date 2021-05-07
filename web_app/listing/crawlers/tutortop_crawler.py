from requests_html import HTMLSession
from datetime import datetime
from slugify import slugify

from listing.models import School, Course, Category


def crawl_school(url):
    """
    Парсинг школ
    :param url: сслыка на страницу со школами
    """
    schools = []

    with HTMLSession() as session:
        response = session.get(url)

    content = response.html

    count = len(content.xpath('//div[@class="list-item-content-text"]'))
    i = 0

    while i < count:
        print(i)

        description = content.xpath('//div[@class="list-item-content-text"]')[i].text
        logo = content.xpath('//div[contains(@class, "reviews-list-item-header")]//img/@src')[i]
        link = content.xpath('//div[@class="list-item-header-left"]/a[@class="list-item-url"]')[i].text
        review_page = content.xpath('//div[@class="list-item-header-right"]/a[@class="open-review-page"]/@href')[i]
        name = name_school(review_page)

        image_name = slugify(name)
        img_type = logo.split('.')[-1]

        img_path = f'images/school/{image_name}.{img_type}'

        with open(f'media/{img_path}', 'wb') as f:
            with HTMLSession() as session:
                response = session.get(logo)
                f.write(response.content)

        school = {
            'description': description,
            'link': link,
            'name': name,
            'slug': slugify(name),
            'logo': img_path
        }

        school = School(**school)
        schools.append(school)

        i += 1

    School.objects.bulk_create(schools)


def name_school(url):
    """

    :param url: сслыка на страницу со школой
    :return: Имя школы
    """

    with HTMLSession() as session:
        response = session.get(url)

    name = response.html.xpath('//h1')[0].text

    return name


def get_link_course(url):
    """
    Получаем ссылку на курс на сайте школы
    :param url: Ссылка на курс на сайте
    :return: Ссылка на курс на сайте школы
    """
    with HTMLSession() as session:
        r = session.get(url)

    link = r.html.xpath('//script')[2].text

    try:
        link = 'https://' + link.split("https://")[-1].split("&")[0].split("'")[0]
    except:
        link = 'https://' + link.split("https://")[-1].split("'")[0]

    return link


def crawl_course(url):
    """
    Прасинг курсов со страницы отдельной категории
    :param url: Страница со списком курсов отдельной категории
    """

    with HTMLSession() as session:
        response = session.get(url)

    content = response.html
    category_name = content.xpath('//span[@class="breadcrumb_last"]')[0].text

    category = {
        'name': category_name,
        'slug': slugify(category_name)
    }
    category, created = Category.objects.get_or_create(**category)

    count = len(content.xpath("//div[contains(@class, 'm-course-name-link')]"))
    i = 0

    while i < count:
        name = content.xpath("//div[contains(@class, 'm-course-name-link')]")[i].text.replace(' Ссылка на курс',
                                                                                              '')
        link = get_link_course(
            content.xpath('//div[contains(@class, "m-course-name-link")]/a[@class="tab-link-course"]/@href')[i])
        price = content.xpath('//div[@class="tab-course-col tab-course-col-flex tab-course-col-price"]/span')[i] \
            .text.replace(' ', '').replace('₽', '')
        duration = content. \
            xpath('//div[@class="tab-course-col tab-course-col-flex tab-course-col-dlitelnost"]/@data-dlitelnost')[i]
        try:
            start_date = datetime.fromtimestamp(int(
                content.xpath(
                    "//div[@class='tab-course-col tab-course-col-date-t tab-course-col-date']/@data-date")[
                    i])).strftime("%Y-%m-%d")
        except:
            start_date = None

        school_name = \
            content.xpath('//div[@class="m-course-price-details"]//a[@class="course__col_school_name"]')[
                i].text
        try:
            school = School.objects.get(name=school_name)
        except:
            # просто костыль для теста
            school = School.objects.get(id=3)

        course = {
            'name': name,
            'link': link,
            'description': name,
            'price': price,
            'duration': duration,
            'start_date': start_date,
            'school': school
        }

        course, created = Course.objects.get_or_create(**course)
        course.categories.add(category)

        print(name)
        i += 1


"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school_courses', verbose_name='Школа')
    categories = models.ManyToManyField(Category, verbose_name='Категория')
"""
