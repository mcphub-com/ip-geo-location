import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/natkapral/api/ip-geo-location'

mcp = FastMCP('ip-geo-location')

@mcp.tool()
def visitor_lookup(format: Annotated[Union[str, None], Field(description='The desired format of the data. Options: json or xml')] = None,
                   filter: Annotated[Union[str, None], Field(description='Lets you to return only required data. It can be comma separated. Options: asn, city, country, continent, area, currency, security, time, postcode. If left blank the API will return all available data.')] = None,
                   language: Annotated[Literal['en', 'ru', 'zh', 'es', 'ar', 'fr', 'fa', 'ja', 'pl', 'it', 'pt', 'de', None], Field(description='language code to return the results in the specific language. Available options are: en, ru, zh, es, ar, fr, fa, ja, pl, it, pt, de')] = None) -> dict: 
    '''Returns the IP address of the client with all the location data'''
    url = 'https://ip-geo-location.p.rapidapi.com/ip/check'
    headers = {'x-rapidapi-host': 'ip-geo-location.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'format': format,
        'filter': filter,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def iplookup(format: Annotated[Union[str, None], Field(description='The desired format of the data. Options: json or xml')] = None,
             filter: Annotated[Union[str, None], Field(description='Lets you to return only required data. It can be comma separated. Options: asn, city, country, continent, area, currency, security, time, postcode. If left blank the API will return all available data.')] = None,
             language: Annotated[Literal['en', 'ru', 'zh', 'es', 'ar', 'fr', 'fa', 'ja', 'pl', 'it', 'pt', 'de', None], Field(description='language code to return the results in the specific language. Available options are: en, ru, zh, es, ar, fr, fa, ja, pl, it, pt, de')] = None) -> dict: 
    '''Provides geo information for the given IP'''
    url = 'https://ip-geo-location.p.rapidapi.com/ip/23.123.12.11'
    headers = {'x-rapidapi-host': 'ip-geo-location.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'format': format,
        'filter': filter,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
