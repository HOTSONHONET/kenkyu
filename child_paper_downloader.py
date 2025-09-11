import pymupdf
from pprint import pprint
import re
import requests 
import os
from tqdm import tqdm


class Config:
    DOWNLOAD_PATH = "downloads"

def main(filepath):
    doc = pymupdf.open(filepath)
    
    full_txt = ""
    for page in doc: full_txt += page.get_text()

    refs_match = re.search(r'(References|Bibliography)(.*)', full_txt, re.IGNORECASE | re.DOTALL)
    refs_text = ""
    if refs_match: refs_text = refs_match.group(2).strip()
    
    references = re.split(r'\n\d+\.\s+', refs_text)

    if len(references) <= 1: 
        references = [ref.strip() for ref in refs_text.split("\n") if ref.strip()]
    
    references = [ref for ref in references if ref]

    refs = []
    for ref in references:
        ref_list = ref.split("[")[1:]
        for actual_ref in ref_list: refs.append("[" + actual_ref)
        
    # Collecting all the DOIs
    dois = []
    search_prefixes = ["arXiv:", "abs/"]
    for ref in refs:
        for search_prefix in search_prefixes:
            if search_prefix in ref:
                try:
                    search_prefix_idx = ref.index(search_prefix)
                    doi = ref[search_prefix_idx + len(search_prefix):].split(",")[0]
                    title = ref[:100][4:] + ".pdf"
                    dois.append({
                        "name": title,
                        "doi": doi
                    })
                except Exception as E:
                    print(f"[ERROR] {E}")

    pprint(dois)
    print(f"Coverage: {len(dois)}/{len(refs)}")

    # Creating a download directory
    if not os.path.exists(Config.DOWNLOAD_PATH): os.mkdir(Config.DOWNLOAD_PATH)

    url = "https://arxiv.org/pdf"
    for ref_doi in tqdm(dois):
        response = requests.get(f'{url}/{ref_doi["doi"]}')

        if response.status_code == 200:
            file_path = f"{Config.DOWNLOAD_PATH}/{ref_doi['name']}.pdf"
            try:
                with open(file_path, "wb") as file: file.write(response.content)
            except Exception as E:
                print(f"[ERROR] {E}")
    



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")

    args = parser.parse_args()
    main(args.file_name)
