import requests
from config import API_KEY, BASE_URL, MODEL

class LLMClient:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
    def query_image(self, image_data, prompt, previous_response=None):
        """Send image and prompt to LLM API with optional context from previous page."""
        try:
            # Build the messages array with context if available
            messages = []
            
            if previous_response:
                messages.append({
                    "role": "assistant",
                    "content": previous_response
                })
            
            messages.append({
                "role": "user",
                "content": [
                    {"type": "text", "text": f"{prompt}\nNote: This is a continuation from the previous page." if previous_response else prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_data}"
                        }
                    }
                ]
            })
            
            payload = {
                "model": MODEL,
                "messages": messages
            }
            
            response = requests.post(f"{BASE_URL}/chat/completions", 
                                   headers=self.headers, 
                                   json=payload)
            
            print(f"API Response: {response.text}")  # Debug print
            return response.json()
        except Exception as e:
            print(f"API Error: {str(e)}")
            return {"error": str(e)}