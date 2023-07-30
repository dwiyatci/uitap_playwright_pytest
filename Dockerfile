FROM mcr.microsoft.com/playwright/python:v1.36.0-jammy

WORKDIR /e2e-testing
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "./docker-entrypoint.sh" ]
CMD [ "pytest", "-s" ]
