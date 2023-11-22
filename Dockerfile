FROM python:3.9-slim 

RUN apt-get update && apt-get install -y git g++ \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt /app
 
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "tei2txt.py" ]
