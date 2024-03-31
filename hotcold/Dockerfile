FROM python:3.9-slim
WORKDIR /app
RUN pip install Flask
COPY . /app
EXPOSE 5000
CMD ["python", "hot-cold.py"]