FROM python:3.6
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN groupadd -r tallessa && useradd -r -g tallessa tallessa && \
    pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app
RUN env DEBUG=1 python manage.py collectstatic --noinput && \
    python -m compileall -q . && \
    mkdir -p /usr/src/app/media && \
    chown tallessa:tallessa /usr/src/app/media
VOLUME /usr/src/app/media
USER tallessa
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
