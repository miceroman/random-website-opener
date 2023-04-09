import tkinter as tk
import webbrowser
import requests
import random

def open_random_website(word):
    # Send a request to Google and get the first page of results
    url = f'https://www.google.com/search?q={word}&start=0'
    response = requests.get(url)
    response.raise_for_status()
    search_results = response.text

    # Find links to pages containing the specified word
    links = []
    start_index = 0
    while True:
        link_start = search_results.find('<a href="/url?q=', start_index)
        if link_start == -1:
            break
        link_end = search_results.find('&amp;', link_start + 16)
        if link_end == -1:
            break
        link = search_results[link_start + 16:link_end]
        if link.startswith('http'):
            links.append(link)
        start_index = link_end

    # Choose a random site from the found links and open it
    random_link = random.choice(links)
    webbrowser.open_new_tab(random_link)

# Create a GUI
root = tk.Tk()
root.title("Random Website Opener")
root.geometry("400x200")

# Create a label and an entry field
label = tk.Label(root, text="Enter a word to search for:")
label.pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack()

# Create a button to open a random website
def open_random_website_gui():
    word = entry.get()
    open_random_website(word)
button = tk.Button(root, text="Open Random Website", command=open_random_website_gui)
button.pack(pady=10)

root.mainloop()