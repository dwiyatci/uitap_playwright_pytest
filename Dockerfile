FROM mcr.microsoft.com/playwright/python:v1.21.0

WORKDIR /e2e-testing
COPY . .

RUN make install

ENTRYPOINT [ "./docker-entrypoint.sh" ]
CMD [ "make", "test_ci" ]
