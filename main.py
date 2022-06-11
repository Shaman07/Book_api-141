from flask import Flask,jsonify , request
import csv

all_articles = []
with open('articles.csv') as f:
    df = csv.reader(f)
    data = list(df)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []
not_watched_articles = []

app = Flask(__name__)

@app.route('/get_articles')
def get_articles() :
    return jsonify(
        {
            'data' : all_articles[0],
            'status':'success'
        }
    )

@app.route('/liked_book', methods = ['POST'])
def liked_book() :
    book = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(book)
    return jsonify({
        'status':'success'
    }),200

@app.route('/not_liked_book' , methods = ['POST'])
def not_liked_articles():
    book = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(book)
    return jsonify({
        'status':'success'
    }),200

@app.route('/not_watched_book', methods = ['POST'])
def not_watched_articles():
    book = all_articles[0]
    all_articles = all_articles[1:]
    not_watched_articles.append(book)
    return jsonify({
        'status':'success'
    }),200
    
if __name__ == "__main__":
    app.run()