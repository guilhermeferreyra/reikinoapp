FROM python:3.9.9-slim-buster
ENV TZ=America/Recife
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY api.py ./
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "/usr/src/app/api.py"]