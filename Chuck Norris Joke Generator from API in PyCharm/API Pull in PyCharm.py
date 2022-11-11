# API Pull in PyCharm
# Author Wittlieff, Alexa

# import libraries
import requests
import json


# call to API
def chuck():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        data = requests.get(url)
        response = json.loads(data.text)
        print(response["value"])
    except:
        print("Connection Failure")


def main():
    # welcome message to user
    print('Welcome to the Chuck Norris Joke Machine! Here is your first joke!')
    chuck()
    # creating loop
    yes_choice = ['yes', 'Yes', 'YES', 'y', 'Y']
    no_choice = ['no', 'No', 'NO', 'n', 'N']
    prompt = input('\nWould you like another Chuck Norris joke? Type "Yes" to receive another joke or "No" to quit. ')
    prompt = prompt.lower()
    prompt_joke = True
    while prompt_joke:
        if prompt in yes_choice:
            chuck()
            prompt = input(
                '\nWould you like another Chuck Norris joke? Type "Yes" to receive another joke or "No" to quit. ')
        elif prompt in no_choice:
            print('Thank you for using the Chuck Norris Joke Machine!')
            prompt_joke = False
        else:
            print('Invalid entry. Please try again.')
            prompt = input(
                '\nWould you like another Chuck Norris joke? Type "Yes" to receive another joke or "No" to quit. ')


# Define call to main
if __name__ == "__main__":
    main()
