import requests

url = 'https://webbrowser11.github.io/backend/banner.txt'
urlfetch()
class Main:
    def urlfetch()
        response = requests.get(url)
        
        content = response.text  # Get the content of the page
        print(content)
    
    def welcome():
        print("you reached the webbrwoser11 BACKEND!")
        print("here is a list of files you can open view now:")
        print("cinnamon")
        print("readme")
        print("or enter a command:")
        print("banner - show the banner")
        print("welcome - shows the welcome message")
    
    def script()
        input = input("file/command: ")
        if input == "banner":
            url = 'https://webbrowser11.github.io/backend/banner.txt'
            urlfetch()
        elif input == "welcome":
            welcome()
        elif input == "cinnamon":
            url = 'https://webbrowser11.github.io/backend/cinnamon.txt'
            urlfetch()
        elif input == "readme":
            url = 'https://webbrowser11.github.io/backend/readme.md'
            urlfetch()


if __name__ == "__main__":
    Main()
