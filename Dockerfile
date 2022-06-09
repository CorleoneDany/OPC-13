FROM python:3.10.4-alpine3.14

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN addgroup --system django
RUN adduser --system --ingroup django django

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./ /app
RUN chown -R django:django /app
USER django

EXPOSE 8000

CMD gunicorn  oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
