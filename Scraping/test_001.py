import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


def get_search_results(query, api_key, search_engine_id, num_results=10):
    search_url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': search_engine_id,
        'q': query,
        'num': num_results
    }
    response = requests.get(search_url, params=params)
    results = response.json().get('items', [])
    return [result['link'] for result in results]


def fetch_webpage(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')
    text_content = ' '.join([para.text for para in paragraphs])
    return text_content


def is_allowed_to_crawl(base_url, path):
    robots_url = urljoin(base_url, '/robots.txt')
    response = requests.get(robots_url)
    if response.status_code == 200:
        robots_txt = response.text
        if f"Disallow: {path}" in robots_txt:
            return False
    return True


def main():
    api_key = 'your_google_api_key_here'
    search_engine_id = 'your_search_engine_id_here'
    query = '最新的AI技术'
    headers = {'User-Agent': 'MyCrawler/1.0 (+http://mywebsite.com/crawler)'}

    urls = get_search_results(query, api_key, search_engine_id)

    for url in urls:
        base_url = urljoin(url, '/')
        path = url.replace(base_url, '')

        if is_allowed_to_crawl(base_url, path):
            html_content = fetch_webpage(url, headers)
            if html_content:
                text_content = parse_html(html_content)
                print(f"内容来自 {url}:\n{text_content[:200]}...")  # 打印前200个字符
            else:
                print(f"无法获取内容: {url}")
            time.sleep(2)  # 等待2秒
        else:
            print(f"禁止爬取: {url}")


if __name__ == "__main__":
    main()