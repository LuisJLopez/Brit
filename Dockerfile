FROM python:3.9.15

# Prevent python compiled files from being generated
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Install packages
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system 


# Add source code to working dir
ADD . /app

# Expose port
EXPOSE 8000

# Run
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]