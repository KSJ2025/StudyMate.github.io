from flask import *
import sqlite3
app = Flask(__name__)

@app.route('/')
def contact():
    return render_template('KLS.html')

@app.route('/register.html')
def reg():
    return render_template("register.html")

@app.route('/login.html')
def log():
    return render_template("login.html")

@app.route('/KLS.html')
def kls():
    return render_template("KLS.html")

@app.route('/my.html')
def home():
    return render_template("my.html")



@app.route('/my' , methods=["POST"])
def form():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(name,email,message)
        con = sqlite3.connect("kj.db")
        con.execute("INSERT INTO CONTACT(name, email, message) VALUES(?,?,?)",(name,email,message))
        con.commit()
        msg= 'Thank You! our team will be in touch with you shortly'
        return render_template("my.html", msg=msg)

@app.route('/register' , methods=["POST"])
def register():
    if request.method == "POST":
        usn = request.form['usn']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        print(usn,name,email,password)
        con = sqlite3.connect("mydatabase.db")
        con.execute("INSERT INTO users(usn,name,email,password)VALUES(?,?,?,?)",
                     (usn,name,email,password))
        con.commit()
        msg = "Registered successfully!"
        return render_template("register.html", msg=msg)


@app.route('/view')
def view():
    conn = sqlite3.connect("mydatabase.db")
    cur = conn.execute("SELECT *FROM users")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usn = request.form['usn']
        password = request.form['password']
        conn = sqlite3.connect("mydatabase.db")
        cur = conn.execute("SELECT * FROM users WHERE usn=? and password=?",(usn,password))
        row = cur.fetchone()
        if (usn=="admin") and (password=="admin"):
            return render_template("admin.html")
        else:
            if row == None:
                return render_template("login.html", msg="Invalid Id & Password!")
            else:
                return render_template("user.html",row=row)



if __name__ == '__main__':
    app.run(debug=True)