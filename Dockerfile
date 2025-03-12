FROM ubuntu:latest
LABEL authors="anarsic"

ENTRYPOINT ["top", "-b"]