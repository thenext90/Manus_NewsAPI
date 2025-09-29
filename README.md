# 🔍 Buscador de Noticias Preciso

Un buscador de noticias moderno y eficiente que utiliza la API de NewsAPI para proporcionar resultados precisos y relevantes.

## ✨ Características

- **Búsquedas precisas**: Sistema optimizado para encontrar noticias relevantes
- **Filtros avanzados**: Por categoría, fuentes específicas, idioma y palabras clave
- **Interfaz moderna**: Diseño responsivo y fácil de usar
- **API endpoints**: Acceso programático a los datos
- **Optimizado para Vercel**: Deploy rápido y eficiente

## 🚀 Deploy en Vercel

### 1. Configura las variables de entorno en Vercel:

```bash
NEWS_API_KEY=tu_clave_de_newsapi_aqui
SECRET_KEY=una_clave_secreta_segura
```

### 2. Conecta tu repositorio a Vercel

1. Ve a [Vercel Dashboard](https://vercel.com/dashboard)
2. Haz clic en "Import Project"
3. Conecta tu repositorio de GitHub
4. Vercel detectará automáticamente que es un proyecto Python/Flask

### 3. Variables de entorno requeridas:

- `NEWS_API_KEY`: Tu clave de API de NewsAPI (obtén una gratis en [newsapi.org](https://newsapi.org/))
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
export NEWS_API_KEY=tu_clave_aqui
export SECRET_KEY=tu_clave_secreta

# Ejecuta la aplicación
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## 📱 Uso de la Aplicación

### Búsqueda Web
1. Accede a la página principal
2. Usa las palabras clave específicas para búsquedas precisas
3. Filtra por categoría, fuentes o idioma
4. Obtén resultados relevantes y actualizados

### API Endpoints

#### Obtener Noticias
```
GET /api/news?q=tecnologia&language=es&category=technology
```

#### Obtener Fuentes Disponibles
```
GET /api/sources?language=es
```

#### Health Check
```
GET /health
```

## 💡 Consejos para Búsquedas Precisas

1. **Usa términos específicos**: En lugar de "noticias", usa "inteligencia artificial", "cambio climático"
2. **Combina filtros**: Usa categoría + palabras clave para mejores resultados
3. **Fuentes confiables**: Filtra por fuentes específicas como `bbc-news,cnn,reuters`
4. **Idiomas múltiples**: Cambia el idioma para acceder a más fuentes

## 🔧 Configuración Avanzada

### Fuentes Populares por Idioma:

- **Español**: `efe`, `el-pais`, `abc-es`, `marca`
- **Inglés**: `bbc-news`, `cnn`, `reuters`, `associated-press`
- **Francés**: `le-monde`, `le-figaro`, `liberation`

### Categorías Disponibles:
- General, Negocios, Entretenimiento, Salud, Ciencia, Deportes, Tecnología

## 📂 Estructura del Proyecto

```
Manus_NewsAPI/
├── app.py              # Aplicación Flask principal
├── templates/
│   └── index.html      # Interfaz web
├── requirements.txt    # Dependencias Python
├── vercel.json        # Configuración de Vercel
└── README.md          # Este archivo
```

## 🐛 Solución de Problemas

### Error: "La clave de API de noticias no está configurada"
- Verifica que `NEWS_API_KEY` esté configurada correctamente en Vercel
- Asegúrate de que la clave sea válida en [newsapi.org](https://newsapi.org/)

### No aparecen resultados
- Intenta con términos más generales
- Verifica que el idioma seleccionado tenga fuentes disponibles
- Revisa los límites de tu plan de NewsAPI

### Errores de deployment en Vercel
- Verifica que todas las dependencias estén en `requirements.txt`
- Revisa los logs de build en el dashboard de Vercel
- Asegúrate de que las variables de entorno estén configuradas

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

## 🤝 Contribuir

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

¿Necesitas ayuda? [Crea un issue](https://github.com/tu-usuario/Manus_NewsAPI/issues) en el repositorio.