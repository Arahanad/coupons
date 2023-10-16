import requests
import os
import hashlib
from datetime import datetime

response = requests.get('https://api.flipp.com/flyerkit/v4.0/publications/safeway?access_token=7749fa974b9869e8f57606ac9477decf&locale=en-US&postal_code=94611&store_code=3132')

if response.status_code == 200:
    data = response.json()
    urls = [item['first_page_thumbnail_url'] for item in data]

    today = datetime.now().strftime("%Y-%m-%d")
    download_dir = os.path.join("Output", today)
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:
            filename = hashlib.sha1(url.encode()).hexdigest() + ".jpg"
            local_filename = os.path.join(download_dir, filename)

            with open(local_filename, 'wb') as f:
                f.write(response.content)

            print(f"Image downloaded and saved as {local_filename}")
        else:
            print(f"Failed to download the image from {url}. Status code: {response.status_code}")
else:
    print(f"Failed to fetch data from the API. Status code: {response.status_code}")
