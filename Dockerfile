# base image 
FROM python:3.7

# File Author / Maintainer
MAINTAINER Xeno

# Copy the application folder inside the container
ADD . /usr/src/app

# set the default directory where CMD will execute
WORKDIR /usr/src/app

COPY requirements.txt ./
# Get pip to download and install requirements:

RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 8000

# default command to execute    
CMD python manage.py migrate                  # Apply database migrations
CMD python manage.py collectstatic --noinput  # Collect static files
CMD echo Starting Gunicorn.
CMD exec gunicorn djangoapp.wsgi:application --bind 0.0.0.0:8000 --workers 3 --log-level=info

