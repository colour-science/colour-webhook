FROM golang:alpine

WORKDIR /go/src/github.com/adnanh/webhook

ENV PACKAGE webhook
ENV VERSION 2.6.8
ENV URL https://github.com/adnanh/${PACKAGE}/archive/${VERSION}.tar.gz

RUN apk add --update -t build-deps curl gcc libc-dev libgcc
RUN curl -L -o ${PACKAGE}.tar.gz ${URL} && \
    tar -xzf ${PACKAGE}.tar.gz --strip 1 &&  \
    go get -d && \
    go build -o /usr/local/bin/${PACKAGE}

FROM alpine

RUN apk add --update bash git && \
    rm -rf /var/cache/apk/*
COPY --from=0 /usr/local/bin/${PACKAGE} /usr/local/bin/${PACKAGE}

EXPOSE 9000
ENTRYPOINT ["/usr/local/bin/webhook"]