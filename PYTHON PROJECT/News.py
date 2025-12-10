import requests
import time
import random
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
def speak():
    speaker.speak("What Type Of News You Want")
while True:
    speak()
    if (a:= input("Enter Your Choice : ")) != "Quit":
        l = ["business","entertainment","general","health","science","sports","technology"]
        for i, j in enumerate(l, start=1):
         print(f"{i}: {j}")
        url = f"https://newsapi.org/v2/top-headlines?country=us&sortBy=popularity&category={a}&apiKey=b0b459d0c58a4ea6b7207fd68adaaad4"
        response = requests.get(url)
        data = response.json()
        speaker.speak("How MUch News You Want")
        b = int(input("How MUch News You Want\nEnter Your Choice : "))
        speaker.speak("Here is the latest news")
        articles = data['articles']
                # Shuffle the list of articles
        random.shuffle(articles)
                # Select a random subset of the first 10 articles
        selected_articles = articles[:b]
        for index, article in enumerate(selected_articles, start=1):
            print(f"Title {index}: {article['title']}")
            print("Description:", article['description'])
            print(f"To more Information About This News please press ctrl + click {url}")
            print()

        speaker.speak("How Much Minute To Need To Complete This News")
        a = int(input("How Much Minute To Need : "))
        time.sleep(a*60)
        print(f"Time Completed {a} Minute\nIf You Want To exit Press Quit")
        speaker.speak("If You Want To exit Press Quit")
    else:
        break

# url = "https://newsapi.org/v2/top-headlines?country=in&sortBy=popularity&apiKey=fc63ac1838ba43dfb7c0f2c4237309c8"
# response = requests.get(url)
# data = response.json()
# print(response.status_code)
# print(response.text)
# for article in data['articles'][:10]:
#     print("Title: ", article['title'])
#     print("Description: ", article['description'])
#     print()
