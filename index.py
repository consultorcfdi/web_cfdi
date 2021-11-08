from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/prods')
def prods():
    return render_template('productos.html')

@app.route('/servs')
def servicios():
    return render_template('servicios.html')

@app.route('/bio')
def c_v():
    return render_template('bio.html')



if __name__=='__main__':
    app.run(debug=True)



