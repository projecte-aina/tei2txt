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
from optparse import OptionParser


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


# def extract_text(soup, p):
#     alltext = []
#     for data in soup.find_all(p):
#         alltext.append(data.get_text())
#     return alltext


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
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input",
                      help="input directory")
    parser.add_option("-o", "--output", dest="output",
                      help="output directory")
    parser.add_option("-e", "--extract", dest="extracted", help="extracted xml directory")

    parser.add_option("-f", "--filter", dest="filter",
                      help="if filter by lang", default=None)
    parser.add_option("-s", "--stats", dest="stats",
                      help="lang_id stats", default=None)
    parser.add_option('-S', '--selector',
                      default="head, p",
                      dest="selector",
                      type='string')

    (options, args) = parser.parse_args(sys.argv)

    # default_tags =  ['head', 'p']

    input_dir = Path(options.input)
    output_dir = Path(options.output)
    extracted_dir = None

    output_dir.mkdir(exist_ok=True)

    if options.extracted:
        extracted_dir = Path(options.extracted)
        extracted_dir.mkdir(exist_ok=True)

    # else:
    #     extracted_dir = Path(f"{output_dir.parent}/extracted")

    if options.stats:
        stats = {}
    all_files = os.listdir(input_dir)
    print(f"[TEI2TXT] Processing: {str(len(all_files))} files ...")
    #
    for tei_file in all_files:

        print(Path(input_dir, tei_file))
        soup = read_tei(Path(input_dir, tei_file))

        text_list = extract_text_by_selector(soup, options.selector)
        # text_list = extract_text(soup, default_tags)
        if text_list:
            if options.filter:
                p = langaverage(text_list)
                if options.stats:
                    stats[tei_file] = p
                if p > int(options.filter):
                    text_string = "\n".join(text_list)
                    w = open(output_dir + tei_file + ".txt", "w")
                    w.write(text_string)
                    w.close()
                else:
                    pass
            else:
                text_string = "\n".join(text_list)
                w = open(Path(output_dir, f"{tei_file}.txt"), "w")
                w.write(text_string)
                w.close()
            if extracted_dir is not None:
                shutil.move(Path(input_dir, tei_file), extracted_dir)
    if options.stats:
        with open("lang_id_stats.json", "w") as jout:
            json.dump(stats, jout, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
