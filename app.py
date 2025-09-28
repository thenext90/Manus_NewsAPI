from flask import Flask, render_template
import requests
import os

# --- Detailed Logging for Vercel Diagnosis ---
print("--- Flask App Script Starting ---")

app = Flask(__name__)

# We will read the environment variable inside the request context
# to avoid crashing the app at startup if the key is missing.
NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything'

@app.route('/')
def index():
    print("--- index() route handler triggered ---")

    # Get the API key from environment variables
    api_key = os.getenv('NEWS_API_KEY')
    articles = []
    error_message = None

    # If the API key is missing, show a user-friendly error on the page
    if not api_key:
        error_message = "Error: La variable de entorno NEWS_API_KEY no está configurada. Por favor, añádela en la configuración de tu proyecto en Vercel para poder obtener las noticias."
        print("CRITICAL_ERROR: NEWS_API_KEY environment variable not found or is empty.")
        return render_template('index.html', articles=articles, error_message=error_message)

    # Log a masked version for verification without exposing the full key.
    masked_key = f"{api_key[:4]}...{api_key[-4:]}"
    print(f"SUCCESS: NEWS_API_KEY loaded. Key starts with '{masked_key}'.")

    params = {
        'apiKey': api_key,
        'q': 'tecnologia',
        'language': 'es'
    }

    print(f"Making request to News API: {NEWS_API_BASE_URL}")
    try:
        response = requests.get(NEWS_API_BASE_URL, params=params)
        print(f"API Response Status: {response.status_code}")
        response.raise_for_status()
        data = response.json()
        articles = data.get("articles", [])
        print(f"API call successful, {len(articles)} articles found.")
    except requests.exceptions.RequestException as e:
        error_message = f"Error connecting to the News API: {e}"
        print(f"ERROR during API request: {e}")
    except ValueError:
        error_message = "Error decoding the JSON response from the API."
        print("ERROR decoding JSON from API response.")

    print("--- Rendering template ---")
    return render_template('index.html', articles=articles, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')