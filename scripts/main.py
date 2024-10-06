import requests

class Main:
    def script():
        def urlfetch():
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

        url = 'https://webbrowser11.github.io/backend/banner.txt'
        urlfetch()
        welcome()
        while True:
            user = input("file/command: ")
            if user == "banner":
                url = 'https://webbrowser11.github.io/backend/banner.txt'
                urlfetch()
            elif user == "welcome":
                welcome()
            elif user == "cinnamon":
                url = 'https://webbrowser11.github.io/backend/cinnamon.txt'
                urlfetch()
            elif user == "readme":
                url = 'https://webbrowser11.github.io/backend/README.md'
                urlfetch()
    script()


if __name__ == "__main__":
    Main()
