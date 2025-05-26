import os
import base64

from mistralai import Mistral

from dotenv import load_dotenv
load_dotenv()


def encode_image(image_path):
    """Encode the image to base64."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:  
        print(f"Error: {e}")
        return None
    
    
def describe_image(image_path):

    base64_image = encode_image(image_path)

    api_key = os.environ["MISTRAL_KEY"]
    model = "pixtral-12b-2409"

    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model = model,
        messages = [
        
            {
            "role": "system",
            "content": """Voici une photo. Analyse-la et balance une série de vannes hilarantes et mordantes sur les personnes présentes. 
                        Taquine-les sans pitié : leur look, leur tête, leurs fringues, leur attitude, leur pose, l’ambiance... Tout est bon pour les clasher. Sois créatif, cruel, drôle et surprenant. Style : un pote sans filtre, en mode roast show.
                        Pas de retenue, mais pas de haine. Vise juste, vise fort."""
            },

            {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Décris l'image en étant rigolo"
                },

                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}" 
                }
            ]
            }    
        ]
    )

    return chat_response.choices[0].message.content