#!/usr/bin/env python3
"""
Script de verificación para el Buscador de Noticias
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
        'README.md'
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
    """Verifica las variables de entorno"""
    print("\n🔐 Verificando configuración de variables de entorno...")
    
    # Para desarrollo local
    news_api_key = os.environ.get('NEWS_API_KEY')
    secret_key = os.environ.get('SECRET_KEY')
    
    if news_api_key:
        print(f"  ✅ NEWS_API_KEY configurada (longitud: {len(news_api_key)})")
    else:
        print("  ⚠️  NEWS_API_KEY no encontrada localmente (debe estar en Vercel)")
    
    if secret_key:
        print(f"  ✅ SECRET_KEY configurada (longitud: {len(secret_key)})")
    else:
        print("  ⚠️  SECRET_KEY no encontrada localmente (debe estar en Vercel)")
    
    print("\n📋 Variables de entorno requeridas en Vercel:")
    print("  • NEWS_API_KEY: Tu clave de API de NewsAPI")
    print("  • SECRET_KEY: Clave secreta para Flask")
    
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
        
        print("  ✅ requirements.txt es válido")
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

def main():
    """Función principal"""
    print("🔍 VERIFICACIÓN DEL PROYECTO - BUSCADOR DE NOTICIAS")
    print("=" * 60)
    
    checks = [
        check_files(),
        check_syntax(),
        check_dependencies(),
        check_vercel_config(),
        check_env_vars()
    ]
    
    print("\n" + "=" * 60)
    
    if all(checks):
        print("🎉 ¡PROYECTO LISTO PARA DEPLOY!")
        print("\n📝 Próximos pasos:")
        print("1. Asegúrate de que las variables de entorno estén configuradas en Vercel")
        print("2. Haz push de los cambios a tu repositorio")
        print("3. Deploy automático en Vercel")
        print("\n🌐 URLs importantes:")
        print("• Dashboard de Vercel: https://vercel.com/dashboard")
        print("• NewsAPI: https://newsapi.org/")
        return 0
    else:
        print("❌ HAY PROBLEMAS QUE RESOLVER")
        print("Por favor, revisa los errores mostrados arriba")
        return 1

if __name__ == '__main__':
    sys.exit(main())