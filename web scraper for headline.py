import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_headlines(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []

    # Directly get <a> tags that look like news headlines
    for link in soup.select("a[href]"):
        title = link.get_text(strip=True)

        # Skip empty text or small irrelevant links
        if len(title) < 15:
            continue

        href = link["href"]

        # Make relative links absolute
        full_link = urljoin(url, href)

        headlines.append({"title": title, "url": full_link})

    return headlines


# ------------------------
# Run for BBC
# ------------------------
news_url = "https://www.bbc.com/news"

headlines = get_headlines(news_url)

print("\n--- Headlines ---\n")
for h in headlines[:20]:   # Show only first 20
    print("•", h["title"])
    print("  →", h["url"])
    print()
