FROM python:3.10-alpine
RUN mkdir /app && apk add ffmpeg
COPY *.py /app
WORKDIR /app
RUN pip install flask yandex_speechkit
EXPOSE 8080
CMD ["python","/app/speechserver.py"]