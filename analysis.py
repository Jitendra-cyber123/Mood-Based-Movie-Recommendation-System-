import requests
from bs4 import BeautifulSoup
import re


URLS = {
    "Drama": ' https://www.imdb.com/list/ls056451874/',
    "Action": ' https://www.imdb.com/list/ls052745924/',
    "Comedy": ' https://www.imdb.com/list/ls056781270/',
    "Horror": ' https://www.imdb.com/list/ls080422325/',
    "Crime": ' https://www.imdb.com/list/ls098198962/',
    "Motivational": ' https://www.imdb.com/list/ls008221629/',
    "Love story": '  https://www.imdb.com/list/ls098392303/?sort=popularity%2Casc',
    "Sad": '   https://www.imdb.com/list/ls049587868/',



    
}

def main(emotion):
    url = URLS.get(emotion)
    print("ok", url)
    if not url:
        print("Invalid emotion.")
        return []

    headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    soup = BeautifulSoup(response.text, "lxml")

    
    titles = [a.get_text() for a in soup.find_all('a', href=re.compile(r'/title/tt\d+/'))]
    return titles


if __name__ == '__main__':
    emotion = input("Enter the emotion: ").strip()
    movie_titles = main(emotion)

    if not movie_titles:
        print("No titles found.")
    else:
        max_titles = 14 if emotion in ["Drama", "Action", "Comedy", "Horror", "Crime"] else 12
        for title in movie_titles[:max_titles]:
            print(title)
