FROM python:3.8

WORKDIR /code

COPY requirements.txt /
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./alembic.ini ./
COPY ./alembic  /code/alembic
COPY ./prestart.sh ./

RUN chmod +x prestart.sh

COPY .env /code

COPY ./app /code/app



CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]