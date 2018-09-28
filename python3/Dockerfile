# Argruments from FROM
ARG REGISTRY
ARG PYTHON_VERSION=3.4
ARG WATCHER_VERSION=0.1.0

# Get watcher - if watcher is uploaded on github, remove this line.
FROM ${REGISTRY}/watcher:${WATCHER_VERSION}-python2 as watcher

# Function Environment Prepare
FROM python:${PYTHON_VERSION}-alpine
ARG ADDITIONAL_PACKAGE
RUN apk --no-cache add curl alpine-sdk python-dev ${ADDITIONAL_PACKAGE} && \
    apk del curl --no-cache
RUN pip install grpcio

ARG handler_file=handler.py
ARG handler_name=Handler

ENV HANDLER_DIR=/dcf/handler
ENV HANDLER_FILE=${HANDLER_DIR}/${handler_file}
ENV HANDLER_NAME=${handler_name}

RUN mkdir -p ${HANDLER_DIR}
WORKDIR ${HANDLER_DIR}
COPY . .
RUN touch ${HANDLER_DIR}/__init__.py
RUN pip3 install -r requirements.txt

COPY --from=watcher /dcf/watcher ${HANDLER_DIR}

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

ENTRYPOINT ["python3"]
CMD ["server.py"]
