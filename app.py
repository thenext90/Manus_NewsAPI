from flask import Flask, render_template, request, redirect, url_for, session
import requests
import os

app = Flask(__name__)
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("Error: La variable de entorno SECRET_KEY no está configurada. Por favor, configúrela para la sesión de Flask.")
app.secret_key = SECRET_KEY

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
if not NEWS_API_KEY:
    raise ValueError("Error: La variable de entorno NEWS_API_KEY no está configurada. Por favor, añada su clave de API de noticias.")
NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything'

default_config = {
    'category': 'general',
    'sources': '',
    'q': '',
    'language': 'es'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'config' not in session:
        session['config'] = default_config.copy()

    current_config = session['config']

    if request.method == 'POST':
        current_config['category'] = request.form.get('category', default_config['category'])
        current_config['sources'] = request.form.get('sources', default_config['sources'])
        current_config['q'] = request.form.get('q', default_config['q'])
        current_config['language'] = request.form.get('language', default_config['language'])
        session['config'] = current_config
        return redirect(url_for('index'))

    if not NEWS_API_KEY:
        return render_template('index.html', articles=[], config=current_config, error_message="La clave de API de noticias no está configurada.", available_sources=[])

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
        params['q'] = 'noticias' # Default query if nothing else is specified

    if current_config.get('sources'):
        params['sources'] = current_config['sources']

    articles = []
    available_sources = []
    error_message = None
    try:
        # Fetch articles
        response = requests.get(NEWS_API_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        articles = data.get("articles", [])

        # Fetch sources
        sources_response = requests.get('https://newsapi.org/v2/sources', params={'apiKey': NEWS_API_KEY, 'language': current_config['language']})
        sources_response.raise_for_status()
        sources_data = sources_response.json()
        available_sources = sources_data.get('sources', [])

    except requests.exceptions.RequestException as e:
        error_message = f"Error al conectar con la API de noticias: {e}"
    except ValueError:
        error_message = "Error al decodificar la respuesta JSON de la API."

    return render_template('index.html', articles=articles, config=current_config, error_message=error_message, available_sources=available_sources)

# Vercel will use a WSGI server to run the app, so this is not needed.
# if __name__ == '__main__':
#     app.run(debug=True)
