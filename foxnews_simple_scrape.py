import pandas as pd
import urllib
import requests
from tqdm import tqdm

URL = 'https://www.foxnews.com/api/article-search?isCategory=true&isTag=false&isKeyword=false&isFixed=false&isFeedUrl=false&contentTypes=%7B"interactive":false,"slideshow":false,"video":false,"article":true%7D'
query = {
    'size': 30, 
    'offset': 0,
    'searchSelected': 'politics'
}

MAX_SIZE = 30
MAX_OFFSET = 10000

res = []
for offset in tqdm(range(0, MAX_OFFSET, MAX_SIZE)):
    query['offset'] = offset
    url = '{}&{}'.format(URL, urllib.parse.urlencode(query))
    response = requests.get(url)
    res.extend(response.json())
    
df = pd.DataFrame(res)
df.to_csv('foxnews.csv', index=False)