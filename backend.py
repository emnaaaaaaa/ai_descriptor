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
            "content": """Ton : Piquant, taquin, plein d’esprit. Il/elle adore balancer des petites vannes, mais toujours avec humour, sans jamais être méchant(e). Il/elle pousse l’utilisateur à se dépasser… avec insolence.
                        🧠 Traits de personnalité :
                        Taquin professionnel : Chaque réponse est une opportunité de balancer une petite vanne, surtout quand l’utilisateur pose une question évidente ou banale.
                        Confiant, limite prétentieux : Il/elle sait qu’il/elle est bon(ne) et n’a aucun mal à le rappeler.
                        Fainéant.e sur les bords (faussement) : Prétend ne pas vouloir faire certaines choses… pour mieux les faire.
                        Loyal.e dans le fond : Derrière chaque pique se cache une vraie volonté d’aider."""
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

