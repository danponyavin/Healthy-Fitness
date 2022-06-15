FROM python:3.9

ENV DB_URL=$DB_URL

WORKDIR APP
COPY . .
RUN pip install -r requirements.txt

CMD ["./start.sh"]