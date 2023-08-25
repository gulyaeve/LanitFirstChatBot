FROM python:3.11.4-slim-bullseye

WORKDIR /src

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]