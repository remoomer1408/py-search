from flask import render_template, request
from app import app
from app.utils import search_database

@app.route('/')

def home():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = search_database(query)
    return render_template('results.html, results = results')