FROM python:3.13

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV PORT=8080

CMD ["python", "application.py"]
