from flask import Flask, render_template
import requests
import os

# --- Detailed Logging for Vercel Diagnosis ---
print("--- Flask App Script Starting ---")

app = Flask(__name__)

print("Reading environment variable 'NEWS_API_KEY'...")
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

if NEWS_API_KEY:
    # Log a masked version for verification without exposing the full key.
    masked_key = f"{NEWS_API_KEY[:4]}...{NEWS_API_KEY[-4:]}"
    print(f"SUCCESS: NEWS_API_KEY loaded. Key starts with '{masked_key}'.")
else:
    # This is the most likely cause of the crash. This message will appear in Vercel logs.
    print("CRITICAL_ERROR: NEWS_API_KEY environment variable not found or is empty.")
    raise ValueError("CRITICAL: NEWS_API_KEY environment variable is not set.")

NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything'

@app.route('/')
def index():
    print("--- index() route handler triggered ---")
    params = {
        'apiKey': NEWS_API_KEY,
        'q': 'tecnologia',
        'language': 'es'
    }

    articles = []
    error_message = None

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