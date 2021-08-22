# This Dockerfile is used to create the image for the Flask application
FROM python:3.8-slim

ENV PYTHONUNBUFFER ED True  // Prevent the app from crashing without printing a relevant message
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . ./

CMD ["python", "flask_app/app.py"]