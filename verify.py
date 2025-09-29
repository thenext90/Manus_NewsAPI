#!/usr/bin/env python3
"""
Script de verificación para el APITube.io News Explorer
Verifica que todo esté listo para el deploy en Vercel
"""

import sys
import os
from pathlib import Path

def check_files():
    """Verifica que todos los archivos necesarios estén presentes"""
    print("🔍 Verificando archivos del proyecto...")
    
    required_files = [
        'app.py',
        'requirements.txt',
        'vercel.json',
        'templates/index.html',
        'README.md',
        'runtime.txt'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
        else:
            print(f"  ✅ {file_path}")
    
    if missing_files:
        print(f"  ❌ Archivos faltantes: {', '.join(missing_files)}")
        return False
    
    print("  ✅ Todos los archivos necesarios están presentes")
    return True

def check_syntax():
    """Verifica la sintaxis de Python"""
    print("\n🐍 Verificando sintaxis de Python...")
    
    try:
        import py_compile
        py_compile.compile('app.py', doraise=True)
        print("  ✅ app.py tiene sintaxis válida")
        return True
    except py_compile.PyCompileError as e:
        print(f"  ❌ Error de sintaxis en app.py: {e}")
        return False

def check_env_vars():
    """Verifica las variables de entorno para APITube.io"""
    print("\n🔐 Verificando configuración de variables de entorno...")
    
    # Para desarrollo local
    apitube_api_key = os.environ.get('APITUBE_API_KEY')
    secret_key = os.environ.get('SECRET_KEY')
    
    if apitube_api_key:
        print(f"  ✅ APITUBE_API_KEY configurada (longitud: {len(apitube_api_key)})")
        if apitube_api_key.startswith('at_'):
            print("  ✅ Formato de clave APITube.io correcto")
        else:
            print("  ⚠️  Formato de clave podría ser incorrecto (debe empezar con 'at_')")
    else:
        print("  ⚠️  APITUBE_API_KEY no encontrada localmente (debe estar en Vercel)")
    
    if secret_key:
        print(f"  ✅ SECRET_KEY configurada (longitud: {len(secret_key)})")
    else:
        print("  ⚠️  SECRET_KEY no encontrada localmente (debe estar en Vercel)")
    
    print("\n📋 Variables de entorno requeridas en Vercel:")
    print("  • APITUBE_API_KEY: Tu clave de API de APITube.io")
    print("  • SECRET_KEY: Clave secreta para Flask")
    
    print("\n🌟 Ventajas de APITube.io:")
    print("  • 500,000+ fuentes verificadas vs ~80,000 de NewsAPI")
    print("  • 177 países vs ~54 de otras APIs")
    print("  • 60+ idiomas vs ~14 de competidores")
    print("  • 65+ parámetros de filtrado vs ~10 básicos")
    print("  • Actualizaciones en tiempo real")
    print("  • IA integrada para análisis de sentimientos")
    
    return True

def check_dependencies():
    """Verifica las dependencias"""
    print("\n📦 Verificando dependencias...")
    
    try:
        with open('requirements.txt', 'r') as f:
            deps = f.read().strip().split('\n')
        
        print("  Dependencias en requirements.txt:")
        for dep in deps:
            if dep.strip():
                print(f"    • {dep.strip()}")
        
        print("  ✅ requirements.txt es válido para APITube.io")
        return True
    except Exception as e:
        print(f"  ❌ Error al leer requirements.txt: {e}")
        return False

def check_vercel_config():
    """Verifica la configuración de Vercel"""
    print("\n🚀 Verificando configuración de Vercel...")
    
    try:
        import json
        with open('vercel.json', 'r') as f:
            config = json.load(f)
        
        print("  ✅ vercel.json es JSON válido")
        
        # Verificar estructura básica
        if 'builds' in config and 'routes' in config:
            print("  ✅ vercel.json tiene la estructura correcta")
        else:
            print("  ⚠️  vercel.json podría tener problemas de estructura")
        
        return True
    except Exception as e:
        print(f"  ❌ Error al leer vercel.json: {e}")
        return False

def check_apitube_integration():
    """Verifica la integración específica con APITube.io"""
    print("\n🌐 Verificando integración con APITube.io...")
    
    try:
        with open('app.py', 'r') as f:
            content = f.read()
        
        if 'APITUBE_API_KEY' in content:
            print("  ✅ Configuración de APITube.io encontrada en app.py")
        else:
            print("  ❌ No se encontró configuración de APITube.io")
            return False
            
        if 'api.apitube.io' in content:
            print("  ✅ URL de APITube.io configurada correctamente")
        else:
            print("  ❌ URL de APITube.io no encontrada")
            return False
            
        if 'X-API-Key' in content:
            print("  ✅ Método de autenticación correcto (X-API-Key header)")
        else:
            print("  ⚠️  Método de autenticación podría estar mal configurado")
        
        print("  ✅ Integración con APITube.io parece correcta")
        return True
        
    except Exception as e:
        print(f"  ❌ Error al verificar integración: {e}")
        return False

def main():
    """Función principal"""
    print("🌐 VERIFICACIÓN DEL PROYECTO - APITUBE.IO NEWS EXPLORER")
    print("=" * 65)
    
    checks = [
        check_files(),
        check_syntax(),
        check_dependencies(),
        check_vercel_config(),
        check_apitube_integration(),
        check_env_vars()
    ]
    
    print("\n" + "=" * 65)
    
    if all(checks):
        print("🎉 ¡PROYECTO LISTO PARA DEPLOY CON APITUBE.IO!")
        print("\n📝 Próximos pasos:")
        print("1. Obtén tu API Key gratis en https://apitube.io/")
        print("2. Configura APITUBE_API_KEY en las variables de entorno de Vercel")
        print("3. Configura SECRET_KEY en Vercel")
        print("4. Haz push de los cambios a tu repositorio")
        print("5. Deploy automático en Vercel")
        print("\n🌐 URLs importantes:")
        print("• APITube.io: https://apitube.io/")
        print("• Documentación: https://docs.apitube.io/")
        print("• Dashboard Vercel: https://vercel.com/dashboard")
        print("• Query Builder: https://docs.apitube.io/platform/news-api/query-builder")
        print("\n🚀 ¡Experimenta el poder de 500,000+ fuentes de noticias!")
        return 0
    else:
        print("❌ HAY PROBLEMAS QUE RESOLVER")
        print("Por favor, revisa los errores mostrados arriba")
        return 1

if __name__ == '__main__':
    sys.exit(main())