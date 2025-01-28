import os
import xml.etree.ElementTree as ET

# Function to preprocess the TMX file by finding and replacing specified characters
def preprocess_tmx_file(file_path, chars_to_replace):
    with open(file_path, "r", encoding="utf-8") as file:
        xml_content = file.read()

    for char in chars_to_replace:
        xml_content = xml_content.replace(char, "")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(xml_content)

# Function to parse the TMX file and extract source and target texts
def parse_tmx_file(file_path, source_lang, target_lang):
    chars_to_replace = [
        "&#x0;", "&#x1;", "&#x2;", "&#x3;", "&#x4;", "&#x5;", "&#x6;", "&#x7;",
        "&#x8;", "&#x9;", "&#xA;", "&#xB;", "&#xC;", "&#xD;", "&#xE;", "&#xF;",
        "&#x10;", "&#x11;", "&#x12;", "&#x13;", "&#x14;", "&#x15;", "&#x16;", "&#x17;",
        "&#x18;", "&#x19;", "&#x1A;", "&#x1B;", "&#x1C;", "&#x1D;", "&#x1E;", "&#x1F;"
    ]
    preprocess_tmx_file(file_path, chars_to_replace)

    tree = ET.parse(file_path)
    root = tree.getroot()

    ns = {"xml": "http://www.w3.org/XML/1998/namespace"}

    source_texts = []
    target_texts = []

    for tu in root.findall(f".//tuv[@xml:lang='{source_lang}']/seg", namespaces=ns):
        source_text = tu.text
        print(f"Source text found: {source_text}")  # Debugging
        source_texts.append(source_text)

    for tu in root.findall(f".//tuv[@xml:lang='{target_lang}']/seg", namespaces=ns):
        target_text = tu.text
        print(f"Target text found: {target_text}")  # Debugging
        target_texts.append(target_text)

    return source_texts, target_texts

# Function to create an XLIFF file from the source and target texts
def create_xliff(source_texts, target_texts, source_lang, target_lang, output_file):
    if len(source_texts) != len(target_texts):
        print("Error: The source and target texts do not have the same number of entries.")
        return

    xliff = ET.Element("xliff", attrib={"version": "1.2", "xmlns": "urn:oasis:names:tc:xliff:document:1.2"})

    file_tag = ET.SubElement(
        xliff, "file",
        attrib={
            "source-language": source_lang,
            "target-language": target_lang,
            "datatype": "plaintext",
            "original": "input.tmx"
        }
    )

    body = ET.SubElement(file_tag, "body")

    for i, (src, tgt) in enumerate(zip(source_texts, target_texts), start=1):
        trans_unit = ET.SubElement(body, "trans-unit", attrib={"id": str(i)})
        ET.SubElement(trans_unit, "source").text = src
        ET.SubElement(trans_unit, "target").text = tgt

    tree = ET.ElementTree(xliff)
    ET.indent(tree, space="  ", level=0)  # Pretty print
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"XLIFF file created: {output_file}")

# Main function to drive the TMX to XLIFF conversion
def main():
    # Prompt user for inputs
    directory = input("Enter the directory containing the .tmx files: ").strip()
    if not os.path.isdir(directory):
        print("Invalid directory.")
        return

    source_lang = input("Enter the source language code (e.g., 'en'): ").strip()
    target_lang = input("Enter the target language code (e.g., 'fr'): ").strip()

    output_folder = os.path.join(directory, "output")
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(directory):
        if file.endswith(".tmx"):
            file_path = os.path.join(directory, file)

            source_texts, target_texts = parse_tmx_file(file_path, source_lang, target_lang)

            output_file = os.path.join(output_folder, f"{os.path.splitext(file)[0]}_{source_lang}_{target_lang}.xliff")
            create_xliff(source_texts, target_texts, source_lang, target_lang, output_file)

if __name__ == "__main__":
    main()
