from flask import Flask, render_template, request
from model import predict_review, model,tokenizer
from model_image import real_classifier
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sift_logo_classification import predict_output

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    tag = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/products', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        tag = predict_review(desc)
        todo = Todo(title=title, desc=desc,tag=tag)
        db.session.add(todo)
        db.session.commit()
        
    allTodo = Todo.query.all() 
    
    image_tag=real_classifier(r'static/images/adidas.jpeg')
    print('static/images/detected_'+image_tag+'.jpg')
    image_verify=predict_output(image_tag,'static/detected_images/detected_'+image_tag+'.jpg')
    
    return render_template('Pages/Adidas.html', allTodo=allTodo,image_tag=image_verify)

@app.route('/products2', methods=['GET', 'POST'])
def product2():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        tag = predict_review(desc)
        todo = Todo(title=title, desc=desc,tag=tag)
        db.session.add(todo)
        db.session.commit()
        
    allTodo = Todo.query.all() 
    image_tag=real_classifier('static/images/abibas.jpg')
    image_verify=predict_output(image_tag,'static/detected_images/detected_'+image_tag+'.jpg')
    return render_template('Pages/AdidasTShirt.html', allTodo=allTodo,image_verify=image_verify)


@app.route('/products3', methods=['GET', 'POST'])
def product3():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        tag = predict_review(desc)
        todo = Todo(title=title, desc=desc,tag=tag)
        db.session.add(todo)
        db.session.commit()
        
    allTodo = Todo.query.all() 
    image_tag=real_classifier('static/images/nike.jfif')
    image_verify=predict_output(image_tag,'static/detected_images/detected_'+image_tag+'.jpg')
    
    return render_template('Pages/Nike_shoes.html', allTodo=allTodo,image_tag=image_verify)

@app.route('/products4', methods=['GET', 'POST'])
def product4():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        tag = predict_review(desc)
        todo = Todo(title=title, desc=desc,tag=tag)
        db.session.add(todo)
        db.session.commit()
        
    allTodo = Todo.query.all() 
    image_tag=real_classifier('static/images/nipe.jpeg')
    print('static/detected_images/detected_'+image_tag+'.jpg')
    image_verify=predict_output(image_tag,'static/detected_images/detected_'+image_tag+'.jpg')
    print(image_verify)
    return render_template('Pages/Nike.html', allTodo=allTodo,image_tag=image_verify)

@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'this is products page'

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
        
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/products")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
