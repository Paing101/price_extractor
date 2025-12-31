# price_extractor
Scrap electronic prices from the e-commerce website (The project is created for educational purpose)

# City Mall Product Scraper
A Python-based web scraper designed to extract product information from the City Mall Myanmar website. This tool iterates through multiple category pages, collects product details, and exports the data into an organized Excel spreadsheet.

# Features
Multi-page Scraping: Automatically loops through 18 pages of products.

Data Extraction: Captures Product Name, Price (as integers), and Seller Status.

Robust Error Handling: Uses custom functions to handle missing data without crashing.

Excel Export: Automatically generates a timestamped .xlsx file.

# Tech Stack
Python 3.14+

BeautifulSoup4 & html5lib: For parsing HTML content.

Requests: For making HTTP connections.

Pandas & Openpyxl: For data manipulation and Excel generation.

# Installation (macOS)
Follow these steps to set up the project on your Mac:

1. Clone the Repository
Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create and Activate Virtual Environment
Bash

python3 -m venv .venv
source .venv/bin/activate
(Your terminal should now show (.venv) at the beginning of the line.)

3. Install Dependencies
Bash

pip install -r requirements.txt

# How to Run
Ensure your virtual environment is active.

Run the script using:

Bash

python "All Pages Extraction_26122025.py"
Once completed, look for a file named Output_HH-MM-SS.xlsx in your project folder.

# Data Preview
The generated Excel file will contain the following columns: | Product Name | Product Price | Product Status | | :--- | :--- | :--- | | Example Item A | 25000 | In Stock | | Example Item B | 12000 | Out of Stock |

# Disclaimer
This project is for educational purposes only. Please ensure you comply with the website's robots.txt and Terms of Service before scraping.

How to add this to GitHub:
In VS Code, create a new file and name it README.md.

Paste the text above into it.

Save the file.

In your terminal, run:

Bash

git add README.md
git commit -m "Add professional README"
git push
