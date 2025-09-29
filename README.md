# 🌐 APITube.io News Explorer

Un explorador de noticias avanzado y potente que utiliza la API de **APITube.io** para acceder a más de **500,000 fuentes globales verificadas** y proporcionar búsquedas súper precisas.

## ✨ Características Avanzadas

- **🌍 Cobertura Global**: Más de 500,000 fuentes de 177 países
- **🔍 Búsquedas Inteligentes**: 65+ parámetros de filtrado disponibles
- **⚡ Tiempo Real**: Actualizaciones instantáneas de noticias
- **🎯 Filtros Avanzados**: Por país, categoría, idioma y palabras clave
- **🎨 Interfaz Moderna**: Diseño responsivo con animaciones suaves
- **🔌 API REST**: Endpoints para acceso programático
- **🚀 Optimizado para Vercel**: Deploy rápido y eficiente

## 🚀 Deploy en Vercel

### 1. Configura las variables de entorno en Vercel:

```bash
APITUBE_API_KEY=tu_clave_de_apitube_aqui
SECRET_KEY=una_clave_secreta_segura
```

### 2. Conecta tu repositorio a Vercel

1. Ve a [Vercel Dashboard](https://vercel.com/dashboard)
2. Haz clic en "Import Project"
3. Conecta tu repositorio de GitHub
4. Vercel detectará automáticamente que es un proyecto Python/Flask

### 3. Variables de entorno requeridas:

- `APITUBE_API_KEY`: Tu clave de API de APITube.io (obtén una gratis en [apitube.io](https://apitube.io/))
- `SECRET_KEY`: Una clave secreta para Flask (genera una segura)

## 🛠️ Desarrollo Local

### Prerrequisitos:
- Python 3.8+
- pip

### Instalación:

```bash
# Clona el repositorio
git clone <tu-repositorio>
cd Manus_NewsAPI

# Instala las dependencias
pip install -r requirements.txt

# Configura las variables de entorno
export APITUBE_API_KEY=tu_clave_aqui
export SECRET_KEY=tu_clave_secreta

# Ejecuta la aplicación
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## 📱 Uso de la Aplicación

### Explorador Web
1. Accede a la página principal
2. **Búsqueda específica**: Usa términos precisos como "blockchain", "COVID-19", "inteligencia artificial"
3. **Filtros avanzados**: Combina país, categoría e idioma
4. **500,000+ fuentes**: Accede a la red de noticias más grande del mundo
5. **Tiempo real**: Obtén las noticias más recientes al instante

### API Endpoints

#### Obtener Noticias
```
GET /api/news?q=blockchain&language=es&country=es&category=technology
```

#### Obtener Categorías Disponibles
```
GET /api/categories
```

#### Obtener Países Disponibles
```
GET /api/countries
```

#### Health Check
```
GET /health
```

## 🌟 Ventajas de APITube.io vs Otras APIs

| Característica | APITube.io | NewsAPI | Otros |
|---|---|---|---|
| **Fuentes** | 500,000+ | ~80,000 | Limitadas |
| **Países** | 177 | ~54 | Pocos |
| **Idiomas** | 60+ | ~14 | Básicos |
| **Parámetros** | 65+ | ~10 | Limitados |
| **Actualización** | Tiempo real | 15 min | Lenta |
| **Análisis** | IA integrada | Básico | No |

## 💡 Ejemplos de Búsquedas Avanzadas

### 🔬 Ciencia y Tecnología
- `inteligencia artificial + machine learning`
- `blockchain + criptomonedas + DeFi`
- `cambio climático + sostenibilidad`

### 📈 Negocios y Finanzas
- `startups + financiamiento + venture capital`
- `mercados financieros + bolsa + inversiones`
- `economía digital + e-commerce`

### 🌍 Noticias Globales
- `política internacional + diplomacia`
- `crisis humanitaria + ayuda internacional`
- `elecciones + democracia + votaciones`

## 🔧 Configuración Avanzada

### Países Disponibles:
- **América**: Estados Unidos, México, Argentina, Colombia, Perú, Chile, Brasil
- **Europa**: España, Reino Unido, Francia, Alemania, Italia
- **Asia**: China, Japón, India, Corea del Sur
- **Y 160+ países más...**

### Categorías Disponibles:
- General, Negocios, Entretenimiento, Salud
- Ciencia, Deportes, Tecnología, Política
- Finanzas, Educación, Viajes, Comida, Estilo de vida

### Idiomas Soportados:
- Español, Inglés, Francés, Alemán, Italiano
- Portugués, Ruso, Chino, Japonés, Árabe
- **Y 50+ idiomas más...**

## 📂 Estructura del Proyecto

```
Manus_NewsAPI/
├── app.py              # Aplicación Flask con APITube.io
├── templates/
│   └── index.html      # Interfaz web moderna
├── requirements.txt    # Dependencias Python
├── runtime.txt        # Versión de Python
├── vercel.json        # Configuración de Vercel
├── verify.py          # Script de verificación
└── README.md          # Este archivo
```

## 🐛 Solución de Problemas

### Error: "La clave de API de APITube.io no está configurada"
- Verifica que `APITUBE_API_KEY` esté configurada en Vercel
- Obtén una clave válida en [apitube.io](https://apitube.io/)
- Revisa que no haya espacios extra en la clave

### No aparecen resultados
- Intenta con términos más generales o específicos
- Verifica que el país/idioma seleccionado tenga contenido
- Revisa los límites de tu plan de APITube.io
- Combina diferentes filtros para mejores resultados

### Errores de deployment en Vercel
- Verifica que `APITUBE_API_KEY` esté configurada en las variables de entorno
- Revisa los logs de build en el dashboard de Vercel
- Asegúrate de que todas las dependencias estén en `requirements.txt`

## 🆚 APITube.io vs NewsAPI

### ¿Por qué cambiar a APITube.io?

1. **📊 Más Datos**: 500,000+ fuentes vs ~80,000
2. **🌍 Mayor Cobertura**: 177 países vs ~54
3. **🎯 Más Preciso**: 65+ filtros vs ~10
4. **⚡ Más Rápido**: Tiempo real vs 15 minutos
5. **🤖 IA Integrada**: Análisis automático de sentimientos
6. **💰 Mejor Precio**: Más características por el mismo costo

## 📊 Estadísticas de APITube.io

- **Total de fuentes**: 504,519k+
- **Artículos totales**: 3.69 mil millones
- **Países cubiertos**: 177
- **Idiomas disponibles**: 60+
- **Actualizaciones diarias**: 78,979+ artículos nuevos

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

## 🤝 Contribuir

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add APITube.io integration'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 🔗 Enlaces Útiles

- **APITube.io**: https://apitube.io/
- **Documentación API**: https://docs.apitube.io/
- **Dashboard Vercel**: https://vercel.com/dashboard
- **Query Builder**: https://docs.apitube.io/platform/news-api/query-builder
- **Postman Collection**: https://www.postman.com/apitube/apitube/overview

---

🚀 **¡Experimenta el poder de 500,000+ fuentes de noticias globales con APITube.io!** 

¿Necesitas ayuda? [Crea un issue](https://github.com/tu-usuario/Manus_NewsAPI/issues) o contacta al soporte de [APITube.io](https://apitube.io/contact).