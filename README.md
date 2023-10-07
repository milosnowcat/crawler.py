# crawler.py
 Web Crawler

## Installation of the Crawler.py Project

This project provides a web crawler built with Scrapy that extracts book titles, prices, and availability from a website. To get started using this project, follow the installation steps below.

### Prerequisites

Before installing the project, make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. Clone the GitHub repository to your local machine using the following command:

   ```bash
   git clone https://github.com/milosnowcat/crawler.py.git
   ```

2. Navigate to the `crawler.py` directory:

   ```bash
   cd crawler.py
   ```

3. Install Scrapy using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the spider to start crawling:

   ```bash
   scrapy crawl books
   ```

   This will start the web crawling process and extract book information from the specified website.

That's it! You have successfully installed and executed the Crawler.py project.

---

## Using the Crawler.py Project

The Crawler.py project is a web crawler built with Scrapy that extracts book titles, prices, and availability from a website. Here are the steps for using the project.

### Web Crawling

1. Ensure you have followed the installation steps mentioned in the "Installation of the Crawler.py Project" section.

2. After running the `scrapy crawl books` command, the spider will start crawling the website [http://books.toscrape.com/](http://books.toscrape.com/).

3. The spider follows two rules defined in the `Crawler.py` class:
   - It follows links with "catalogue/category" in the URL.
   - It follows links with "catalogue" in the URL but excludes those with "category." The `parse_item` callback function is used to extract book information from these pages.

4. The extracted information includes book titles, prices, and availability.

5. The crawled data is printed to the console in JSON format.

6. You can customize the spider to save the data to a file, database, or perform other actions as needed.

7. To stop the spider, press `Ctrl + C` in your terminal.

That's it! You have successfully used the Crawler.py project to scrape book information from a website using Scrapy.
