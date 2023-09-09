FROM python:latest
 
 
RUN pip install -r requirements.txt
 
CMD ["bash","run.sh"]
