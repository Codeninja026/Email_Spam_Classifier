
import string
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize
import nltk.stem
from nltk.stem import WordNetLemmatizer
from flask import Flask,request, jsonify, render_template
import pickle


def rem_stop_words(text):
    l = []
    stop_words = stopwords.words('english')
    for word in text:
        if word not in stop_words:
            l.append(word)
    text = ' '.join(l)
    return text


def preprocess(text):
    exclude = string.punctuation
    word_net_Lemma = WordNetLemmatizer()

    text = text.lower()
    text = text.translate(str.maketrans('', '', exclude))
    text = word_tokenize(text)
    text = rem_stop_words(text)

    final_sen = []
    for word in text.split():
        final_sen.append(word_net_Lemma.lemmatize(word))
    return ' '.join(final_sen)


app  = Flask(__name__)


model = pickle.load(open('email_spam.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    text = request.form['email']
    text = preprocess(text)
    final_text = vectorizer.transform([text])

    prediction = model.predict(final_text)

    result = "Spam" if prediction == 1 else "Not Spam"
    return render_template('index.html', prediction=result,)


if __name__=='__main__':
    app.run(host='localhost',debug=True)




