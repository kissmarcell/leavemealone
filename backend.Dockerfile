FROM python:3.12

WORKDIR /usr/src/app
VOLUME /usr/src/app/resources

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend .

EXPOSE 5000

CMD [ "python", "./app.py" ]
