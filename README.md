# ilovesyd

A fully asynchronous Python wrapper for the ilovesyd.xyz API.  
Easily predict Pokémon, upload images, and retrieve processed screenshots.

## Installation

Install via pip:

```bash
pip install ilovesyd
```

## Setup & Usage

First, import and initialize the client:

```python
import asyncio
from ilovesyd import IloveSydAPI

api = IloveSydAPI(api_key="your_api_key_here")

async def main():
    result = await api.predict_pokemon("https://example.com/pokemon.png")
    print(result)

asyncio.run(main())
```

## Features & API Methods

### 1. Predict Pokémon

Identify a Pokémon from an image URL.

```python
response = await api.predict_pokemon("https://example.com/pokemon.png")
print(response)  # {"name": "Pikachu", "conf": 98.7}
```

**Function:**

```python
async def predict_pokemon(self, image_url: str) -> dict:
```

- **image_url** (`str`): The URL of the Pokémon image.
- **Returns**: A dictionary with the Pokémon name and confidence level.

### 2. Upload Screenshot

Upload an image for processing.

```python
response = await api.upload_image("screenshot.png")
print(response)  # {"url": "/api/i/abcd1234"}
```

**Function:**

```python
async def upload_image(self, file_path: str) -> dict:
```

- **file_path** (`str`): The path to the image file.
- **Returns**: A dictionary with the image URL.

### 3. Retrieve Processed Image

Get a processed screenshot by its ID.

```python
response = await api.get_image("abcd1234")
with open("output.png", "wb") as f:
    f.write(response)
```

**Function:**

```python
async def get_image(self, image_id: str) -> bytes:
```

- **image_id** (`str`): The ID of the image.
- **Returns**: The image file as bytes.

### All Available Methods

| Method             | Parameters          | Description                        |
|--------------------|--------------------|------------------------------------|
| `predict_pokemon` | `image_url: str`    | Predicts Pokémon from an image    |
| `upload_image`    | `file_path: str`    | Uploads an image for processing   |
| `get_image`       | `image_id: str`     | Retrieves a processed image       |

## Configuration

By default, the API uses:

```
https://ilovesyd.xyz/api
```

To use a custom base URL:

```python
api = IloveSydAPI(api_key="your_api_key_here", base_url="https://customdomain.com/api")
```

## Dependencies

This package requires `aiohttp` for asynchronous HTTP requests.  
It is automatically installed, but you can manually install it if needed:

```bash
pip install aiohttp
```

## Example Project

Save this as `example.py`:

```python
import asyncio
from ilovesyd import IloveSydAPI

api = IloveSydAPI(api_key="your_api_key_here")

async def main():
    # Predict Pokémon
    result = await api.predict_pokemon("https://example.com/pokemon.png")
    print("Prediction:", result)

    # Upload Screenshot
    upload = await api.upload_image("screenshot.png")
    print("Uploaded URL:", upload["url"])

    # Retrieve Image
    image_data = await api.get_image("abcd1234")
    with open("downloaded.png", "wb") as f:
        f.write(image_data)
    print("Image saved as downloaded.png")

asyncio.run(main())
```

Run it:

```bash
python example.py
```

## Contributing

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m "Added new feature"`)  
4. Push to your branch (`git push origin feature-branch`)  
5. Open a Pull Request  

## License

This project is licensed under the MIT License.

---

**Made with ❤️ by [ilovesyd.xyz](https://ilovesyd.xyz)**  
