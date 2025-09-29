#!/usr/bin/env python3
"""
Test de diferentes endpoints de APITube.io
"""

import requests
import os
import json

APITUBE_API_KEY = os.environ.get('APITUBE_API_KEY')
if not APITUBE_API_KEY:
    print("❌ Error: Configura APITUBE_API_KEY")
    exit(1)

headers = {
    'X-API-Key': APITUBE_API_KEY,
    'Content-Type': 'application/json'
}

# Diferentes URLs posibles para APITube.io
endpoints_to_test = [
    'https://api.apitube.io/v1/news/everything',
    'https://api.apitube.io/v1/news/top-headlines', 
    'https://api.apitube.io/v1/news',
    'https://api.apitube.io/news/everything',
    'https://api.apitube.io/news',
]

def test_endpoint(url, params):
    """Test individual endpoint"""
    try:
        print(f"📡 Probando: {url}")
        print(f"📋 Parámetros: {params}")
        
        response = requests.get(url, params=params, headers=headers, timeout=15)
        print(f"📊 Status: {response.status_code}")
        print(f"🔗 URL final: {response.url}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                if isinstance(data, dict) and 'data' in data:
                    articles = data['data']
                    print(f"✅ ÉXITO: {len(articles)} artículos encontrados")
                    
                    if articles:
                        first = articles[0]
                        print(f"   📰 Primer título: {first.get('title', 'N/A')[:80]}")
                        print(f"   🏢 Fuente: {first.get('source', {}).get('name', 'N/A')}")
                        return True, len(articles)
                else:
                    print(f"⚠️  Respuesta inesperada: {list(data.keys()) if isinstance(data, dict) else type(data)}")
            except json.JSONDecodeError:
                print(f"❌ Respuesta no es JSON: {response.text[:100]}")
        elif response.status_code == 404:
            print("❌ 404: Endpoint no existe")
        elif response.status_code == 401:
            print("❌ 401: API Key inválida")
        else:
            print(f"❌ Error {response.status_code}: {response.text[:100]}")
            
    except requests.exceptions.RequestException as e:
        print(f"🌐 Error de conexión: {e}")
        
    return False, 0

def main():
    print("🔍 TESTING APITUBE.IO ENDPOINTS")
    print("="*50)
    
    # Parámetros básicos para prueba
    basic_params = {
        'language': 'es',
        'limit': 3
    }
    
    spanish_search_params = {
        'q': 'España',
        'language': 'es', 
        'limit': 3
    }
    
    working_endpoints = []
    
    print("\n🧪 FASE 1: Test endpoints básicos")
    print("-" * 40)
    
    for url in endpoints_to_test:
        print(f"\n📍 Endpoint: {url}")
        success, count = test_endpoint(url, basic_params)
        if success:
            working_endpoints.append(url)
        print()
    
    if working_endpoints:
        print(f"\n✅ Endpoints que funcionan: {len(working_endpoints)}")
        for endpoint in working_endpoints:
            print(f"   - {endpoint}")
            
        print("\n🧪 FASE 2: Test búsqueda en español en endpoints funcionales")
        print("-" * 40)
        
        for url in working_endpoints:
            print(f"\n📍 Probando búsqueda español en: {url}")
            test_endpoint(url, spanish_search_params)
            print()
    else:
        print("\n❌ NINGÚN ENDPOINT FUNCIONÓ")
        print("Posibles causas:")
        print("1. API Key inválida")
        print("2. URLs incorrectas")
        print("3. APITube.io cambió su estructura")
        print("4. Problema de autenticación")

if __name__ == "__main__":
    main()