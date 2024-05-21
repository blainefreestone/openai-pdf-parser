import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="pdf-parser",
        description="Uses OpenAI gpt-4-turbo to describe the contents of each page of a PDF file.",
    )

    parser.add_argument('pdf-filepath', type=str, help='Path to the PDF file to be parsed.')
    
    parser.add_argument('output-filepath', type=str, help='Path to the file where the output will be written.')

    parser.add_argument('--system-instructions', '-s', default='system-instructions.txt', help='Path to the file containing system instructions.')

    args = parser.parse_args()
