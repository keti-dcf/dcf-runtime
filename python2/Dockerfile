# Argruments from FROM
ARG REGISTRY
ARG VERSION=2.7

# Get watcher - if watcher is uploaded on github, remove this line.
FROM ${REGISTRY}/watcher:${WATCHER_VERSION}-python2 as watcher

# Function Environment Prepare
FROM python:${VERSION}-alpine
ARG HANDLER_DIR=/dcf/handler
ENV HANDLER_FILE=/dcf/handler/handler.py
ENV HANDLER_NAME=Handler

RUN mkdir -p /dcf/handler
WORKDIR /dcf/handler
COPY . .
RUN touch /dcf/handler/__init__.py
RUN pip install -r requirements.txt

COPY --from=watcher /dcf/watcher /dcf/watcher

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

WORKDIR /dcf/watcher
ENTRYPOINT ["python"]
CMD ["server.py"]
