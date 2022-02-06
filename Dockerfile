FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 8000
COPY . .

CMD ["python3", "manage.py", "runserver"]