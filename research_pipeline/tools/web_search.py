from serpapi import GoogleSearch
import os

async def web_search(query: str):
    """Finds general knowledge information using Google search."""
    print(">>> web_search")
    search = GoogleSearch({
        "engine": "google",
        "api_key": os.getenv("SERPAPI_KEY"),
        "q": query,
        "num": 5
    })
    results = search.get_dict()["organic_results"]
    contexts = "\n---\n".join(
        ["\n".join([x["title"], x["snippet"], x["link"]]) for x in results]
    )
    return contexts