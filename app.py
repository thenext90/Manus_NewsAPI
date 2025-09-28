from flask import Flask, render_template, request, redirect, url_for, session
import requests
import os
import json

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
if not app.secret_key:
    raise ValueError("No SECRET_KEY set for Flask application")

NEWS_API_KEY = os.getenv('NEWS_API_KEY')
if not NEWS_API_KEY:
    raise ValueError("No NEWS_API_KEY set for Flask application")
NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'config' not in session:
        session['config'] = {
            'category': 'general',
            'sources': '',
            'q': '',
            'language': 'es'
        }

    if request.method == 'POST':
        session['config']['category'] = request.form.get('category', 'general')
        session['config']['sources'] = request.form.get('sources', '')
        session['config']['q'] = request.form.get('q', '')
        session['config']['language'] = request.form.get('language', 'es')
        session.modified = True
        return redirect(url_for('index'))

    current_config = session['config']

    params = {
        'apiKey': NEWS_API_KEY,
        'language': current_config['language']
    }

    query_parts = []
    if current_config.get('q'):
        query_parts.append(current_config['q'])
    
    if current_config.get('category') and current_config['category'] != 'general' and not current_config.get('sources'):
        query_parts.append(current_config['category'])

    if query_parts:
        params['q'] = ' AND '.join(query_parts)
    elif not current_config.get('sources'):
        params['q'] = 'noticias'

    if current_config.get('sources'):
        params['sources'] = current_config['sources']

    articles = []
    error_message = None
    try:
        response = requests.get(NEWS_API_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        articles = data.get("articles", [])
    except requests.exceptions.RequestException as e:
        error_message = f"Error al conectar con la API de noticias: {e}"
    except ValueError:
        error_message = "Error al decodificar la respuesta JSON de la API."

    available_sources = []
    try:
        sources_response = requests.get('https://newsapi.org/v2/sources', params={'apiKey': NEWS_API_KEY, 'language': current_config['language']})
        sources_response.raise_for_status()
        sources_data = sources_response.json()
        available_sources = sources_data.get('sources', [])
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error fetching news sources: {e}")

    return render_template('index.html', articles=articles, config=current_config, error_message=error_message, available_sources=available_sources)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
