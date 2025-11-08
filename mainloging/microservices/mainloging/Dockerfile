FROM python:3.12

WORKDIR /app


COPY  . /app 
COPY ./requirements.txt /app
COPY ./app/db db
COPY ./app/models models
COPY ./app/schemas schemas
COPY ./app/security security
COPY ./app/auth auth
COPY ./app/routers routers
COPY . .

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy python-jose[cryptography] python-multipart

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
