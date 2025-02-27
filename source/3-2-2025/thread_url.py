import threading
import requests

def fetch_url(url, results):
    response = requests.get(url)
    html_content = response.text  # Get the HTML content as a string
    results.append(f"Fetched {url}:\n{html_content}\n")

urls = [
    # "https://example.com"
    "https://www.google.com"
]

threads = []
results = []

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url, results))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Display results in the console after all threads are done
for result in results:
    # print(result)
    with open("goooggg.html","w") as file:
        file.write(result)

print("All URLs fetched")
