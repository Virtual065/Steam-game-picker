
import requests
import time
import os

dev_mode = False

os.system('clear')

api_key = "95C5181B69E73049EB8F1170DF9FC617"

# Ask for the steam username
username = input("Enter the first steam username: ")

# Define the base URL for the Steam API
base_url = "https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/"

# Define the parameters for the API request
params = {
    "key": "95C5181B69E73049EB8F1170DF9FC617", # Replace this with your own key
    "vanityurl": username # The username to look up
}

# Make the API request and get the response as a JSON object
response = requests.get(base_url, params=params).json()

# Check the response status
status = response["response"]["success"]

# If the status is 1, the steam id is found
if status == 1:
    # Save the steam id as a variable
    steam_id_1 = response["response"]["steamid"]
    # Print the steam id
    if dev_mode == True:   
        print(f"The steam id of {username} is {steam_id_1}")
    print('\033[1m' + f"Steam Account Found: {username}" + '\033[0m')
# If the status is 42, the steam id is not found
elif status == 42:
    # Print an error message
    print(f"Unable to find Steam Account named : {username}")
    print("Please check the spelling and try again.")
    time.sleep(3)
    quit()
# If the status is anything else, something went wrong
else:
    # Print a generic error message
    print("Something went wrong. Please try again later.")
    time.sleep(3)
    quit()




username2 = input("Enter the second steam username: ")

# Define the base URL for the Steam API
base_url = "https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/"

# Define the parameters for the API request
params = {
    "key": "95C5181B69E73049EB8F1170DF9FC617", # Replace this with your own key
    "vanityurl": username2 # The username to look up
}

# Make the API request and get the response as a JSON object
response = requests.get(base_url, params=params).json()

# Check the response status
status = response["response"]["success"]


# If the status is 1, the steam id is found
if status == 1:
    # Save the steam id as a variable
    steam_id_2 = response["response"]["steamid"]
    # Print the steam id
# If the status is 42, the steam id is not found
elif status == 42:
    # Print an error message
    print(f"Unable to find Steam Account named : {username2}")
    print("Please check the spelling and try again.")
    time.sleep(3)
    quit()
# If the status is anything else, something went wrong
else:
    # Print a generic error message
    print("Something went wrong. Please try again later.")
    time.sleep(3)
    quit()


os.system('clear')
if dev_mode == True:   
    print(f"The steam id of {username} is {steam_id_1}")
print('\033[1m' + f"Steam Account Found: {username}" + '\033[0m')

if dev_mode == True:   
    print(f"The steam id of {username2} is {steam_id_2}")
print('\033[1m' + f"Steam Account Found: {username2}" + '\033[0m')



print()
print("Please wait while we request data from steam's servers...")

















# Define the base URL for the API request
base_url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"

# Define a function to get the list of games owned by a steam ID
def get_games(steam_id):
    # Construct the full URL with the parameters
    full_url = base_url + "?key=" + api_key + "&steamid=" + steam_id + "&format=json"

    # Send a GET request and get the response
    response = requests.get(full_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()

        # Get the list of games owned
        games = data["response"]["games"]

        # Create an empty array to store the game names
        game_names = []

        # Loop through the games and append their names to the array
        for game in games:
            # Get the app ID of the game
            app_id = game["appid"]

            # Define the URL for the app name request
            app_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"

            # Send a GET request and get the app name response
            app_response = requests.get(app_url)

            # Check if the app name request was successful
            if app_response.status_code == 200:
                # Parse the app name response as JSON
                app_data = app_response.json()

                # Search for the app name that matches the app ID
                app_name = None
                for app in app_data["applist"]["apps"]:
                    if app["appid"] == app_id:
                        app_name = app["name"]
                        break

                # If the app name is found, append it to the array
                if app_name:
                    game_names.append(app_name)
                # If the app name is not found, use the app ID as the name instead
                else:
                    game_names.append(str(app_id))
            # If the app name request was not successful, use the app ID as the name instead
            else:
                game_names.append(str(app_id))

        # Return the array of game names
        return game_names
    else:
        # Return an empty array
        return []

# Ask for the first steam ID
#steam_id_1 = input("Enter the first steam ID: ")

# Get the list of games owned by the first steam ID
games_1 = get_games(steam_id_1)

# Print the number and list of games owned by the first steam ID
os.system('clear')
print('\033[1m' + f"The account {username} owns {len(games_1)} games:" + '\033[0m')
if dev_mode == True:
    print(games_1)




# Ask for the second steam ID
#steam_id_2 = input("Enter the second steam ID: ")

# Get the list of games owned by the second steam ID
games_2 = get_games(steam_id_2)

# Print the number and list of games owned by the second steam ID
print()
print('\033[1m' + f"The account {username2} owns {len(games_2)} games:" + '\033[0m')
if dev_mode == True:
    print(games_2)


# Create an empty array to store the games shared by both steam IDs
shared_games = []

# Loop through the games owned by the first steam ID
for game in games_1:
    # Check if the game is also owned by the second steam ID
    if game in games_2:
        # Append the game to the shared games array
        shared_games.append(game)

# Print the number and list of games shared by both steam IDs
print()
print('\033[1m' + f"The accounts  {username} and {username2} share {len(shared_games)} games:" + '\033[0m')
print(shared_games)
print()

quest = input("Would you like to pick a random game from the shared list? (y/n): ")

if quest == "y" or quest == "Yes" or quest == "yes":
    import random
    os.system('clear')
    print('\033[1m' + f"The accounts  {username} and {username2} share {len(shared_games)} games:" + '\033[0m')
    print(shared_games)
    print()
    print("Your random game is: ")
    print()
    print('\033[1m' + random.choice(shared_games) + '\033[0m')
    print()
    print("Enjoy!")
    print()
    time.sleep(3)
    quit()

else:
    print()
    print("Thanks for using the program!")
    print()
    time.sleep(3)
    quit()