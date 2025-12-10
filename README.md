# web-scraper-for-headlines

A lightweight Python script to fetch news headlines from one or more news websites using requests + BeautifulSoup. It parses and displays the headline title, URL, and (if available) publish time. Results can be saved to JSON or CSV. The scraper respects robots.txt, supports polite delays and error handling, and optionally filters headlines by keyword.
## Features

* Fetch headlines (title + URL) from one or multiple news sources
* Attempt to extract publish time when available
* Save results to *JSON* or *CSV*
* Respect robots.txt rules and support configurable delays
* Robust error handling and retry mechanism
* Optional keyword filtering (include/exclude)
* Configurable per-site CSS selectors for higher accuracy
* Command-line interface for easy usage

 ## Usage
Basic usage (script: scraper.py):

bash
python scraper.py --source https://www.bbc.com/news --output headlines.json

## output
-- Headlines ---

• Skip to content
  → https://www.bbc.com/news#main-content

• British Broadcasting Corporation
  → https://www.bbc.com/

• Israel-Gaza War
  → https://www.bbc.com/news/topics/c2vdnvdg6xxt

• Israel-Gaza War
  → https://www.bbc.com/news/topics/c2vdnvdg6xxt

• N. Ireland Politics
  → https://www.bbc.com/news/northern_ireland/northern_ireland_politics

• Scotland Politics
  → https://www.bbc.com/news/scotland/scotland_politics

• Executive Lounge
  → https://www.bbc.com/business/executive-lounge

• Technology of Business
  → https://www.bbc.com/business/technology-of-business

• Future of Business
  → https://www.bbc.com/business/future-of-business

• Science & Health
  → https://www.bbc.com/innovation/science

• Artificial Intelligence
  → https://www.bbc.com/innovation/artificial-intelligence

• Entertainment News
  → https://www.bbc.com/culture/entertainment-news

• Australia and Pacific
  → https://www.bbc.com/travel/destinations/australia-and-pacific

• Caribbean & Bermuda
  → https://www.bbc.com/travel/destinations/caribbean

• Central America
  → https://www.bbc.com/travel/destinations/central-america

• Culture & Experiences
  → https://www.bbc.com/travel/cultural-experiences

• Natural Wonders
  → https://www.bbc.com/future-planet/natural-wonders

• Weather & Science
  → https://www.bbc.com/future-planet/weather-science

• Climate Solutions
  → https://www.bbc.com/future-planet/solutions

• Sustainable Business
  → https://www.bbc.com/future-planet/sustainable-business

