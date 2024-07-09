import requests
import base64
from openai import OpenAI

# openaiのセットアップ
# see キーの取得方法: https://book.st-hakky.com/data-science/open-ai-create-api-key/
api_key = "openai key"

client = OpenAI()
openai.api_key = st.secrets["OPENAI_API_KEY"]

img_pth = "image url"

# 画像をバイナリに変換
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# 画像のパス
image_path = "demo.jpg"

base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What’s in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 50
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json().get("choices")[0]["message"]["content"])