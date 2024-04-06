from PIL import Image
import requests
from io import BytesIO
import math


def _download_images(urls):
    images = []
    for url in urls:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Double sided cards are not supported yet! url: {url}")
            continue
        img = Image.open(BytesIO(response.content))
        images.append(img)
    return images


def _create_image_grid(images, grid_size, padding=10):
    grid_width = (images[0].width + padding) * grid_size[1] - padding
    grid_height = (images[0].height + padding) * grid_size[0] - padding

    grid_image = Image.new("RGB", (grid_width, grid_height), color="white")

    for i, img in enumerate(images):
        row = i // grid_size[1]
        col = i % grid_size[1]
        x = col * (img.width + padding)
        y = row * (img.height + padding)
        grid_image.paste(img, (x, y))

    return grid_image


def generate_image(image_urls: list[str], grid_size: tuple[int, int], deck_id):
    images = _download_images(image_urls)
    column, row = grid_size    
    image_chunks = chunk_list(images, column * row)

    for i, chunk in enumerate(image_chunks):
        grid_image = _create_image_grid(chunk, grid_size)
        grid_image.save(f"{deck_id}_{i}.png")


def chunk_list(lst, chunk_size):
    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]
