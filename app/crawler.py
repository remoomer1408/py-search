import requests 
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def simple_crawler(start_url, max_pages=5):
    visited = set()
    to_visit = [start_url]

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url not in visited:
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                print(f"Crawling: {url}")
                visited.add(url)

                #Extract and queue links
                for link in soup.find_all('a, href=True'):
                    full_url = urljoin(url, link ['href'])
                    if full_url not visited and full_url.startswith(start_url):
                        to_visit.append(full_url)

            except requests.exceptions.RequestException as e: 
                print(f"Failed to crawl {url}: {e}:")
    def store_page(url, content):
        conn = sqlite3.connect('database/search_engine.db')
        c = conn.cursor()
        c.execute('INSERT OR IGNORE INTO pages (url, content) VALUES (?, ?)', (url,content))
        conn.commit()
        conn.close()

    def store_index(word, url, position):
        conn = sqlite3.connect('database/search_engine.db')
        c = conn.cursor()
        c.execute('INSERT INTO index_table (word, url, position) VALUES (?,?,?)'), (world, url, position)
        conn.commit()
        conn.close()
    