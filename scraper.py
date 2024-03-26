import os
import django
import requests
from bs4 import BeautifulSoup

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "articles_scraper.settings")
django.setup()

from articles.models import Article

def check_for_duplicate(url):
    """
    Check if an article with the given URL already exists in the database.
    """
    return Article.objects.filter(url=url).exists()


url = 'https://hongkongfp.com/'

response = requests.get(url)
if response.status_code == 200:
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    news = soup.find('div', class_='wp-block-columns alignwide is-style-first-col-to-second is-layout-flex wp-container-core-columns-layout-1 wp-block-columns-is-layout-flex').find_all('article')

    for n in news:
        try:
            start = len('https://hongkongfp.com/')
            article_data = {
                'title': n.find('h2', class_='entry-title').find('a').text,
                'url': n.find('h2', class_='entry-title').find('a')['href'],
                'pub_date': n.find('h2', class_='entry-title').find('a')['href'][start:start+10],
            }

            # Check for the presence of the subtitle
            author = n.find('span', class_='author vcard').find('a')
            if author:
                article_data['author'] = author.text
            else:
                article_data['author'] = ''

            # Check for the presence of the subtitle
            subtitle = n.find('div', class_='newspack-post-subtitle newspack-post-subtitle--in-homepage-block')
            if subtitle:
                article_data['short_desc'] = subtitle.text
            else:
                article_data['short_desc'] = ''

            # Get image URL
            try:
                img = n.find('figure', class_='post-thumbnail').find('a', {'rel': 'bookmark'}).find('img')
                if img.has_attr('data-src'):
                    article_data['image_url'] = img['data-src']
                else:
                    article_data['image_url'] = img['src']
            except AttributeError:
                article_data['image_url'] = ''

            # Fetch article content
            article_url = article_data['url']
            
            if check_for_duplicate(article_url):
                print(f"Skipping duplicate article: {article_url}")
                continue

            response_article = requests.get(article_url)
            if response_article.status_code == 200:
                parsed_html = BeautifulSoup(response_article.content, 'html.parser')
                # Parse the HTML content using Beautiful Soup
                article_data['content'] = parsed_html.prettify()
            else:
                article_data['content'] = ''

            # Create and save the article
            article = Article.objects.create(
                author=article_data["author"],
                title=article_data["title"],
                short_description=article_data["short_desc"],
                url=article_data["url"],
                image_url=article_data["image_url"],
                publishing_datetime=article_data["pub_date"],
                content=article_data["content"],
            )

        except Exception as e:
            pass

    print('Scraping and saving completed.')
else:
    print('Failed to retrieve webpage')
