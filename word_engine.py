from docx import Document

__all__ = ['generate_memo']  # Only 'greet' will be importable via 'from mymodule import *'


def generate_memo():
    """
    Generates a Word document with placeholders replaced by actual values.
    """
    # Create a new Word document
    doc = Document()

    # Define your variables
    variables = {
        "name": "Roman",
        "city": "New York",
        "role": "Sales Lead"
    }

    # Add a paragraph with placeholders
    text = "Hello, my name is {name}. I live in {city}, and I work as a {role}."
    final_text = text.format(**variables)

    doc.add_paragraph(final_text)

    # Save the document
    doc.save("generated_memo.docx")
