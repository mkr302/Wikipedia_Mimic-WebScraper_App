### libraries utilized
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from PIL import ImageTk, Image
from time import sleep

# Tkinter window initialization
WebScraper = tk.Tk()

#Tkinter elements initialization
textbox1 = tk.Text(WebScraper, width=50, height=1, bd=5, bg='white', font = ("Helvetica", 16), relief ='raised')
textbox1.place(x=40,y=50)

myFont1 = font.Font(family='Helvetica', weight='bold')

btn1_Set = tk.Button(WebScraper, text="Search Wiki", bd=5, width=15, height=1, bg="black", fg="white",
                       command=lambda:userinput())
btn1_Set['font'] = myFont1
btn1_Set.place(x = 100, y = 100)

btn2_Set = tk.Button(WebScraper, text="Clear Search", bd=5, width=15, height=1, bg="black", fg="white",
                       command=lambda:clearsearch(textbox1))
btn2_Set['font'] = myFont1
btn2_Set.place(x = 430, y = 100)

separator1_style = ttk.Style()
separator1_style.configure("Line.TSeparator", bg="black")
separator1= ttk.Separator(WebScraper, orient='horizontal')
separator1.place(x=0, y=200, height=380, width=695)

textbox2 = tk.Text(WebScraper, width=35, height=1, bd=5, bg='light blue', font = ("Helvetica", 14), relief ='raised')
textbox2.place(x=150,y=230)

textbox3 = tk.Text(WebScraper, width=100, height=13, bd=5, bg='light grey', font = ("Helvetica", 8), relief ='raised')
textbox3.place(x=50,y=280)

textbox4 = tk.Text(WebScraper, width=86, height=1, bd=5, bg='light blue', font = ("Helvetica", 10), relief ='raised')
textbox4.place(x=50,y=500)

separator2= ttk.Separator(WebScraper, orient='horizontal') 
separator2.place(x=0, y=580, width=695, height=1)

textbox5 = tk.Text(WebScraper, width=26, height=1, bg = 'burlywood', font = ("Helvetica", 8))
textbox5.config(highlightthickness = 0, borderwidth=0)
textbox5.place(x=250,y=583)
textbox5.insert('1.0', 'Copyright @ github.com/mkr302')
textbox5.configure(state='disabled')

def clearsearch(textboxn):
    
    """
    Clear the respective text boxes as per the click button
    """
    
    textboxn.delete("1.0","end")

def userinput():
    #user_input = input("Please enter the search term: ")
    user_input = textbox1.get("1.0","end").strip()
    if len(user_input) == 0:
        textbox1.delete("1.0","end")
        textbox2.delete("1.0","end")
        textbox3.delete("1.0","end")
        textbox4.delete("1.0","end")
        textbox3.insert('1.0', "No inputs received!")
    else:
        url1 = 'https://en.wikipedia.org/wiki/{}'.format(user_input)
        textbox1.delete("1.0","end")
        searchwiki(url1)

def searchwiki(url1):
    response = requests.get(url=url1)
    textbox1.delete("1.0","end")
    textbox2.delete("1.0","end")
    textbox3.delete("1.0","end")
    textbox4.delete("1.0","end")
    #print(response.status_code) # 200 = successful response from server

    if response.status_code == 200:
        #print("Website response successful!")
        final_url = url1
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find(id="firstHeading")
        #print("Webpage title: ", title.string)
        textbox2.insert("1.0","Wiki-page title:  {}".format(title.string))
        accumulator = 0
        wiki_text = ""
        for x in soup.select('p'):
            if accumulator < 2:
                #print(x.getText())
                incr_text = x.getText()
                wiki_text = "\n".join((wiki_text, incr_text)).strip()
            accumulator = + 1
        
        #print(len(wiki_text))
        textbox3.insert("1.0","Wiki contents are as follows: \n\n{}".format(wiki_text[:5000]))
        
        textbox4.insert("1.0",'For more details, go to: {}'.format(url1))
                
    else:
        textbox3.insert('1.0', "No response from server, Please try again/refine your search")
        



# Title and size adjustments
WebScraper.title('           Web Scrapper/Wiki Mimic App - USING PYTHON/BS4/REQUESTS/TKINTER         ')
WebScraper.geometry('695x600')
WebScraper.resizable(0,0)
WebScraper.configure(bg='burlywood')
WebScraper.mainloop()


################################### END OF SCRIPTS ###################################