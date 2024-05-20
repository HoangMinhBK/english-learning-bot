import requests


class NewsAPI:
    @staticmethod
    def get_news_summary(api_key, query="technology"):
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
        response = requests.get(url)
        articles = response.json().get("articles")
        if not articles:
            return ["No news found."]

        summaries = []
        for article in articles[:5]:  # Limiting to 5 articles for brevity
            title = article["title"]
            description = article["description"]
            url = article["url"]
            summaries.append((title, description, url))

        return summaries
