from flask import Flask, render_template, request, redirect, url_for, session
import requests
import os
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)

NEWS_API_KEY = '302857ab1fe041249e0fd1ff87f6bb32'
NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything'
CONFIG_FILE = 'config.json'

default_config = {
    'category': 'general',
    'sources': '',
    'q': '',
    'language': 'es'
}

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return default_config.copy()

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

@app.route('/', methods=['GET', 'POST'])
def index():
    current_config = load_config()

    if request.method == 'POST':
        current_config['category'] = request.form.get('category', default_config['category'])
        current_config['sources'] = request.form.get('sources', default_config['sources'])
        current_config['q'] = request.form.get('q', default_config['q'])
        current_config['language'] = request.form.get('language', default_config['language'])
        save_config(current_config)
        return redirect(url_for('index'))

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

    if current_config.get('sources'):
        params['sources'] = current_config['sources']

    if 'q' not in params and 'sources' not in params:
        params['q'] = 'noticias'

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

    sources_response = requests.get('https://newsapi.org/v2/sources', params={'apiKey': NEWS_API_KEY, 'language': current_config['language']})
    available_sources = []
    if sources_response.status_code == 200:
        sources_data = sources_response.json()
        available_sources = sources_data.get('sources', [])

    return render_template('index.html', articles=articles, config=current_config, error_message=error_message, available_sources=available_sources)

if __name__ == '__main__':
    if not os.path.exists(CONFIG_FILE):
        save_config(default_config)
    app.run(debug=True, host='0.0.0.0')
