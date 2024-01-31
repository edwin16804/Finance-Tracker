from flask import Flask, render_template
#from sqlalchemy import create_engine
#engine = create_engine("mysql+pymysql://root:Edchaz168@localhost/trial?charset=utf8mb4")
import mysql.connector as ms

conn = ms.connect(host="localhost",
                  port=3306,
                  user="root",
                  passwd="Edchaz168",
                  database="trial")

if conn.is_connected():
    print("Hi")

mc=conn.cursor()
mc.execute("select uname from trialusers")
result=mc.fetchone()

print(result)

'''with engine.connect() as conn:
  result=conn.execute(next("select * from trialusers"))
  print(result.all())'''


app = Flask(__name__)


@app.route('/')
def main_page():
  return render_template("start_page.html")


@app.route('/signup')
def login_page():
  return render_template("Signup.html")


@app.route('/login')
def success_page():
  return render_template("login.html",)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

