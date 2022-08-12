#!/usr/bin/python3

import requests
import crayons
from tkinter import *
from datetime import datetime

#get date time
today = datetime.date(datetime.now())

# getting api for news.cred file
def return_news_creds():
    with open("/home/student/news.cred", "r") as news_creds:
        news_creds = news_creds.read()

    news_creds = "apiKey=" + news_creds.strip("\n")
    return news_creds


api_key = return_news_creds()



def get_news(topic, from_date=today, to_date=today, language="en",
             api_key=return_news_creds()):
    NEWSURL = requests.get(
        f"https://newsapi.org/v2/everything?q={topic}&from_param={from_date}&to={to_date}&language={language}&{api_key}")

    data = NEWSURL.json()
    articles = data["articles"]

    articles_collection = []

    for article in articles:
        print(f"""
            Title: {crayons.blue(article['title'])}

            Description: {article['description']}

            Url: {crayons.green(article["url"])}

        """)



window = Tk()
window.title("Query News Api")
window.geometry('400x300')

#Display label
topic_label = Label(window, text="Enter topic:", fg='blue', font=('Arial', 14))
topic_label.grid(row=0, column=0, padx=5, pady=10)

#Display  from date label
topic_label = Label(window, text="Start date:", fg='blue', font=('Arial', 14))
topic_label.grid(row=2, column=0, padx=5, pady=10)

#Display  from date label
end_date_label = Label(window, text="End date:", fg='blue', font=('Arial', 14))
end_date_label.grid(row=3, column=0, padx=5, pady=10)

#Display  language label
end_date_label = Label(window, text="Language:", fg='blue', font=('Arial', 14))
end_date_label.grid(row=4, column=0, padx=5, pady=10)

topic=StringVar()

#White box to enter text for topic
topic_entry = Entry(window, textvariable=topic, fg='blue', font=('Arial', 14))
topic_entry.grid(row=0,column=1)
print(topic_entry.get())

start=StringVar()
#BOX TO ENTER START DATE
start_date_entry = Entry(window, textvariable=start, fg='blue', font=('Arial', 14))
start_date_entry.grid(row=2,column=1)

end=StringVar()
#BOX TO ENTER End DATE
end_date_entry = Entry(window, textvariable=end, fg='blue', font=('Arial', 14))
end_date_entry.grid(row=3,column=1)

lang=StringVar()
#Language
language_entry = Entry(window, textvariable=lang, fg='blue', font=('Arial', 14))
language_entry.grid(row=4,column=1)








button=Button(window, text='Submit', fg='blue', command= lambda:get_news(topic_entry.get(),start_date_entry.get(),end_date_entry.get(),language_entry.get()) , font=('Arial', 14))
button.grid(row=5,column=1, sticky=W)





def main():
    window.mainloop()


if __name__ == "__main__":
    main()

