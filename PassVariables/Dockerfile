FROM docker.arvancloud.ir/python:3.12.3

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DB_HOST=host
ENV DB_USER=user
ENV DB_PASSWORD=password

CMD ["python", "main.py"]
