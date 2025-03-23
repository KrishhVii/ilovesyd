# IloveSydAPI Wrapper

IloveSydAPI is a simple and easy-to-use wrapper for interacting with the `ilovesyd.xyz` API.

## 🚀 Installation

You can install the package using pip:

```sh
pip install ilovesyd
```

## 📌 Usage

### 1️⃣ Import the Library

```python
from ilovesyd import IloveSydAPI
```

### 2️⃣ Initialize API

```python
api = IloveSydAPI(api_key="your_api_key_here")
```

### 3️⃣ Predict Pokémon from an Image URL

```python
result = api.predict_pokemon("https://example.com/pokemon.png")
print(result)
```

### 4️⃣ Upload an Image

```python
result = api.upload_screenshot("path/to/image.png")
print(result)
```

### 5️⃣ Get Screenshot by Image ID

```python
result = api.get_screenshot("image_id_here")
print(result)
```

### 6️⃣ Test API Connection

```python
result = api.test_connection()
print(result)
```

## 🔥 API Methods

| Method                         | Description                     |
|--------------------------------|---------------------------------|
| `predict_pokemon(image_url)`   | Predicts Pokémon from an image. |
| `upload_screenshot(file_path)` | Uploads an image to the API.    |
| `get_screenshot(image_id)`     | Retrieves a screenshot by ID.   |
| `test_connection()`            | Checks if the API is reachable. |

## 📦 Dependencies

- `requests`

## ⚖ License

This project is licensed under the **MIT License**.

---


