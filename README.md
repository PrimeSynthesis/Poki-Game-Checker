# Poki Game Tracker

The Poki Game Tracker is a Python script designed to scrape and track video game listings from the [Poki website](https://poki.com/). It helps users to identify new and removed games by comparing current game listings with previous records stored locally.

## Features

- **Scrape Games**: Automatically fetches the current game listings from Poki.
- **Track Changes**: Compares the latest game listings to previously stored data to identify newly added and recently removed games.
- **Local Storage**: Saves game listings with timestamps to track historical data.

## Requirements

- Python 3.6+
- BeautifulSoup4
- requests

## How It Works

- The script sends a GET request to the Poki website to fetch the HTML content.
- It parses the HTML content to extract the game titles using BeautifulSoup.
- It compares the extracted titles to the titles saved in a local file from the previous run.
- The script outputs the new and removed games and updates the local file with the current game listings.
