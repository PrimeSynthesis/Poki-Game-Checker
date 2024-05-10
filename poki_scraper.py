import requests
from bs4 import BeautifulSoup
import datetime



def main():

  url = "https://poki.com/"
  filename = "games.txt"
  print("Welcome to the Poki Game Checker")
  header, past_games = read_games(filename)
  current_games = get_games(url)
  if not header:
    print("Game Scan Never Ran")
  else:
    print(header)
  
  new_games, removed_games = check(past_games, current_games)

  if new_games:
    print("New Games Found:")
    for game in new_games:
      print(game)
  else:
    print("No new games have been added last scan")
  if removed_games:
    print("Removed Games:")
    for game in removed_games:
      print(game)
  else:
    print("No game have been removed since last scan")
  
  save_games(filename,current_games)
  print("Game List Updated,Exiting Program")
  quit()

  
  



 
def check(past_games, current_games):
  new_games = list(set(current_games) - set(past_games))
  removed_games = list(set(past_games) - set(current_games))
  return new_games, removed_games

  

# Make  Request to Poki website and processes respond
def get_games(url):
  res = requests.get(url)
  if res.status_code == 200:
    soup = BeautifulSoup(res.text, "html.parser")
    # Looking for just the game titles in on the website
      # <a> tags contains the home button, game titles, categories and other links
      # <span> tags contain the game titles and categories 
      # game titles have href link that contain /en/g/
    links = soup.find_all("a")
    game_list = []
    for link in links:
      if "/en/g/" in link.get("href",""):
        span = link.find_all("span")
        for game_title in span:
          game_list.append(game_title.text)
    return game_list

  else:
    print(f"Request Failed Status Code: {res.status_code}")
    return []


# Saving Game List to File with timestamp
def save_games(filename,game_list):
  with open(filename,"w") as file:
    timestamp = datetime.datetime.now().strftime("%m/%d/%Y,%I:%M:%S %p")
    file.write(f"Game List Last Updated At: {timestamp}\n")
    file.write("_______________________________________________________\n")
    for game in game_list:
      file.write(f"{game}\n")

#Reading games from file to list
def read_games(filename):
  try:
    with open(filename,"r") as file:
      lines = [line.strip() for line in file if line.strip()]
      if (len(lines) < 2 ):
        print("Insufficient data in file.")
        return [], []
      header = lines.pop(0) #  Timestamp stored in the first line
      lines.pop(0)#  Throwawy Line
      return header, lines # Return Header to display and game list for comparsion
      
  except FileNotFoundError:
    print("File is Missing")
    return [], []
  except Exception as e:
    print(f"An error occurred: {e}")

      





  
main()


