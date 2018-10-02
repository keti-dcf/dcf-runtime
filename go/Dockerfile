# Argrumnets for FROM
ARG REGISTRY
ARG GO_VERSION=1.9.7
ARG WATCHER_VERSION=0.1.0

# Get watcher - if watcher is uploaded on github, remove this line.
FROM ${REGISTRY}/watcher:${WATCHER_VERSION}-go as watcher

# Function Build & Run
ARG handler_file
ARG handler_name=Handler

ENV HANDLER_DIR=${GOPATH}/src/dcf/handler
ENV HANDLER_FILE=${GOPATH}/src/dcf/handler/handler
ENV HANDLER_NAME=${handler_name}

# Copy dcf-watcher
RUN cp ${GOPATH}/src/github.com/keti-dcf/dcf-watcher/go/dcf-watcher /dcf-watcher
RUN chmod +x /dcf-watcher

# Install dep
RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh

RUN mkdir -p ${HANDLER_DIR}
WORKDIR ${HANDLER_DIR}
COPY . .
RUN dep ensure

# Build handler
RUN go build -o ${HANDLER_FILE} -buildmode=plugin .

HEALTHCHECK --interval=2s CMD [ -e /tmp/.lock ] || exit 1

CMD ["/dcf-watcher"]
