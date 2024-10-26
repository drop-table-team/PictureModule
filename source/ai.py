import base64
from io import BytesIO

from PIL import Image

from langchain_ollama import ChatOllama



from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import JsonOutputParser

# 192.168.0.104:11434
def convert_image_ollama(image):
    ollama = ChatOllama(
        model="llava",
        temperature=0,
        format="json",
        base_url="http://192.168.0.104:11434",
    )

    # Create the chain with the prompt function, model, and output parser
    chain = prompt_func | ollama | JsonOutputParser()

    pil_image = Image.open(image)
    image_b64 = convert_to_base64(pil_image)

    # Invoke the chain with the text and image data
    query_chain = chain.invoke(
        {"text": "", "image": image_b64}
    )

    return query_chain

def convert_to_base64(pil_image):
    """
        Convert PIL images to Base64 encoded strings

        :param pil_image: PIL image
        :param image_format: Image format, default: PNG
        :return: Re-sized Base64 string
        """

    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")  # You can change the format if needed
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

# Function to create the prompt with text and image
def prompt_func(data):
    text = data["text"]
    image = data["image"]

    image_part = {
        "type": "image_url",
        "image_url": f"data:image/jpeg;base64,{image}",
    }

    content_parts = []

    text_part = {"type": "text", "text": "You are a helpful assistant that collects information from pictures. Return answers to the following statements: Give the picture a title. Summarise the picture. Describe the picture. Repeat the text in the picture if there is any., Give tags corresponding to the image."
    }


    content_parts.append(image_part)
    content_parts.append(text_part)

    return [HumanMessage(content=content_parts)]