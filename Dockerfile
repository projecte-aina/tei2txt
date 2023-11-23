FROM python:3.9-slim 

WORKDIR /app

COPY ./requirements.txt /app
 
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "tei2txt.py"]
