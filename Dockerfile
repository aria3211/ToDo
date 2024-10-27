FROM python:3.9-slim

WORKDIR /app/


COPY To_Do/ /app/To_Do

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000


RUN python /app/To_Do/A/manage.py migrate

CMD ["python", "/app/To_Do/A/manage.py", "runserver", "0.0.0.0:8000"]

HEALTHCHECK --interval=30s --timeout=5s CMD curl -f http://localhost:8000/ || exit 1
