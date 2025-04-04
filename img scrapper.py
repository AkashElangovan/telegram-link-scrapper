import requests
from bs4 import BeautifulSoup
import os
from concurrent.futures import ThreadPoolExecutor

def download_image(url, output_folder):
    try:
        img_response = requests.get(url)
        if img_response.status_code == 200:
            img_name = url.split('/')[-1]
            with open(os.path.join(output_folder, img_name), 'wb') as img_file:
                img_file.write(img_response.content)
            print(f"Image '{img_name}' downloaded from '{url}'")
    except Exception as e:
        print(f"Error downloading image from '{url}': {e}")

def scrape_images_from_urls(input_file, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read URLs from the input file
    with open(input_file, 'r') as f:
        urls = f.readlines()

    # Download images concurrently using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url in urls:
            url = url.strip()
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                img_tags = soup.find_all('img')
                for img_tag in img_tags:
                    img_url = img_tag.get('src')
                    if img_url:
                        executor.submit(download_image, img_url, output_folder)

def main():
    input_file = input("Enter the path of the input file: ")
    output_folder = r""  # Output folder to save images
    scrape_images_from_urls(input_file, output_folder)

if __name__ == "__main__":
    main()
