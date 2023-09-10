FROM python:3.11-slim as base-image

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    APP_PATH=/app

FROM base-image as builder-image
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential
RUN pip install poetry
WORKDIR $APP_PATH
COPY ./pyproject.toml $APP_PATH/
COPY ./poetry.lock $APP_PATH/
RUN poetry export -f requirements.txt --output $APP_PATH/requirements.txt --without-hashes


FROM builder-image as production-image
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR $APP_PATH
COPY . /app
COPY --from=builder-image $APP_PATH/requirements.txt $APP_PATH/requirements.txt
RUN pip install --no-cache-dir --upgrade -r $APP_PATH/requirements.txt
ENV PYTHONPATH=/app:/app/src

ENTRYPOINT ["/app/start.sh"]