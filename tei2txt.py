#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 09:21:14 2022

@author: carlos rodriguez (bsc)
"""
import shutil
from collections import Counter
from pathlib import Path
from bs4 import BeautifulSoup
import langid
import os, json, sys
import argparse

def read_tei(tei_file):
    with open(tei_file, 'r') as tei:
        soup = BeautifulSoup(tei, 'xml')
        return soup
    raise RuntimeError('Cannot generate a soup from the input')


def extract_text_by_selector(soup, selector):
    alltext = []
    for data in soup.select(selector):
        alltext.append(data.get_text())
    return alltext


def langdet(alltext):
    langs = []
    for s in alltext:
        if langid.classify(s)[0] != 'ca':
            print(s, langid.classify(s)[0])
        else:
            langs.append(langid.classify(s)[0])


def langaverage(alltext):
    langs = []
    for s in alltext:
        langs.append(langid.classify(s)[0])
    counts = Counter(langs)
    nca = counts['ca']
    nothers = sum([counts[x] for x in counts if (x != 'ca')])
    cafr = (nca * 100) / (nca + nothers)
    return cafr


def main():
    parser = argparse.ArgumentParser(prog="tei2txt", description="Convert tei-xml to txt")

    parser.add_argument("-i", "--input", help="input directory", required=True)
    parser.add_argument("-o", "--output", help="output directory", required=True)
    parser.add_argument("--force", action="store_true", help="to reprocess tei.xml input files")
    parser.add_argument("-f", "--filter", dest="filter", help="if filter by lang")
    parser.add_argument("-s", "--stats", dest="stats", help="lang_id stats")
    parser.add_argument('-S', '--selector', default="head, p", dest="selector", type=str)

    args = parser.parse_args()

    input_dir = Path(args.input)
    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True)
    force = args.force


    if args.stats:
        stats = {}
    all_files = os.listdir(input_dir)
    
    print(f"[TEI2TXT] Processing: {str(len(all_files))} files")
    
    for tei_file in all_files:
        
        output_file_path = Path(output_dir, f"{tei_file}.txt")
        print(f"[TEI2TXT] Processing {Path(input_dir, tei_file)}")

        if not force and os.path.isfile(output_file_path):
            print(f"[TEI2TXT] {output_file_path}, already exist, skipping... (use --force to reprocess tei.xml input files)")
            continue
        soup = read_tei(Path(input_dir, tei_file))

        text_list = extract_text_by_selector(soup, args.selector)

        # text_list = extract_text(soup, default_tags)
        if text_list:
            if args.filter:
                p = langaverage(text_list)
                if args.stats:
                    stats[tei_file] = p
                if p > int(args.filter):
                    text_string = "\n".join(text_list)
                    w = open(output_dir + tei_file + ".txt", "w")
                    w.write(text_string)
                    w.close()
                else:
                    pass
            else:
                text_string = "\n".join(text_list)
                w = open(output_file_path, "w")
                w.write(text_string)
                w.close()
    if args.stats:
        with open("lang_id_stats.json", "w") as jout:
            json.dump(stats, jout, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
