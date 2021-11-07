FROM python:latest
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN pip install  --no-cache-dir -r requirements.txt
CMD ["python", "./main.py"]