import requests
from bs4 import BeautifulSoup
from . import config

_HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; SearchAgent/1.0)"}
_SEARCH_URL = "https://html.duckduckgo.com/html/"


def web_search(query: str) -> list[dict]:
    """Search DuckDuckGo and return a list of {title, url} results."""
    resp = requests.post(
        _SEARCH_URL, data={"q": query}, headers=_HEADERS, timeout=10
    )
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    return [
        {"title": a.get_text(strip=True), "url": a["href"]}
        for a in soup.select(".result__a")[: config.NUM_RESULTS]
        if a.get("href")
    ]


def fetch_page(url: str) -> str:
    """Fetch a webpage and return cleaned plain text."""
    try:
        resp = requests.get(url, headers=_HEADERS, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        return soup.get_text(separator="\n", strip=True)[: config.MAX_PAGE_CHARS]
    except Exception as e:
        return f"[Failed to fetch {url}: {e}]"
