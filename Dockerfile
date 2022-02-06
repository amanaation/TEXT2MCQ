FROM python:3.7

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN /bin/bash -c "python3 -m  venv .venv  && source .venv/bin/activate"

RUN pip3 install -r requirements.txt
EXPOSE 8000
COPY . .
CMD ["python3", "manage.py", "runserver"]