import json
import os

import requests
from langchain.tools import tool


class SearchTools:
    """Search Tools."""

    @staticmethod
    @tool("Search internet")
    def search_internet(query: str) -> str:
        """Search the internet for a given query and return relevant results.

        Args:
            query (str): Query string

        Returns:
            str: Search results

        """
        return SearchTools.search(query)

    @staticmethod
    @tool("Search Amazon UAE")
    def search_amazon_uae(query: str) -> str:
        """Search Amazon UAE for a given query and return relevant results.

        Args:
            query (str): Query string

        Returns:
            str: Search results

        """
        query = f"site:amazon.ae {query}"
        return SearchTools.search(query)

    @staticmethod
    def search(query: str, n_results: int = 5) -> str:
        """Search the internet for a given query and return relevant results.

        Args:
            query (str): Query string
            n_results (int, optional): Number of results to return. Defaults to 5.

        Returns:
            str: Search results

        """
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            "X-API-KEY": os.environ["SERPER_API_KEY"],
            "content-type": "application/json",
        }
        response = requests.request("POST", url, headers=headers, data=payload, timeout=10)
        results = response.json()["organic"]
        text = []
        for result in results[:n_results]:
            try:
                text.append(
                    "\n".join(
                        [
                            f"Title: {result['title']}",
                            f"Link: {result['link']}",
                            f"Snippet: {result['snippet']}",
                            "\n-----------------",
                        ],
                    ),
                )
            except KeyError:
                continue

        content = "\n".join(text)
        return f"\nSearch result: {content}\n"
