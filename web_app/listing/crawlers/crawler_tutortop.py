from requests_html import HTMLSession
from datetime import datetime
from slugify import slugify

from listing.models import School, Course, Category, CourseFormat


def crawl_school(url):
    """
    Парсинг школ
    :param url: сслыка на страницу со школами
    """

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
        try:
            school = School.objects.get(slug=slugify(name))
            school.description = description
            school.link = link
            school.logo = img_path
            school.save()
            print(f'Обновили данные {school}')
        except:
            school, created = School.objects.get_or_create(**school)
            print(f'Добавили новую школу {school}')


        i += 1


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
        link = 'https://' + link.split("https://")[-1].split("http://")[-1].split("&")[0].split("'")[0].split("?")[0]
    except:
        link = 'https://' + link.split("https://")[-1].split("http://")[-1].split("'")[0].split("?")[0]

    return link


def crawl_course(url):
    """
    Прасинг курсов со страницы отдельной категории с блока "Эти же курсы, но подробнее"
    :param url: Страница со списком курсов отдельной категории
    """

    with HTMLSession() as session:
        response = session.get(url)

    content = response.html
    category_name = content.xpath('(//div[@class="breadcrumbs"]//span)[3]')[0].text
    categories = category_name.split(' / ')

    if len(categories) == 1:
        category = {
            'name': categories[0],
            'slug': slugify(categories[0])
        }
        category, created = Category.objects.get_or_create(**category)
    elif len(categories) == 2:
        parent_category = {
            'name': categories[0],
            'slug': slugify(categories[0])
        }
        parent_category, created = Category.objects.get_or_create(**parent_category)

        category = {
            'name': categories[1],
            'slug': slugify(categories[1]),
            'parent':  parent_category,
            'order': 2
        }
        category, created = Category.objects.get_or_create(**category)

    count = len(content.xpath("//div[@class='course']//div[contains(@class, 'course__wrap__box post')]"))
    i = 0
    i_format = 1

    while i < count:
        school_name = content.xpath("//div[@class='course']//a[contains(@class, 'school_name')]")[i].text
        try:
            school = School.objects.get(name=school_name)
        except:
            school = {
                'name': school_name,
                'slug': slugify(school_name),
                'logo': 'images/school/nologo.png'
            }
            school,  created = School.objects.get_or_create(**school)

        name = content.xpath("//div[@class='course']//h2")[i].text

        link = get_link_course(
            content.xpath("//div[@class='course']//div[@class='course__wrap__box__btn']//a/@href")[i]
        )
        print(link)

        price = content.xpath("//div[contains(@class,'course__wrap__box post')]/@data-price")[i]
        deferred_price = content.xpath("//div[contains(@class,'course__wrap__box post')]/@data-rassrochka")[i]
        if int(deferred_price) == 1:
            deferred_price = None
        duration = content.xpath("//div[contains(@class,'course__wrap__box post')]/@data-dlitelnost")[i]
        try:
            start_date = datetime.fromtimestamp(
                int(content.xpath("//div[contains(@class,'course__wrap__box post')]/@data-date"
                                  )[i])).strftime("%Y-%m-%d")
            if start_date == '1970-01-01':
                start_date = None
        except:
            start_date = None
        try:
            course_format = content.xpath(f"(//div[@class='course']//div[@class='clock__box'])[{i_format}]/p[@class='book']")[0].text
            course_format_list = course_format.replace('Формат: ', '').split(', ')
        except:
            course_format_list = None

        course = {
            'name': name,
            'link': link,
            'description': name,
            'price': price,
            'deferred_price': deferred_price,
            'duration': duration,
            'start_date': start_date,
            'school': school
        }

        try:
            course = Course.objects.get(name=name, school=school)
            course.price = price
            course.start_date = start_date
            course.deferred_price = deferred_price
            course.link = link
            course.save()
        except Course.DoesNotExist:
            course, created = Course.objects.get_or_create(**course)

        course.categories.add(category)

        try:
            for course_format in course_format_list:
                course_format, created = CourseFormat.objects.get_or_create(name=course_format)
                course.course_format.add(course_format)
        except:
            pass



        print(course)

        i += 1
        i_format += 1
