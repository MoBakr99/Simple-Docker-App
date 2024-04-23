FROM python

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir nltk && \
    python -m nltk.downloader stopwords

CMD [ "python" , "Stopwords_Script.py" ]