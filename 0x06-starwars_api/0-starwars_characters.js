#!/usr/bin/node
""" Star Wars Characters"""
import sys
import requests

def get_movie_characters(movie_id):
    """prints all characters of a Star Wars movie"""

    url = f"https://swapi.dev/api/films/{movie_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        characters_urls = data['characters']
        for character_url in characters_urls:
            character_response = requests.get(character_url)
            if character_response.status_code == 200:
                character_data = character_response.json()
                print(character_data['name'])
            else:
                print(f"Failed to fetch character data for URL: {character_url}")
    else:
        print(f"Failed to fetch movie data for ID: {movie_id}")

