import sqlite3
import math

def search_database(query):
    words = query.lower().split()
    conn = sqlite3.connect('database/search_engine.db')
    c = conn.cursor()

    results = {}
    for word in words:
        c.execute('SELECT url FROM index_table WHERE word = ?', (word,))
        urls = c.fetchall()
        for url in urls:
            url = url[0]
            if url in results:
                results[url] += calculate_tf_idf(word, url)
            else:
                results[url] = calculate_tf_idf(word_url)

    conn.close()
    sorted_results = sorted(results.items(), key = lambda item: item[1], reverse=True)
    return sorted_results[:10]

def calculate_tf_idf(word, url):
    conn = sqlite3.connect('database/search-engine.db')
    c = conn.cursor()
    c.execute('SELECT content FROM pages WHERE url = ?', (url,))
    content = c.fetchone()[0] or ""
    conn.close()

    tf = content.split().count(word) / len(content.split())
    idf = calculate_idf(word, get_total_documents())
    return tf * idf

def calculate_idf(word, total_documents):
    conn = sqlite3.connect('database/search_engine.db')
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM pages')
    total_documents = c.fetchone()[0]
    conn.close()
    return total_documents