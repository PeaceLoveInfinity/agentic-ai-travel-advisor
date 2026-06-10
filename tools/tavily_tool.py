from tavily import TavilyClient

from config.settings import TAVILY_API_KEY


client = TavilyClient(
    api_key=TAVILY_API_KEY
)


def search_web(query):

    response = client.search(
        query=query,
        max_results=5
    )

    return response