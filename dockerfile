FROM python:latest
 
WORKDIR /chad-post-bot
COPY . /chad-post-bot
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python3"]
CMD ["-m","main.py"]
