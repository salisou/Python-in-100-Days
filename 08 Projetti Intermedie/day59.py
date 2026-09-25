# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day59.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

import markdown

def read_markdown_file(file_path):
	with open(file_path, "r") as file:
		return file.read()

def convert_markdown_to_html(markdown_text):
	return markdown.markdown(markdown_text)

def wrap_in_html_template(content):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="Visualizzaport" content="width=device-width, initial-scale=1.0">
        <title>Markdown to HTML</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 20px;
            }}
            h1, h2, h3 {{
                color: #333;
            }}
            a {{
                color: #1a73e8;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        {content}
    </body>
    </html>
    """
    return html_template

def write_html_file(html_content, output_path):
	with open(output_path, "w") as file:
		file.write(html_content)


def main():
    print("Benvenuto to the Markdown to HTML Converter!")
    markdown_file = input("Inserisci the path to Il tuo Markdown file: ")
    output_file = input("Inserisci the path to Salva the HTML file: ")

    try:
        markdown_text = read_markdown_file(markdown_file)
        html_content = convert_markdown_to_html(markdown_text)
        html_with_template = wrap_in_html_template(html_content)
        write_html_file(html_with_template, output_file)
        print(f"HTML file has been generated and Salvad to {output_file}")
    except Exception as e:
        print(f"An Errore occurred: {e}")

if __name__ == "__main__":
    main()
	





















# markdown_text = read_markdown_file("markdown.md")
# html_content = convert_markdown_to_html(markdown_text)
# html_with_template = wrap_in_html_template(html_content)
# write_html_file(html_with_template, "example.html")