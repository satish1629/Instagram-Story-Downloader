
# Instagram Story Downloader

A simple and efficient Instagram Story Downloader with both **GUI and CLI** support.

## 🚀 Features
- Download public Instagram stories.  
- **GUI Mode:** Modern web interface using Flask.  
- **CLI Mode:** Command-line interface for direct downloads.  
- Dual usage from the terminal or browser.  

---

## ⚙️ Installation

1. **Clone the Repository:**
```
git clone <your-repo-url>
cd instagram_story_downloader
```

2. **Install Dependencies:**
```
pip install -r requirements.txt
```

---

## 🌐 GUI Mode
Run the following command to start the GUI:
```
python app.py
```
- Open your browser and go to:  
```
http://127.0.0.1:5000
```
- Enter the Instagram username and click `Download Stories`.  

---

## 💻 CLI Mode
Download stories directly from the terminal:
```
python downloader.py <username>
```

Example:
```
python downloader.py nasa
```
- The stories will be saved in the `/downloads/` folder.

---

## 📁 Folder Structure
```
/templates  
   └── index.html         # HTML template for GUI  
/static  
   └── styles.css         # CSS styling  
app.py                    # Flask GUI  
downloader.py              # CLI downloader  
requirements.txt           # Dependencies  
README.md                  # Instructions  
/downloads/                 # Folder for saving stories  
```

---

## 🛠️ Tech Stack
- Flask for the GUI  
- Typer for CLI mode  
- BeautifulSoup + requests for web scraping  
- Bootstrap for responsive design  

---

## ✅ Usage Tips
- Use public Instagram accounts for seamless downloads.  
- For private accounts, you'll need authentication (not implemented here).  
- Avoid excessive requests to prevent being temporarily blocked by Instagram.

---

## 📧 Support
If you encounter any issues, feel free to reach out or open a GitHub issue.

---

✅ Happy downloading! 🚀
