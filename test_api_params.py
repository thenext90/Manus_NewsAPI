#!/usr/bin/env python3
"""
Script de prueba para verificar los parámetros de APITube.io
"""

import requests
import os
from pprint import pprint

# Configuración
APITUBE_API_KEY = os.environ.get('APITUBE_API_KEY')
APITUBE_BASE_URL = 'https://api.apitube.io/v1/news/everything'

def test_api_parameters():
    """
    Prueba diferentes combinaciones de parámetros
    """
    if not APITUBE_API_KEY:
        print("❌ Error: APITUBE_API_KEY no está configurada")
        print("Configúrala con: set APITUBE_API_KEY=tu_api_key")
        return
    
    headers = {
        'X-API-Key': APITUBE_API_KEY,
        'Content-Type': 'application/json'
    }
    
    # Diferentes configuraciones de prueba
    test_cases = [
        {
            'name': 'Búsqueda básica en español',
            'params': {
                'q': 'España',
                'language': 'es',
                'limit': 3
            }
        },
        {
            'name': 'Sin query, solo idioma español',
            'params': {
                'language': 'es',
                'limit': 3
            }
        },
        {
            'name': 'Con país España',
            'params': {
                'q': 'noticias',
                'country': 'ES',
                'language': 'es',
                'limit': 3
            }
        },
        {
            'name': 'Categoría deportes',
            'params': {
                'category': 'sports',
                'language': 'es',
                'limit': 3
            }
        },
        {
            'name': 'Parámetros mínimos',
            'params': {
                'limit': 1
            }
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*60}")
        print(f"Prueba {i}: {test_case['name']}")
        print(f"{'='*60}")
        
        try:
            print(f"URL: {APITUBE_BASE_URL}")
            print(f"Parámetros: {test_case['params']}")
            
            response = requests.get(
                APITUBE_BASE_URL, 
                params=test_case['params'], 
                headers=headers, 
                timeout=15
            )
            
            print(f"Status Code: {response.status_code}")
            print(f"URL final: {response.url}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Respuesta exitosa")
                print(f"Claves en respuesta: {list(data.keys())}")
                
                articles = data.get('data', [])
                print(f"Número de artículos: {len(articles)}")
                
                if articles:
                    print("\nPrimer artículo:")
                    first_article = articles[0]
                    print(f"  - Título: {first_article.get('title', 'N/A')[:100]}")
                    print(f"  - Fuente: {first_article.get('source', {}).get('name', 'N/A')}")
                    print(f"  - Fecha: {first_article.get('published_at', 'N/A')}")
                    print(f"  - Idioma: {first_article.get('language', 'N/A')}")
                else:
                    print("⚠️  No se encontraron artículos")
                    
            else:
                print(f"❌ Error HTTP: {response.status_code}")
                print(f"Respuesta: {response.text[:500]}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Error de conexión: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    print("🔍 Probando parámetros de APITube.io")
    print(f"API Key configurada: {'✅' if APITUBE_API_KEY else '❌'}")
    
    if APITUBE_API_KEY:
        print(f"Longitud de API Key: {len(APITUBE_API_KEY)} caracteres")
    
    test_api_parameters()