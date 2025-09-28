from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# This is the most likely point of failure.
# If the app crashes, it's because this environment variable is not set in Vercel.
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
if not NEWS_API_KEY:
    raise ValueError("CRITICAL: NEWS_API_KEY environment variable is not set.")

NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything'

@app.route('/')
def index():
    """
    A simplified route that fetches news for a hardcoded query ('tecnologia')
    and renders them. All complexity has been removed for diagnostics.
    """
    params = {
        'apiKey': NEWS_API_KEY,
        'q': 'tecnologia',
        'language': 'es'
    }

    articles = []
    error_message = None
    try:
        response = requests.get(NEWS_API_BASE_URL, params=params)
        response.raise_for_status() # Raise an exception for bad status codes
        data = response.json()
        articles = data.get("articles", [])
    except requests.exceptions.RequestException as e:
        error_message = f"Error connecting to the News API: {e}"
    except ValueError: # Catches JSON decoding errors
        error_message = "Error decoding the JSON response from the API."

    # Pass only the necessary data to a simplified template
    return render_template('index.html', articles=articles, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')