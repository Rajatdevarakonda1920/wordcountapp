from flask import Flask , render_template , request
import numpy as np
import nltk
from nltk import FreqDist
import string 
import joblib
def word_count(data):
    
    punct = string.punctuation
    sent = len(nltk.sent_tokenize(data))
    words = [word for word in nltk.word_tokenize(data) if word not in punct]
    freq = FreqDist(nltk.word_tokenize(" ".join(words)))
    char = (" ".join(words))
    char_count = len(char)
    word_count = len(words)
    res = dict()
    res['freq'] = freq
    res['sent'] = sent
    res['char'] = char_count
    res['words'] = word_count

    return res
#initialise the app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')




@app.route('/predict' , methods = ['post'])
def predict():
    if request.method == 'POST':
        data =  request.form.get('paragraph_text')
        result = word_count(data)
        r1 = result.get('sent')
        r2 = result.get('words')
        r3 = result.get('char')
        r4 = result.get('freq')


    return render_template('predict.html',value= f'Number of Sentences in given Input text are ==> {r1}',value1= f'Number of Words in given Input text are ==> {r2}',
                            value2= f'Number of Words in given Input text are ==> {r3}',value3= f'Frequency of Words in given Input text are ==> {r4}')





if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port=8080)
