from flask import Flask, render_template, request, redirect, session,url_for
#from sqlalchemy import create_engine
#engine = create_engine("mysql+pymysql://root:Edchaz168@localhost/trial?charset=utf8mb4")
import mysql.connector as ms

conn = ms.connect(host="localhost",
                  port=3306,
                  user="root",
                  passwd="Edchaz168",
                  database="dbms_proj")

if conn.is_connected():
    print("Hi")

mc=conn.cursor()

app = Flask(__name__)



@app.route('/')
def main_page():
  return render_template("start_page.html")


@app.route('/signup')
def signup_page():
  return render_template("Signup.html")

@app.route('/fill_details', methods=['POST'])
def enter_details():
  if request.method == 'POST':
    global uname
    uname=request.form['username']
    passwd=request.form['password']
    mc.execute("select uname from users where uname=%s",(uname,))
    result=mc.fetchall()
    conn.commit()
    if result!=[]:
      err='Username already exists'
      return render_template("Signup.html",err=err)
    else:
      mc.execute("insert into users values(%s,%s)",(uname,passwd))
      conn.commit()
      return render_template("fill_details.html",result=result)

@app.route('/start/login')
def login_page():
  return render_template("login.html")
@app.route('/login', methods=['POST'])
def success_page():
  if request.method == 'POST':
    fname=request.form['firstname']
    lname=request.form['lastname']
    email=request.form['email']
    phone=request.form['pnumber']
    budget=request.form['budget']
    savings=request.form['savings']
    print(uname,fname,lname,email,phone,budget,savings)
    phone=int(phone)
    budget=int(budget)
    savings=int(savings)
    mc.execute("insert into account_info values(%s,%s,%s,%s,%s,%s,%s)",(uname,fname,lname,email,phone,budget,savings))
    conn.commit()
    return render_template("login.html")
  else:
    return render_template("login.html")


@app.route('/dashboard', methods=['POST'])
def dashboard_page():
  if request.method == 'POST':
    global uname
    uname=request.form['username']
    passwd=request.form['password']
    mc.execute("select * from users where uname=%s and password=%s",(uname,passwd))
    result=mc.fetchall()
    conn.commit
    if result!=[]:
      mc.execute("select * from account_info where uname=%s",(uname,))
      result=mc.fetchall()
      conn.commit()
      for result in result:
          fname=result[1]
          lname=result[2]
          email=result[3]
          pno=result[4]
          budget=result[5]
          savings=result[6]
          
      mc.execute("select * from fixed_expenses where uname=%s",(uname,))
      result_fixed=mc.fetchall()
      conn.commit()
      mc.execute("select * from daily_expenses where uname=%s",(uname,))
      result_daily=mc.fetchall()
      conn.commit()
      if result_fixed!=[] and result_daily==[]:
        mc.execute("select sum(amount) from fixed_expenses where uname=%s",(uname,))
        l=mc.fetchall()
        print(l)
        total_expense=l[0][0]
        conn.commit()
        budget=budget-total_expense
        return render_template("dashboard.html",total_expense=-total_expense,result_fixed=result_fixed,uname=uname,fname=fname,lname=lname,email=email,pno=pno,budget=budget,savings=savings)
      elif result_fixed==[] and result_daily!=[]:
        mc.execute("select sum(amount) from daily_expenses where uname=%s",(uname,))
        l=mc.fetchall()
        print(l)
        total_expense=l[0][0]
        conn.commit()
        budget=budget-total_expense
        return render_template("dashboard.html",total_expense=-total_expense,result_daily=result_daily,uname=uname,fname=fname,lname=lname,email=email,pno=pno,budget=budget,savings=savings)
      elif result_fixed!=[] and result_daily!=[]:
        mc.execute("select sum(amount) from fixed_expenses where uname=%s",(uname,))
        l=mc.fetchall()
        print(l)
        fixed_expense=l[0][0]
        conn.commit()
        mc.execute("select sum(amount) from daily_expenses where uname=%s",(uname,))
        l1=mc.fetchall()
        print(l)
        daily_expense=l1[0][0]
        conn.commit()
        total_expense=fixed_expense + daily_expense
        budget=budget-total_expense
        return render_template("dashboard.html",total_expense=-total_expense,result_daily=result_daily,result_fixed=result_fixed,uname=uname,fname=fname,lname=lname,email=email,pno=pno,budget=budget,savings=savings)
      elif result_fixed==[] and result_daily==[]:
        return render_template("dashboard.html",uname=uname,fname=fname,lname=lname,email=email,pno=pno,budget=budget,savings=savings)
    else:
      err="Invalid username or password!"
      return render_template("login.html",err=err)

@app.route('/user_dashboard')
def user_dashboard_page():
      mc.execute("select * from account_info where uname=%s",(uname,))
      result=mc.fetchall()
      conn.commit()
      for result in result:
          fname=result[1]
          lname=result[2]
          email=result[3]
          pno=result[4]
          budget=result[5]
          savings=result[6]
          
      mc.execute("select * from fixed_expenses where uname=%s",(uname,))
      result_fixed=mc.fetchall()
      conn.commit()
      mc.execute("select * from daily_expenses where uname=%s",(uname,))
      result_daily=mc.fetchall()
      conn.commit()
      if result_fixed!=[] and result_daily==[]:
        mc.execute("select sum(amount) from fixed_expenses where uname=%s",(uname,))
        l=mc.fetchall()
        print(l)
        total_expense=l[0][0]
        conn.commit()
        budget=budget-total_expense
        return render_template("dashboard.html",total_expense=-total_expense,result_fixed=result_fixed,uname=uname,fname=fname,lname=lname,email=email,pno=pno,budget=budget,savings=savings)
      elif result_fixed==[] and result_daily!=[]:
        mc.execute("select sum(amount) from daily_expenses where uname=%s",(uname,))
        l=mc.fetchall()
        print(l)
        total_expense=l[0][0]
        conn.commit()
        budget=budget-total_expense
        return render_template("dashboard.html",total_expense=-total_expense,result_daily=result_daily,uname=uname,fname=fname,lname=lname,email=email,pno=pno,budget=budget,savings=savings)
      elif result_fixed!=[] and result_daily!=[]:
        mc.execute("select sum(amount) from fixed_expenses where uname=%s",(uname,))
        l=mc.fetchall()
        print(l)
        fixed_expense=l[0][0]
        conn.commit()
        mc.execute("select sum(amount) from daily_expenses where uname=%s",(uname,))
        l1=mc.fetchall()
        print(l)
        daily_expense=l1[0][0]
        conn.commit()
        total_expense=fixed_expense + daily_expense
        budget=budget-total_expense
        return render_template("dashboard.html",total_expense=-total_expense,result_daily=result_daily,result_fixed=result_fixed,uname=uname,fname=fname,lname=lname,email=email,pno=pno,budget=budget,savings=savings)
      elif result_fixed==[] and result_daily==[]:
        return render_template("dashboard.html",uname=uname,fname=fname,lname=lname,email=email,pno=pno,budget=budget,savings=savings)



@app.route('/fixed_expenses',methods=['POST'])
def fixed_expenses():
  if request.method == 'POST':
    amt=request.form['fixed_amount']
    amt=int(amt)
    cat=request.form['category']
    des=request.form['desc']
    ma=request.form['m/a']
    sdate=request.form['start_date']
    mc.execute("insert into fixed_expenses values(%s,%s,%s,%s,%s,%s)",(uname,amt,cat,des,ma,sdate))
    conn.commit()
    return redirect(url_for('user_dashboard_page'))

@app.route('/daily_expenses',methods=['POST'])
def daily_expenses():
  if request.method == 'POST':
    amt=request.form['daily_amount']
    amt=int(amt)
    cat=request.form['daily_category']
    des=request.form['daily_desc']
    mc.execute("insert into daily_expenses values(%s,%s,%s,%s,curdate())",(uname,amt,cat,des))
    conn.commit()
    return redirect(url_for('user_dashboard_page'))
  

@app.route('/income',methods=['POST'])
def income():
  if request.method=='POST':
     return redirect(url_for('user_dashboard_page'))
  
@app.route('/loan',methods=['POST'])
def loan():
  if request.method=='POST':
     return redirect(url_for('user_dashboard_page'))



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

