#!/usr/bin/env python3
"""
Test exhaustivo de parámetros para APITube.io
"""

import requests
import os
import json
from datetime import datetime

# Configuración
APITUBE_API_KEY = os.environ.get('APITUBE_API_KEY')
if not APITUBE_API_KEY:
    print("❌ Error: Configura APITUBE_API_KEY con: set APITUBE_API_KEY=tu_api_key")
    exit(1)

BASE_URL = 'https://api.apitube.io/v1/news/everything'

headers = {
    'X-API-Key': APITUBE_API_KEY,
    'Content-Type': 'application/json'
}

def test_parameter_variations():
    """
    Prueba diferentes variaciones de parámetros
    """
    print("🧪 TESTING PARAMETER VARIATIONS")
    print("="*50)
    
    # Diferentes formas de especificar parámetros que podrían funcionar
    test_configs = [
        {
            'name': 'Configuración Actual (que falla)',
            'params': {
                'q': 'España',
                'language': 'es',
                'limit': 3,
                'sortBy': 'publishedAt',
                'order': 'desc'
            }
        },
        {
            'name': 'Sin sortBy (problema común)',
            'params': {
                'q': 'España',
                'language': 'es',
                'limit': 3
            }
        },
        {
            'name': 'Idioma como lang',
            'params': {
                'q': 'España', 
                'lang': 'es',
                'limit': 3
            }
        },
        {
            'name': 'Usando search en lugar de q',
            'params': {
                'search': 'España',
                'language': 'es', 
                'limit': 3
            }
        },
        {
            'name': 'Usando query en lugar de q',
            'params': {
                'query': 'España',
                'language': 'es',
                'limit': 3
            }
        },
        {
            'name': 'País como ES',
            'params': {
                'q': 'noticias',
                'language': 'es',
                'country': 'ES',
                'limit': 3
            }
        },
        {
            'name': 'Idioma como español completo', 
            'params': {
                'q': 'España',
                'language': 'spanish',
                'limit': 3
            }
        },
        {
            'name': 'Solo idioma español sin query',
            'params': {
                'language': 'es',
                'limit': 10
            }
        },
        {
            'name': 'Parámetros mínimos absolutos',
            'params': {
                'limit': 5
            }
        }
    ]
    
    for i, config in enumerate(test_configs, 1):
        print(f"\n{'='*60}")
        print(f"🔬 Test {i}: {config['name']}")
        print(f"{'='*60}")
        
        try:
            print(f"Parámetros: {json.dumps(config['params'], indent=2)}")
            
            response = requests.get(BASE_URL, params=config['params'], headers=headers, timeout=15)
            
            print(f"📡 URL completa: {response.url}")
            print(f"📊 Status Code: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    print(f"✅ Respuesta JSON válida")
                    print(f"📝 Claves: {list(data.keys())}")
                    
                    if 'data' in data:
                        articles = data['data']
                        print(f"📰 Artículos encontrados: {len(articles)}")
                        
                        if articles:
                            print(f"🎯 ÉXITO! Encontrados {len(articles)} artículos")
                            first = articles[0]
                            print(f"   Título: {first.get('title', 'N/A')[:100]}")
                            print(f"   Fuente: {first.get('source', {}).get('name', 'N/A')}")
                            print(f"   Idioma detectado: {first.get('language', 'N/A')}")
                        else:
                            print("⚠️  Array de datos vacío")
                    else:
                        print(f"❌ Sin clave 'data' en respuesta: {data}")
                        
                except json.JSONDecodeError:
                    print(f"❌ Respuesta no es JSON válido: {response.text[:200]}")
                    
            elif response.status_code == 401:
                print("❌ ERROR 401: API Key inválida o mal configurada")
                break
            elif response.status_code == 403:
                print("❌ ERROR 403: Acceso denegado, verifica permisos de API key")
                break  
            elif response.status_code == 429:
                print("⏰ ERROR 429: Límite de rate excedido")
                break
            else:
                print(f"❌ Error HTTP {response.status_code}: {response.text[:200]}")
                
        except requests.exceptions.RequestException as e:
            print(f"🌐 Error de conexión: {e}")
            break
        except Exception as e:
            print(f"💥 Error inesperado: {e}")
            
        input("\n⏸️  Presiona Enter para continuar al siguiente test...")

if __name__ == "__main__":
    print("🚀 DIAGNÓSTICO EXHAUSTIVO APITube.io")
    print(f"🔑 API Key: {'✅ Configurada' if APITUBE_API_KEY else '❌ No configurada'}")
    print(f"🔢 Longitud: {len(APITUBE_API_KEY)} caracteres")
    print(f"🏁 Prefijo: {APITUBE_API_KEY[:10]}..." if APITUBE_API_KEY else "N/A")
    
    test_parameter_variations()