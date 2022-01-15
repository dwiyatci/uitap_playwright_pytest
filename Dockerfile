FROM mcr.microsoft.com/playwright:v1.17.2

WORKDIR /e2e-testing
COPY . .

RUN make install

ENTRYPOINT [ "./docker-entrypoint.sh" ]
CMD [ "make", "test_ci" ]
