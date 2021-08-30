import requests

def get_quote():
    url = 'https://movie-quote-api.herokuapp.com/v1/quote/'  # alternative API
    response = requests.get(url).json()

    return f"'{response['quote']}' \n> {response['role']}, {response['show']}"


if __name__ == "__main__":
    print(get_quote())
