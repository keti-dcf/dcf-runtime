# Argruments from FROM
ARG REGISTRY
ARG WATCHER_VERSION=0.1.0

# Get watcher - if watcher is uploaded on github, remove this line.
FROM ${REGISTRY}/watcher:${WATCHER_VERSION}-python3 as watcher

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

RUN cp -r /dcf/watcher/* ${HANDLER_DIR}

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

ENTRYPOINT ["python3"]
CMD ["server.py"]
