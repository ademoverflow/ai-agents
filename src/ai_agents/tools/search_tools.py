import json
import os
from typing import TypedDict

import requests
from langchain.tools import tool


class SearchResult(TypedDict):
    """Search Result."""

    title: str
    link: str
    snippet: str


class SearchTools:
    """Search Tools."""

    @staticmethod
    @tool("Search internet")
    def search_internet(query: str) -> list[SearchResult]:
        """Search the internet for a given query and return relevant results.

        Args:
            query (str): Query string

        Returns:
            list[SearchResult]: Search results

        """
        return SearchTools.search(query)

    @staticmethod
    @tool("Search Amazon UAE")
    def search_amazon_uae(query: str) -> list[SearchResult]:
        """Search Amazon UAE for a given query and return relevant results.

        Args:
            query (str): Query string

        Returns:
            str: Search results

        """
        query = f"site:amazon.ae {query}"
        return SearchTools.search(query)

    @staticmethod
    @tool("Search AliBaba")
    def search_alibaba(query: str) -> list[SearchResult]:
        """Search AliBaba for a given query and return relevant results.

        Args:
            query (str): Query string

        Returns:
            list[SearchResult]: Search results

        """
        query = f"site:alibaba.com {query}"
        return SearchTools.search(query)

    @staticmethod
    def search(query: str, n_results: int = 5) -> list[SearchResult]:
        """Search the internet for a given query and return relevant results.

        Args:
            query (str): Query string
            n_results (int, optional): Number of results to return. Defaults to 5.

        Returns:
            list[SearchResult]: Search results

        """
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            "X-API-KEY": os.environ["SERPER_API_KEY"],
            "content-type": "application/json",
        }
        response = requests.request("POST", url, headers=headers, data=payload, timeout=10)
        raw_results = response.json()["organic"]
        return [
            SearchResult(
                title=result["title"],
                link=result["link"],
                snippet=result["snippet"],
            )
            for result in raw_results[:n_results]
        ]
