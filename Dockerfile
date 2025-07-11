FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt 
COPY . .

ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["python", "app.py"]

#CMD ["flask", "run"] 
