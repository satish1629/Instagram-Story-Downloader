
from flask import Flask, render_template, request, send_file
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = 'downloads/'
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def extract_username(input_text):
    if "instagram.com" in input_text:
        parts = input_text.rstrip('/').split('/')
        return parts[-1]
    return input_text

def scrape_stories(username):
    username = extract_username(username)
    try:
        url = f"https://storiesig.info/en/stories/{username}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        stories = [story['href'] for story in soup.select('.stories-container a') if 'https://' in story['href']]
        
        return stories if stories else ["No stories found or profile is private."]
    
    except Exception as e:
        return [f"Error: {str(e)}"]

def download_story(story_url):
    try:
        response = requests.get(story_url, stream=True)
        filename = os.path.join(DOWNLOAD_FOLDER, story_url.split('/')[-1])
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        
        return filename
    except Exception as e:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    stories = []
    if request.method == 'POST':
        username = request.form['username'].strip()
        stories = scrape_stories(username)
    
    return render_template('index.html', stories=stories)

@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')
    
    if not url:
        return "Invalid URL", 400
    
    filepath = download_story(url)
    
    if filepath:
        return send_file(filepath, as_attachment=True)
    
    return "Failed to download story.", 500

if __name__ == '__main__':
    app.run(debug=True)
