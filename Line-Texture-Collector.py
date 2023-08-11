import requests, os, json
from bs4 import BeautifulSoup

url = "https://store.line.me/stickershop/product/23398216/zh-Hant"
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")

# create a catalogue to store images
images_dir = "C:\\Users\\HP\\Desktop\\Try\\Line-Texture-Collector-images"

# download images
datas = soup.find_all("li", class_ = "mdCMN09Li FnStickerPreviewItem static-sticker")
for data in datas:
    # typecasting：str to dict
    img_info = json.loads(data.get("data-preview"))
    id = img_info["id"]
    img_file = requests.get(img_info["staticUrl"])
    full_path = os.path.join(images_dir, id)

    # store images
    with open(full_path + ".png", "wb") as f:
        f.write(img_file.content)
    print(full_path + ".png")












































