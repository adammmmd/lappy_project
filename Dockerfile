FROM python:3.9-slim

WORKDIR /app
COPY . /app 


RUN apt-get update && apt-get install -y
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input
RUN python3 manage.py migrate


EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "lappy_project.wsgi:application"]