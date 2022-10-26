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
```bash
python tei2txt.py --help
```

### Usage

```bash
python tei2txt.py [options]
```

| Option              | Default   | Description                                                           |
|:--------------------|:----------|:----------------------------------------------------------------------|
| `-i`, `--input`     | `None`    | **Required.** Xml input directory                                     |
| `-o`, `--output`    | `None`    | **Required.** Text output directory                                   |
| `-e`, `--extracted` | `None`    | **Optional.** Xml extracted directory                                 |
| `-f`, `--filter`    | `None`    | **Optional.** If filter by lang                                       |
| `-s`, `--stats`     | `None`    | **Optional.** lang_id stats in json format                            |
| `-S`, `--selector`  | `"head, p"` | **Optional.** Xml css selector, **Use of double quotes is mandatory** |

#### Example:
```bash
python tei2txt.py --input ./xml --output ./txt --selector "article-meta article-title, abstract, body title, body p"

```


