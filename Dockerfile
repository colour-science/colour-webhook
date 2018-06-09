FROM golang:alpine3.7

WORKDIR /go/src/github.com/adnanh/webhook

ENV PACKAGE webhook
ENV VERSION 2.6.8

RUN apk add --update -t build-deps curl gcc libc-dev libgcc
RUN curl -L -o ${PACKAGE}.tar.gz https://github.com/adnanh/${PACKAGE}/archive/${VERSION}.tar.gz && \
    tar -xzf ${PACKAGE}.tar.gz --strip 1 &&  \
    go get -d && \
    go build -o /usr/local/bin/${PACKAGE} && \
    apk del --purge build-deps && \
    rm -rf /var/cache/apk/* && \
    rm -rf /go

FROM alpine:3.7

RUN apk add --update bash git && \
    rm -rf /var/cache/apk/*
COPY --from=0 /usr/local/bin/${PACKAGE} /usr/local/bin/${PACKAGE}

EXPOSE 9000
ENTRYPOINT ["/usr/local/bin/webhook"]