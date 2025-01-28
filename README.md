# tmx-to-xliff
This script converts .tmx files to .xliff files, preserving translation units as source-target pairs, preserving translation units as source-target pairs.

## Overview

The TMX_to_XLIFF tool processes TMX files in a specified directory, extracts source and target language texts, and generates standardized XLIFF files. Key features include:
- Removal of control characters to ensure XML compatibility
- Preservation of translation unit order and content
- Automatic creation of an output directory for converted files
- Support for user-specified source and target language codes

## Requirements

- **Python 3**  
  The script utilizes the following built-in Python libraries:
  - `os` (for directory operations)
  - `xml.etree.ElementTree` (for XML parsing and generation)

## Files

- TMX_to_XLIFF.py

## Usage

1. Place all .tmx files requiring conversion in a dedicated directory
2. Run the script using Python
3. When prompted, provide:

- **Path to the directory containing .tmx files**  
- **Source language code** (e.g., `en` for English)  
- **Target language code** (e.g., `fr` for French)  

The script will:

- Process all .tmx files in the specified directory  
- Create an `output` subdirectory containing converted .xliff files  
- Generate filenames following the pattern: `[original_filename]_[source]_[target].xliff`  

## Important Notes

1. Input Requirements:
- Ensure TMX files contain matching source/target language pairs  
- Language codes must match those used in the TMX files  

2. Output Characteristics:
- XLIFF files conform to version 1.2 specification  
- XML declaration uses UTF-8 encoding  
- Output files include pretty-printed XML for readability  

3. Error Handling:
- Script validates source/target text alignment  
- Skips processing if directory path is invalid  
- Preserves original whitespace and formatting in texts  

4. Preprocessing:
- Automatically removes Unicode control characters (U+0000-U+001F)  
- Handles empty text segments gracefully  

## License
This project is governed by the CC BY-NC 4.0 license. For comprehensive details, kindly refer to the LICENSE file included with this project.
