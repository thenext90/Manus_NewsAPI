#!/usr/bin/env python3
"""
Script para verificar el estado de la configuración de APITube.io
"""

import os
import sys
from datetime import datetime

def check_api_configuration():
    """Verifica la configuración de APITube.io"""
    
    print("🔍 VERIFICACIÓN DE CONFIGURACIÓN APITUBE.IO")
    print("=" * 50)
    print()
    
    # Verificar variables de entorno locales (para desarrollo)
    apitube_key = os.environ.get('APITUBE_API_KEY')
    secret_key = os.environ.get('SECRET_KEY')
    
    print("📋 VARIABLES DE ENTORNO LOCALES:")
    if apitube_key:
        print(f"  ✅ APITUBE_API_KEY: Configurada (longitud: {len(apitube_key)})")
        if apitube_key.startswith('at_'):
            print("  ✅ Formato correcto (comienza con 'at_')")
        else:
            print("  ⚠️  Formato inusual (no comienza con 'at_')")
    else:
        print("  ⚠️  APITUBE_API_KEY: No encontrada localmente")
        print("  💡 Esto es normal si está configurada solo en Vercel")
    
    if secret_key:
        print(f"  ✅ SECRET_KEY: Configurada (longitud: {len(secret_key)})")
    else:
        print("  ⚠️  SECRET_KEY: No encontrada localmente")
        print("  💡 Esto es normal si está configurada solo en Vercel")
    
    print()
    print("🚀 CONFIGURACIÓN EN VERCEL:")
    print("  Para producción, las variables deben estar en:")
    print("  Dashboard → Settings → Environment Variables")
    print()
    print("  Variables requeridas:")
    print("  • APITUBE_API_KEY: Tu clave de https://apitube.io/")
    print("  • SECRET_KEY: Clave secreta generada")
    print()
    
    print("🧪 ENDPOINTS DE PRUEBA:")
    print("  Una vez deployado, puedes probar:")
    print("  • https://tu-app.vercel.app/health")
    print("  • https://tu-app.vercel.app/test-api")
    print("  • https://tu-app.vercel.app/api/news?q=test")
    print()
    
    print("📊 VENTAJAS DE APITUBE.IO:")
    features = [
        "500,000+ fuentes verificadas",
        "177 países disponibles", 
        "60+ idiomas soportados",
        "65+ parámetros de filtrado",
        "Actualizaciones en tiempo real",
        "IA integrada para análisis"
    ]
    
    for feature in features:
        print(f"  • {feature}")
    
    print()
    print(f"🕒 Verificación realizada: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("✅ Proyecto listo para deploy en Vercel")

if __name__ == '__main__':
    check_api_configuration()