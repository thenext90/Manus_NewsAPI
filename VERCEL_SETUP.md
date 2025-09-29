# 🔐 CONFIGURACIÓN DE VARIABLES DE ENTORNO PARA VERCEL
# ====================================================

## 📋 VARIABLES REQUERIDAS PARA APITUBE.IO

### 1. APITUBE_API_KEY
```
Nombre: APITUBE_API_KEY
Valor: [Tu clave de APITube.io]
Descripción: Clave de autenticación para acceder a la API de APITube.io
Obtener en: https://apitube.io/
Formato típico: at_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 2. SECRET_KEY
```
Nombre: SECRET_KEY
Valor: [Clave secreta generada]
Descripción: Clave secreta para Flask sessions y seguridad
Generar con: python -c "import secrets; print(secrets.token_urlsafe(32))"
Ejemplo: dGhpc19pc19hX3NlY3VyZV9rZXlfZXhhbXBsZQ
```

## 🚀 PASOS PARA CONFIGURAR EN VERCEL

1. **Acceder al Dashboard de Vercel**
   - Ir a: https://vercel.com/dashboard
   - Seleccionar tu proyecto: Manus_NewsAPI

2. **Navegar a la Configuración**
   - Clic en "Settings" (en la parte superior)
   - Seleccionar "Environment Variables" en el menú lateral

3. **Agregar las Variables**
   - Clic en "Add New"
   - Nombre: `APITUBE_API_KEY`
   - Valor: Tu clave de APITube.io
   - Environments: Production, Preview, Development
   - Clic en "Save"

   - Repetir para `SECRET_KEY`

4. **Redeploy del Proyecto**
   - Ir a "Deployments"
   - Clic en "Redeploy" en el deployment más reciente
   - O hacer un nuevo push para trigger automático

## 🌟 VENTAJAS DE APITUBE.IO VS NEWSAPI

| Característica | NewsAPI | APITube.io |
|---|---|---|
| Fuentes | ~80,000 | **500,000+** |
| Países | ~54 | **177** |
| Idiomas | ~14 | **60+** |
| Parámetros | ~10 | **65+** |
| Actualización | 15 min | **Tiempo real** |
| IA Integrada | No | **Sí** |
| Análisis | Básico | **Avanzado** |

## 🔍 VERIFICACIÓN DE LA CONFIGURACIÓN

Una vez configuradas las variables:

1. **Health Check**: https://tu-app.vercel.app/health
2. **Test de API**: https://tu-app.vercel.app/api/news?q=test
3. **Interfaz Web**: https://tu-app.vercel.app/

## 🆘 SOLUCIÓN DE PROBLEMAS

### Error: "La clave de API de APITube.io no está configurada"
- ✅ Verifica que `APITUBE_API_KEY` esté en Environment Variables
- ✅ Verifica que no haya espacios extra
- ✅ Redeploy después de agregar variables

### Error: "Invalid API key"
- ✅ Obtén una nueva clave en https://apitube.io/
- ✅ Verifica que la clave esté activa
- ✅ Revisa los límites de tu plan

### No aparecen resultados
- ✅ Prueba con términos más generales
- ✅ Cambia el idioma/país de búsqueda
- ✅ Verifica tu cuota de APITube.io

## 📞 SOPORTE

- **APITube.io**: https://apitube.io/contact
- **Documentación**: https://docs.apitube.io/
- **Vercel Support**: https://vercel.com/support

---

🚀 **¡Listo para experimentar el poder de 500,000+ fuentes de noticias!**