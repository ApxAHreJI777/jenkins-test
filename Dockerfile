FROM python:3.8-slim as base

EXPOSE 5000

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


FROM base AS python-deps

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Install application into container
COPY . /app

# Create and switch to a new user
WORKDIR /app
RUN useradd appuser && chown -R appuser /app
USER appuser

# Run the application
# ENTRYPOINT ["python", "-m", "flask", "run"]
# CMD ["--host=0.0.0.0"]

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]