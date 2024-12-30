# Image Scraper from Unsplash by   [nouredine_kn](https://www.instagram.com/nouredine_kn)

This project contains a Python script and a Jupyter notebook for scraping images from Unsplash. The scraper uses Selenium WebDriver to automate the process of searching and downloading images based on a given search query. The images are saved locally for further use.

## Requirements

Before running the scripts, make sure you have the following installed:
- Python 3.x
- Chrome WebDriver (make sure it's in your system's PATH)
- Jupyter Notebook (for `script_algorithm.ipynb`)

You can install the required Python libraries by using the `requirements.txt` file.

### Install dependencies:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes the following libraries:
- `selenium`
- `requests`

You can also manually install them using `pip`:

```bash
pip install selenium requests
```

## Files

### `images_scraper.py`
This Python script automates the scraping of images from Unsplash based on a search query. It performs the following actions:
1. Opens the browser and navigates to the search page on Unsplash.
2. Scrolls through the page to load more images.
3. Collects unique image URLs.
4. Saves the images in a folder named after the search query.

#### How to use:
- Modify the `search_query`, `countPage`, and `totalImages` variables to scrape images for your specific needs.
- The images will be saved in the `images/<search_query>` folder.

### `script_algorithm.ipynb`
This Jupyter notebook demonstrates how to scrape images from Unsplash in an interactive environment. The notebook contains:
- Initialization of the WebDriver
- Execution of the scraping logic
- Image downloading after removing duplicates

#### Steps:
1. **Cell 1**: Import necessary libraries.
2. **Cell 2**: Define the search query and number of pages to scrape.
3. **Cell 3**: Initialize Selenium WebDriver and navigate to the Unsplash search page.
4. **Cell 4**: Scroll the page, collect image URLs, and count them.
5. **Cell 5**: Remove duplicate images.
6. **Cell 6**: Create a folder to save the images and download them.

## How to Run

### Using `images_scraper.py`
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/nouredinekn/Image_Scraper_Nouredine_kn.git
   cd Image_Scraper_Nouredine_kn
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python images_scraper.py
   ```

4. The images will be saved in the `images/<search_query>` folder.

### Using `script_algorithm.ipynb`
1. Open the notebook in Jupyter:
   ```bash
   jupyter notebook script_algorithm.ipynb
   ```

2. Run the cells step by step to scrape images interactively.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

## Social Media
- [Telegram](https://t.me/nouredine_kn)
- [Instagram](https://www.instagram.com/nouredine_kn)
