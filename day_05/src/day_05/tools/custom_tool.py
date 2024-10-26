import os
import requests
import json
from crewai_tools import BaseTool
from dotenv import load_dotenv

load_dotenv()


class CustomSerperDevTool(BaseTool):
    name: str = "Custom Serper Dev Tool"
    description: str = ("Search the internet for news")

    def _run(self, query: str) -> str:
        """ 
            Search the internet for News
        """


        url = "https://google.serper.dev/search"

        payload = json.dumps({
        "q": query,
        "tbs": "qdr:d"
        })
        headers = {
        'X-API-KEY': os.getenv('SERPER_API_KEY'),
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text
