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

# Configuración para APITube.io
APITUBE_API_KEY = os.environ.get('APITUBE_API_KEY')
APITUBE_BASE_URL = 'https://api.apitube.io/v1/news/everything'
APITUBE_CATEGORIES_URL = 'https://api.apitube.io/v1/news/category'
APITUBE_TOP_HEADLINES_URL = 'https://api.apitube.io/v1/news/top-headlines'

# Configuración por defecto
default_config = {
    'category': 'general',
    'country': '',
    'q': '',
    'language': 'es',
    'sortBy': 'published_at'
}

def fetch_news(query=None, country=None, language='es', category=None, page_size=20):
    """
    Función para obtener noticias de APITube.io
    """
    if not APITUBE_API_KEY:
        logger.error("APITUBE_API_KEY no está configurada")
        return [], "La clave de API de APITube.io no está configurada."
    
    # Configurar headers de autenticación
    headers = {
        'X-API-Key': APITUBE_API_KEY,
        'Content-Type': 'application/json'
    }
    
    # Parámetros base
    params = {
        'per_page': page_size,
        'sort_by': 'published_at',
        'order': 'desc'
    }
    
    # Configurar idioma
    if language:
        params['language.code'] = language
    
    # Configurar país
    if country and country.strip():
        params['country.code'] = country.strip()
    
    # Configurar categoría
    if category and category != 'general':
        params['category'] = category
    
    # Configurar búsqueda de texto
    if query and query.strip():
        params['title'] = query.strip()
    elif not query and category == 'general':
        # Búsqueda por defecto para contenido general relevante
        params['title'] = 'noticias OR actualidad OR información'
    
    try:
        response = requests.get(APITUBE_BASE_URL, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        if not data.get('success', True):
            error_msg = data.get('message', 'Error desconocido de la API')
            logger.error(f"Error de API: {error_msg}")
            return [], f"Error de la API de APITube.io: {error_msg}"
        
        articles = data.get('data', [])
        
        # Procesar y filtrar artículos
        processed_articles = []
        for article in articles:
            if article.get('title') and article.get('title').strip():
                # Formatear datos para compatibilidad con el template
                processed_article = {
                    'title': article.get('title', ''),
                    'description': article.get('description', ''),
                    'url': article.get('href', ''),
                    'publishedAt': format_date(article.get('published_at')),
                    'source': {
                        'name': article.get('source', {}).get('name', 'Fuente desconocida')
                    },
                    'urlToImage': article.get('image', ''),
                    'content': article.get('body', '')[:200] + '...' if article.get('body') else None
                }
                processed_articles.append(processed_article)
        
        return processed_articles, None
        
    except requests.exceptions.Timeout:
        error_msg = "Timeout al conectar con la API de APITube.io"
        logger.error(error_msg)
        return [], error_msg
    except requests.exceptions.RequestException as e:
        error_msg = f"Error al conectar con la API de APITube.io: {str(e)}"
        logger.error(error_msg)
        return [], error_msg
    except Exception as e:
        error_msg = f"Error inesperado: {str(e)}"
        logger.error(error_msg)
        return [], error_msg


def fetch_categories():
    """
    Función para obtener las categorías disponibles de APITube.io
    """
    if not APITUBE_API_KEY:
        return []
    
    # Categorías disponibles en APITube.io según su documentación
    categories = [
        {'id': 'general', 'name': 'General'},
        {'id': 'business', 'name': 'Negocios'},
        {'id': 'entertainment', 'name': 'Entretenimiento'},
        {'id': 'health', 'name': 'Salud'},
        {'id': 'science', 'name': 'Ciencia'},
        {'id': 'sports', 'name': 'Deportes'},
        {'id': 'technology', 'name': 'Tecnología'},
        {'id': 'politics', 'name': 'Política'},
        {'id': 'finance', 'name': 'Finanzas'},
        {'id': 'education', 'name': 'Educación'},
        {'id': 'travel', 'name': 'Viajes'},
        {'id': 'food', 'name': 'Comida'},
        {'id': 'lifestyle', 'name': 'Estilo de vida'}
    ]
    
    return categories


def get_countries():
    """
    Lista de países disponibles para filtrar noticias
    """
    countries = [
        {'code': '', 'name': 'Todos los países'},
        {'code': 'es', 'name': 'España'},
        {'code': 'mx', 'name': 'México'},
        {'code': 'ar', 'name': 'Argentina'},
        {'code': 'co', 'name': 'Colombia'},
        {'code': 'pe', 'name': 'Perú'},
        {'code': 'cl', 'name': 'Chile'},
        {'code': 'us', 'name': 'Estados Unidos'},
        {'code': 'gb', 'name': 'Reino Unido'},
        {'code': 'fr', 'name': 'Francia'},
        {'code': 'de', 'name': 'Alemania'},
        {'code': 'it', 'name': 'Italia'},
        {'code': 'br', 'name': 'Brasil'},
        {'code': 'cn', 'name': 'China'},
        {'code': 'jp', 'name': 'Japón'},
        {'code': 'in', 'name': 'India'}
    ]
    return countries


def format_date(date_string):
    """
    Formatea la fecha de APITube.io al formato deseado
    """
    if not date_string:
        return 'Fecha no disponible'
    
    try:
        # APITube.io usa formato ISO 8601
        if date_string.endswith('Z'):
            date_string = date_string[:-1] + '+00:00'
        
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime('%d/%m/%Y %H:%M')
    except Exception:
        return date_string


@app.route('/', methods=['GET', 'POST'])
def index():
    # Configuración por defecto
    config = default_config.copy()
    articles = []
    categories = fetch_categories()
    countries = get_countries()
    error_message = None
    
    if request.method == 'POST':
        # Obtener parámetros del formulario
        config['category'] = request.form.get('category', default_config['category'])
        config['country'] = request.form.get('country', default_config['country'])
        config['q'] = request.form.get('q', default_config['q'])
        config['language'] = request.form.get('language', default_config['language'])
    else:
        # Para GET, usar parámetros de URL si están presentes
        config['category'] = request.args.get('category', default_config['category'])
        config['country'] = request.args.get('country', default_config['country'])
        config['q'] = request.args.get('q', default_config['q'])
        config['language'] = request.args.get('language', default_config['language'])
    
    # Obtener noticias usando APITube.io
    articles, error_message = fetch_news(
        query=config['q'],
        country=config['country'],
        language=config['language'],
        category=config['category']
    )
    
    return render_template(
        'index.html', 
        articles=articles, 
        config=config, 
        error_message=error_message, 
        categories=categories,
        countries=countries
    )


@app.route('/api/news', methods=['GET'])
def api_news():
    """
    Endpoint de API para obtener noticias en formato JSON usando APITube.io
    """
    query = request.args.get('q', '')
    country = request.args.get('country', '')
    language = request.args.get('language', 'es')
    category = request.args.get('category', 'general')
    
    articles, error_message = fetch_news(query, country, language, category)
    
    if error_message:
        return jsonify({'error': error_message}), 500
    
    return jsonify({
        'status': 'success',
        'totalResults': len(articles),
        'articles': articles
    })


@app.route('/api/categories', methods=['GET'])
def api_categories():
    """
    Endpoint de API para obtener categorías disponibles
    """
    categories = fetch_categories()
    
    return jsonify({
        'status': 'success',
        'categories': categories
    })


@app.route('/api/countries', methods=['GET'])
def api_countries():
    """
    Endpoint de API para obtener países disponibles
    """
    countries = get_countries()
    
    return jsonify({
        'status': 'success',
        'countries': countries
    })


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint para Vercel
    """
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'api_service': 'APITube.io',
        'api_key_configured': bool(APITUBE_API_KEY),
        'api_key_length': len(APITUBE_API_KEY) if APITUBE_API_KEY else 0,
        'api_key_format': 'Valid' if APITUBE_API_KEY and APITUBE_API_KEY.startswith('at_') else 'Invalid',
        'endpoints_available': [
            '/',
            '/api/news',
            '/api/categories', 
            '/api/countries',
            '/health',
            '/test-api'
        ]
    })


@app.route('/test-api', methods=['GET'])
def test_api_connection():
    """
    Endpoint para probar la conexión con APITube.io
    """
    if not APITUBE_API_KEY:
        return jsonify({
            'status': 'error',
            'message': 'APITUBE_API_KEY no está configurada',
            'solution': 'Configura la variable APITUBE_API_KEY en Vercel'
        }), 500
    
    # Configurar headers de prueba
    headers = {
        'X-API-Key': APITUBE_API_KEY,
        'Content-Type': 'application/json'
    }
    
    # Parámetros de prueba mínimos
    params = {
        'per_page': 1,
        'title': 'test'
    }
    
    try:
        response = requests.get(APITUBE_BASE_URL, params=params, headers=headers, timeout=10)
        
        return jsonify({
            'status': 'success',
            'api_service': 'APITube.io',
            'api_url': APITUBE_BASE_URL,
            'response_status': response.status_code,
            'api_key_working': response.status_code == 200,
            'message': 'Conexión exitosa con APITube.io' if response.status_code == 200 else f'Error HTTP {response.status_code}',
            'timestamp': datetime.now().isoformat()
        })
        
    except requests.exceptions.RequestException as e:
        return jsonify({
            'status': 'error',
            'message': f'Error de conexión: {str(e)}',
            'api_service': 'APITube.io',
            'timestamp': datetime.now().isoformat()
        }), 500


# Para desarrollo local
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
