FROM python:3.10.4-alpine3.14

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./ /app

EXPOSE 8000

CMD ["gunicorn", "oc_lettings_site.wsgi:application"]