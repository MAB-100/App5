import requests

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/181px-Cat_August_2010-4.jpg"

response = requests.get(url)

if url.endswith(".jpg"):
    with open("image.jpg", "wb") as file:
        file.write(response.content)
elif url.endswith(".png"):
    with open("image.png", "wb") as file:
        file.write(response.content)
else:
    print("The file format is not supported")