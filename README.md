## Extraccion de txt plano a partir de tei-xml generado medinte GrobID
### Con o sin identificación de lengua

### Se extraen los textos desde pdfs mediante Grobid

https://grobid.readthedocs.io


```
java -jar grobid-core/build/libs/grobid-core-0.7.1-onejar.jar -gH /mnt/BSC/grobid-0.7.1/grobid-home/ -dIn /mnt/BSC/catala/corpora/tdxin -dOut /mnt/BSC/catala/corpora/tdxout -ignoreAssets -exe processFullText
```

### Help
'''
python tei2txt.py --help

Usage: tei2txt.py [options]


Options:

  -h, --help            show this help message and exit
  
  -i INPUT, --inputdir=INPUT
                        inputdirectory
                        
  -o OUTPUT, --outputdirectory=OUTPUT
                        output directory
                        
  -f FILTER, --filter=FILTER
                        if filter by lang
                        
  -s STATS, --stats=STATS
                        lang_id stats in json format
 '''

