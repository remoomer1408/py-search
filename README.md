# py-search
This project is a basic search engine built using Python and Flask. It crawls web pages, indexes their content, and provides search functionality through a web interface.

Overview
This project is a basic search engine built using Python and Flask. It crawls web pages, indexes their content, and provides search functionality through a web interface. The purpose of this project is to understand the core concepts of web crawling, indexing, and building a simple information retrieval system.

Features
Web Crawler: Crawls and indexes web pages.
Search Functionality: Allows users to input queries and receive a list of relevant pages.
Ranking Mechanism: Utilizes TF-IDF scoring to rank pages.
Web Interface: Built with Flask for a simple and interactive user experience.

File Structure
/project-root
    /app
        __init__.py         # Initializes the Flask application
        routes.py           # Contains routes for handling web requests
        utils.py            # Utility functions for searching and calculating TF-IDF
        crawler.py          # Web crawler script to index pages
    /templates
        search.html         # HTML for the main search page
        results.html        # HTML for displaying search results
    /database
        search_engine.db    # SQLite database for storing indexed data
    config.py               # Configuration file for the project
    run.py                  # Entry point for running the Flask application
    requirements.txt        # List of dependencies
    .gitignore              # Specifies files and folders to be ignored by Git


Installation

1. Clone the repository:
git clone https://github.com/username/search-engine-project.git
cd search-engine-project

2. Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the web crawler:
python app/crawler.py

5. Run the Flask app:
python run.py

Access the application: Open a web browser and go to http://127.0.0.1:5000/.

Usage

Search: Enter a search query on the main page and submit. The app will display a list of relevant results with their scores.
Crawl: Modify crawler.py to change the starting URL for crawling.

Technologies Used

Python: Core language
Flask: Web framework
Beautiful Soup: HTML parsing
SQLite: Database for storing pages and indexes
Jinja2: Templating engine

Future Enhancements

Adding support for more complex search queries.
Implementing pagination for search results.
Enhancing the crawler to handle more complex websites.
Adding user feedback for search result relevance.

Contributing

Feel free to fork the repository, make improvements, and submit a pull request. Contributions are welcome!

License

This project is licensed under the MIT License. See LICENSE for more details.

