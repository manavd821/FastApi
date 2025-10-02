FROM python:3.13.5

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /fastapi_docker

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# RUN pip install "fastapi[standard]"

COPY . ./

# for development purpose
CMD [ "sleep", "infinity" ] 

# CMD [ "fastapi", "dev", "--host", "0.0.0.0", "--port", "8000" ]

# for production purpose
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]