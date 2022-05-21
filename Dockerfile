FROM Python:3.10.4-alpine3.14

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./ /app

ENV PORT=8000

EXPOSE $PORT

CMD ["python", "manage.py", "runserver"]