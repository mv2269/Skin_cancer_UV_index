# Skin Cancer UV Index Analysis

## Description
This project aims to analyze the relationship between UV index data and skin cancer rates across various states in the United States. The data collected through web scraping and API requests will be used to explore potential correlations between UV exposure and skin cancer incidence, ultimately contributing to public awareness regarding skin health and UV protection.This project has enormous potential, we can futher download csv files from https://gco.iarc.who.int/today/en/dataviz/tables, to get cancer data by country and futher compare it to pollution levels as well as UV index levels.

## Data Sources
- **Skin Cancer Rates**: The data on skin cancer rates by state was sourced from [QuoteWizard](https://quotewizard.com/news/skin-cancer-rates-by-state). This website was chosen due to its comprehensive and updated statistics on skin cancer rates, which provide essential insights into the health implications of UV exposure.
- **UV Index Data**: UV index data is obtained from the [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api). This API was selected for its detailed and reliable weather data, including UV index information for various locations.

## Installation and Usage

### Prerequisites
- Python 3.x
- pip (Python package installer)


## How to Run

1. **Clone the Repository**

   - To get started, clone this repository to your local machine:

       git clone https://github.com/mv2269/Skin_cancer_UV_index

       cd Skin_cancer_UV_index

3. **Install Dependencies**

    - Install the required Python libraries using pip. Create a requirements.txt file if you don't have one, with the following content:

        requests

        beautifulsoup4

        python-dotenv

        pandas



    - Then, install the dependencies:

        pip install -r requirements.txt

4. **Run the Script**

    - Execute the script using Python:

        python main.py




