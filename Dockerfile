FROM python:3.7

WORKDIR /app

COPY requirements.txt requirements.txt
COPY temp.py temp.py
RUN python3 -m pip install --upgrade pip
RUN /bin/bash -c "python3 -m  venv .venv  && source .venv/bin/activate" #  && pip3 install pandas && python3 temp.py"

RUN pip3 install -r requirements.txt
EXPOSE 8000
COPY . .
CMD ["python3", "manage.py", "runserver"]