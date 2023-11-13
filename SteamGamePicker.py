import requests
import time
import os

dev_mode = False # Set to True to enable developer mode (just more clutter in the terminal)


api_key = "Enter your steam api key" #https://steamcommunity.com/dev/apikey

username = input("Enter the first steam username: ")

base_url = "https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/"

params = {
    "key": "95C5181B69E73049EB8F1170DF9FC617",
    "vanityurl": username
}

response = requests.get(base_url, params=params).json()

status = response["response"]["success"]

if status == 1:
    steam_id_1 = response["response"]["steamid"]

elif status == 42:
    print(f"Unable to find Steam Account named : {username}")
    print("Please check the spelling and try again.")
    print()
    input("Press Enter to Quit")
    quit()
else:
    print("Something went wrong. Please try again later.")
    print()
    input("Press Enter to Quit")
    quit()




username2 = input("Enter the second steam username: ")

base_url = "https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/"

params = {
    "key": "95C5181B69E73049EB8F1170DF9FC617",
    "vanityurl": username2
}

response = requests.get(base_url, params=params).json()

status = response["response"]["success"]


if status == 1:
    steam_id_2 = response["response"]["steamid"]

elif status == 42:
    print(f"Unable to find Steam Account named : {username2}")
    print("Please check the spelling and try again.")
    print()
    input("Press Enter to Quit")
    quit()

else:
    print("Something went wrong. Please try again later.")
    print()
    input("Press Enter to Quit")
    quit()

print()

if dev_mode == True:   
    print(f"The steam id of {username} is {steam_id_1}")
print('\033[1m' + f"Steam Account Found: {username}" + '\033[0m')

if dev_mode == True:   
    print(f"The steam id of {username2} is {steam_id_2}")
print('\033[1m' + f"Steam Account Found: {username2}" + '\033[0m')



print()
print("Please wait while we request data from steam's servers...")


base_url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"

def get_games(steam_id):
    full_url = base_url + "?key=" + api_key + "&steamid=" + steam_id + "&format=json"

    response = requests.get(full_url)

    if response.status_code == 200:
        data = response.json()

        games = data["response"]["games"]

        game_names = []

        for game in games:
            app_id = game["appid"]

            app_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"

            app_response = requests.get(app_url)

            if app_response.status_code == 200:

                app_data = app_response.json()

                app_name = None
                for app in app_data["applist"]["apps"]:
                    if app["appid"] == app_id:
                        app_name = app["name"]
                        break

                if app_name:
                    game_names.append(app_name)

                else:
                    game_names.append(str(app_id))

            else:
                game_names.append(str(app_id))

        return game_names
    else:

        return []

games_1 = get_games(steam_id_1)

print()
print()
print('\033[1m' + f"The account {username} owns {len(games_1)} games:" + '\033[0m')
if dev_mode == True:
    print(games_1)



games_2 = get_games(steam_id_2)

print()
print('\033[1m' + f"The account {username2} owns {len(games_2)} games:" + '\033[0m')
if dev_mode == True:
    print(games_2)


shared_games = []

for game in games_1:
    if game in games_2:
        shared_games.append(game)

print()
print('\033[1m' + f"The accounts  {username} and {username2} share {len(shared_games)} games:" + '\033[0m')
print(shared_games)
print()

quest = input("Would you like to pick a random game from the shared list? (y/n): ")

if quest == "y" or quest == "Yes" or quest == "yes":
    import random
    print('\033[1m' + f"The accounts  {username} and {username2} share {len(shared_games)} games:" + '\033[0m')
    print(shared_games)
    roll = 1
    while roll == 1:
        print()
        print("Your random game is: ")
        print()
        print('\033[1m' + random.choice(shared_games) + '\033[0m')
        print()
        reroll = input("Would you like to reroll? (y/n): ")
        if reroll == "y" or reroll == "Yes" or reroll == "yes":
            roll = 1
        else:
            roll = 0
        print()
    print("Enjoy!")
    print()
    input("Press Enter to Quit")
    quit()

else:
    print()
    print("Thanks for using the program!")
    print()
    input("Press Enter to Quit")
    quit()

