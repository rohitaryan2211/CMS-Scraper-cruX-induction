# CMS-Scraper-cruX-induction
Python scripts to scrape handouts and files from CMS BPHC.

First, we need to run CMS_course-links_scraper script to collect the links of all courses currently present in the CMS and saves the data in cms_course-links.csv in the same subfolder.
Now, we can scrape handouts by running hanout_scraper.py with links extracted from the previous script.
Here, the script scrapes by logging into the CMS through your BITS mail, so in order to run the script, use your BITS mail credentials in creds.py.
For the demonstration, I am using example-CMS_links.csv as our input which has links for 20 courses extracted from the previous script.
Here's the link for <a href = "https://tinyurl.com/handout-scraping-demonstration" >Video demonstration of the script</a>. 
