# Use an official Python runtime as a parent image
FROM python:3.9
RUN apt-get update && apt-get install -y g++
RUN useradd -m judge_runner

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

RUN mkdir -p /app/code /app/input /app/output && \
    chown -R judge_runner:judge_runner /app/code /app/input /app/output

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=dummy.settings
ENV PYTHONUNBUFFERED=1



# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]