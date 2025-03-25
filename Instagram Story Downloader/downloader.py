
import requests
from bs4 import BeautifulSoup
import os
import typer

app = typer.Typer()

# Folder to save downloaded stories
DOWNLOAD_FOLDER = 'downloads'
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def extract_username(input_text):
    """Extracts the username from a full Instagram URL or returns the input if it's just the username."""
    if "instagram.com" in input_text:
        parts = input_text.rstrip('/').split('/')
        return parts[-1]
    return input_text

def scrape_stories(username):
    """Scrapes public Instagram stories."""
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
        
        if not stories:
            print("No stories found or the profile might be private.")
            return []
        
        return stories
    
    except Exception as e:
        print(f"Error: {e}")
        return []

def download_story(story_url):
    """Downloads a story by URL."""
    try:
        response = requests.get(story_url, stream=True)
        filename = os.path.join(DOWNLOAD_FOLDER, story_url.split('/')[-1])
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        
        print(f"Downloaded: {filename}")
    
    except Exception as e:
        print(f"Failed to download: {e}")

@app.command()
def download(username: str):
    """Download Instagram stories from a public profile."""
    stories = scrape_stories(username)
    
    if stories:
        for story in stories:
            download_story(story)
    else:
        print("No stories found.")

if __name__ == '__main__':
    app()
