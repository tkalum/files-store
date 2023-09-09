
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python3"]
CMD ["bash","run.sh"]
