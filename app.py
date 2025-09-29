from flask import Flask, render_template, request, jsonify
import requests
import os
from datetime import datetime
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuración más flexible para Vercel
SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key-for-development')
app.secret_key = SECRET_KEY

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything'
SOURCES_API_URL = 'https://newsapi.org/v2/sources'

# Configuración por defecto
default_config = {
    'category': 'general',
    'sources': '',
    'q': '',
    'language': 'es',
    'sortBy': 'publishedAt'
}

def fetch_news(query=None, sources=None, language='es', category=None, page_size=20):
    """
    Función para obtener noticias de la API
    """
    if not NEWS_API_KEY:
        logger.error("NEWS_API_KEY no está configurada")
        return [], "La clave de API de noticias no está configurada."
    
    params = {
        'apiKey': NEWS_API_KEY,
        'language': language,
        'pageSize': page_size,
        'sortBy': 'publishedAt'
    }
    
    # Construir la query de búsqueda
    query_parts = []
    
    if query and query.strip():
        query_parts.append(query.strip())
    
    if category and category != 'general' and not sources:
        query_parts.append(category)
    
    # Si hay query específica, usarla; si no, usar una query por defecto
    if query_parts:
        params['q'] = ' AND '.join(query_parts)
    elif not sources:
        params['q'] = 'noticias OR actualidad OR informacion'
    
    # Agregar fuentes si están especificadas
    if sources and sources.strip():
        params['sources'] = sources.strip()
    
    try:
        response = requests.get(NEWS_API_BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get('status') != 'ok':
            error_msg = data.get('message', 'Error desconocido de la API')
            logger.error(f"Error de API: {error_msg}")
            return [], f"Error de la API de noticias: {error_msg}"
        
        articles = data.get('articles', [])
        
        # Filtrar artículos sin título o descripción
        filtered_articles = []
        for article in articles:
            if article.get('title') and article.get('title') != '[Removed]':
                # Formatear fecha
                if article.get('publishedAt'):
                    try:
                        date_obj = datetime.fromisoformat(article['publishedAt'].replace('Z', '+00:00'))
                        article['publishedAt'] = date_obj.strftime('%d/%m/%Y %H:%M')
                    except:
                        pass
                filtered_articles.append(article)
        
        return filtered_articles, None
        
    except requests.exceptions.Timeout:
        error_msg = "Timeout al conectar con la API de noticias"
        logger.error(error_msg)
        return [], error_msg
    except requests.exceptions.RequestException as e:
        error_msg = f"Error al conectar con la API de noticias: {str(e)}"
        logger.error(error_msg)
        return [], error_msg
    except Exception as e:
        error_msg = f"Error inesperado: {str(e)}"
        logger.error(error_msg)
        return [], error_msg


def fetch_sources(language='es'):
    """
    Función para obtener las fuentes disponibles
    """
    if not NEWS_API_KEY:
        return []
    
    try:
        params = {
            'apiKey': NEWS_API_KEY,
            'language': language
        }
        response = requests.get(SOURCES_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get('status') == 'ok':
            return data.get('sources', [])
        else:
            logger.error(f"Error al obtener fuentes: {data.get('message', 'Error desconocido')}")
            return []
            
    except Exception as e:
        logger.error(f"Error al obtener fuentes: {str(e)}")
        return []


@app.route('/', methods=['GET', 'POST'])
def index():
    # Configuración por defecto
    config = default_config.copy()
    articles = []
    available_sources = []
    error_message = None
    
    if request.method == 'POST':
        # Obtener parámetros del formulario
        config['category'] = request.form.get('category', default_config['category'])
        config['sources'] = request.form.get('sources', default_config['sources'])
        config['q'] = request.form.get('q', default_config['q'])
        config['language'] = request.form.get('language', default_config['language'])
    else:
        # Para GET, usar parámetros de URL si están presentes
        config['category'] = request.args.get('category', default_config['category'])
        config['sources'] = request.args.get('sources', default_config['sources'])
        config['q'] = request.args.get('q', default_config['q'])
        config['language'] = request.args.get('language', default_config['language'])
    
    # Obtener noticias
    articles, error_message = fetch_news(
        query=config['q'],
        sources=config['sources'],
        language=config['language'],
        category=config['category']
    )
    
    # Obtener fuentes disponibles
    available_sources = fetch_sources(config['language'])
    
    return render_template(
        'index.html', 
        articles=articles, 
        config=config, 
        error_message=error_message, 
        available_sources=available_sources
    )


@app.route('/api/news', methods=['GET'])
def api_news():
    """
    Endpoint de API para obtener noticias en formato JSON
    """
    query = request.args.get('q', '')
    sources = request.args.get('sources', '')
    language = request.args.get('language', 'es')
    category = request.args.get('category', 'general')
    
    articles, error_message = fetch_news(query, sources, language, category)
    
    if error_message:
        return jsonify({'error': error_message}), 500
    
    return jsonify({
        'status': 'ok',
        'totalResults': len(articles),
        'articles': articles
    })


@app.route('/api/sources', methods=['GET'])
def api_sources():
    """
    Endpoint de API para obtener fuentes disponibles
    """
    language = request.args.get('language', 'es')
    sources = fetch_sources(language)
    
    return jsonify({
        'status': 'ok',
        'sources': sources
    })


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint para Vercel
    """
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'api_key_configured': bool(NEWS_API_KEY)
    })


# Para desarrollo local
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
