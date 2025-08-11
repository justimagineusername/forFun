# List.am Selenium Scraper

## Requirements

- Python 3.7+  
- GeckoDriver (Firefox) installed and in PATH  
- Install dependencies with `pip install -r requirements.txt`

## Usage

1. Activate your virtual environment  
2. Install dependencies  
3. Run `selenium_scraper.py`  
4. The final result will be saved in `list_am_selenium_posts.csv`

## More detailed 

1. Clone the repo
git clone https://github.com/justimagineusername/forFun
cd YourRepo
2. Create and activate a Python virtual environment
On Linux/macOS:
python3 -m venv venv
source venv/bin/activate
On Windows PowerShell:
python -m venv venv
.\venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Make sure you have the right WebDriver installed and in your PATH
If you use Firefox, download GeckoDriver, extract it, and place the executable somewhere in your system PATH (e.g., /usr/local/bin on Linux/macOS or add to PATH on Windows).

check with
geckodriver --version

5. Run the main scraper script

python3 selenium_scraper.py
6. Check the output CSV file
After the scraper runs successfully, you should see a file named list_am_selenium_posts.csv with the scraped posts data.
---
