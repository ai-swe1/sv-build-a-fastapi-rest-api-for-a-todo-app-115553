FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Copy source code
COPY . .

# Expose port
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
