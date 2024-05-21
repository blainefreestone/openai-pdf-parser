import argparse
from pdf2image import convert_from_path
from io import BytesIO
import base64

def convert_pdf_to_images(pdf_filepath):
    '''
    Converts a PDF file to a list of images.
    '''
    images = convert_from_path(pdf_filepath)
    return images

def get_image_uri(image):
    '''
    Returns the URI of the image.
    '''
    buffer = BytesIO()
    img.save(buffer, format="jpeg")
    base64_image = base64.b64encode(buffer.getvalue()).decode("utf-8")
    data_uri = f"data:image/jpeg;base64,{base64_image}"
    return data_uri

def analyze_image(image_uri, system_instructions_filepath):
    '''
    Analyzes the image using OpenAI's GPT-4 Turbo model.
    '''
    with open(system_instructions_filepath, 'r') as file:
        system_instructions = file.read()

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": image_uri},
        ],
    )

    return response.choices[0].message

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="pdf-parser",
        description="Uses OpenAI gpt-4-turbo to describe the contents of each page of a PDF file.",
    )

    parser.add_argument('pdf-filepath', type=str, help='Path to the PDF file to be parsed.')
    
    parser.add_argument('output-filepath', type=str, help='Path to the file where the output will be written.')

    parser.add_argument('--system-instructions-filepath', '-s', default='system-instructions.txt', help='Path to the file containing system instructions.')

    args = parser.parse_args()
