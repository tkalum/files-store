FROM python:latest
 
WORKDIR /alpha
COPY . /alpha
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python3"]
CMD ["bash","run.sh"]
