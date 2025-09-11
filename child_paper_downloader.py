import pymupdf
from pprint import pprint
import re


def main(filepath):
    doc = pymupdf.open(filepath)
    
    full_txt = ""
    for page in doc: full_txt += page.get_text()

    refs_match = re.search(r'References|Bibliography)(.*)', full_txt, re.IGNORECASE | re.DOTALL)
    refs_text = ""
    if refs_match: refs_text = refs_match.group(2).strip()
    
    references = re.split(r'\n\d+\.\s+', refs_text)

    if len(references) <= 1: 
        references = [ref.strip() for ref in refs_text.split("\n") if ref.strip()]
    
    references = [ref for ref in references if ref]

    print("Extracted References: ")
    for ref in references:
        print(ref)
        print("-"*100)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")

    args = parser.parse_args()
    main(args.file_name)
