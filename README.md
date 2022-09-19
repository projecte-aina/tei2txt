## Extraccion de txt plano a partir de tei-xml generado medinte GrobID
### Con o sin identificación de lengua

### Se extraen los textos desde pdfs mediante Grobid

https://grobid.readthedocs.io


```
java -jar grobid-core/build/libs/grobid-core-0.7.1-onejar.jar -gH /mnt/BSC/grobid-0.7.1/grobid-home/ -dIn /mnt/BSC/catala/corpora/tdxin -dOut /mnt/BSC/catala/corpora/tdxout -ignoreAssets -exe processFullText
```

## Install and run

### Virtual environment

pdf2tei2txt was built and tested with Python3.9. It should work for Python >= 3.9 but it has not been tested with other versions than 3.9.

For creating the virtual environment and installing the dependencies (from `requirements.txt`), run:

```sh
bash setup.sh
```

### Help
'''
python tei2txt.py --help

Usage: tei2txt.py [options]


Options:

  -h, --help            show this help message and exit
  
  -i INPUT, --inputdir=INPUT [REQUIRED]
                        inputdirectory
                        
  -o OUTPUT, --outputdirectory=OUTPUT [REQUIRED]
                        output directory

  -e EXTRACTED --extractdirectory [OPTIONAL]
                        tei-xml extracted directory
                        
  -f FILTER, --filter=FILTER [OPTIONAL]
                        if filter by lang
                        
  -s STATS, --stats=STATS [OPTIONAL]
                        lang_id stats in json format
 '''

