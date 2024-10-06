import requests

url = 'https://webbrowser11.github.io/backend/cinnamon.txt'
response = requests.get(url)

if response.status_code == 200:  # Check if the request was successful
    content = response.text  # Get the content of the page
    print(content)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
