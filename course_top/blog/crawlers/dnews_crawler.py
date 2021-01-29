from requests_html import HTMLSession
from datetime import datetime
from slugify import slugify
from django.utils.timezone import make_aware

from concurrent.futures import ThreadPoolExecutor

from blog.models import *

posts = []


def crawl_one(url):
    with HTMLSession() as session:
        response = session.get(url)

    name = response.html.xpath('//div[@class="entry-header"]/h1')[0].text
    content = response.html.xpath('//div[@class="js-mediator-article"]//p')
    image_url = response.html.xpath('//div[@class="js-mediator-article"]//img/@src')[0]
    pub_date = response.html.xpath('//div[@class="entry-info"]/span[@class="entry-date"]/@content')[0]

    my_content = ''
    short_description = ''
    for element in content:
        my_content += f'<{element.tag}>' + element.text + f'<{element.tag}>'
        if len(short_description) < 200:
            short_description += element.text + ' '

    image_name = slugify(name)
    img_type = image_url.split('.')[-1]

    img_path = f'images/post/{image_name}.{img_type}'

    with open(f'media/{img_path}', 'wb') as f:
        with HTMLSession() as session:
            response = session.get(image_url)
            f.write(response.content)

    pub_date = datetime.strptime(pub_date.split('+')[0], '%Y-%m-%dT%H:%M:%S')

    post = {
        'name': name,
        'slug': slugify(name),
        'content': my_content,
        'short_description': short_description.strip(),
        'main_image': img_path,
        'pub_date': make_aware(pub_date),
    }

    # post, created = Post.objects.get_or_create(**post)

    post = Post(**post)
    posts.append(post)

    print(post)


def get_urls():
    base_url = 'https://3dnews.ru/tags/%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5'
    with HTMLSession() as session:
        response = session.get(base_url)

    links = response.html.xpath('//a[@class="entry-header"]/@href')

    urls_news = ['https://3dnews.ru' + lnk for lnk in links]

    return urls_news


def run():
    # удаление всех статей
    # Post.objects.all().delete()

    urls_news = get_urls()

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(crawl_one, urls_news)

    Post.objects.bulk_create(posts)
