from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Static routing
@app.route('/')
def fun():
    return "This is an example of static routing"

# Dynamic routing
@app.route('/<var1>')
def fun1(var1):
    return f"This is an example of dynamic routing: {var1}"

# URL redirection (static)
@app.route('/redirect_1st_page')
def fun2():
    return f"This is 1st page of redirection"

@app.route('/redirect_2nd_page')
def fun3():
    return f"This is 2nd page of redirection"

@app.route('/redirect_3rd_page')
def fun4():
    return f"This is 3rd page of redirection"

@app.route('/redirect/<page_no>')
def fun5(page_no=0):
    res = ""
    if page_no == 1:
        res = "/redirect_1st_page"
    elif page_no == 2:
        res = "/redirect_2nd_page"
    elif page_no == 3:
        res = "/redirect_3rd_page"
    else:
        res = "/"
    return redirect(res)

# URL redirection (dynamic)
@app.route('/not_eligible/<int:age>')
def fun6(age):
    return "You are not eligible to vote: "+str(age)

@app.route('/eligible/<int:age>')
def fun7(age):
    return "You are eligible to vote: "+str(age)

@app.route('/voting_age/<int:age>')
def fun8(age):
    res = ""
    if age >= 18:
        res = "/eligible/"+str(age)
    else:
        res = "/not_eligible/"+str(age)
    return redirect(res)

# Integreate HTML, CSS
@app.route('/render_template')
def fun9():
    return render_template('hello.html')

'''
HTTP verbs: -
    1. POST   --> send data to a server to create/update a resource.
    2. GET    --> request data from a specified resource, these request can also be cached.
    3. PUT    --> create a new resource or replace a resource.
    4. DELETE --> delete a specific resource which is identified by a URL.

HTTP code: -
    1. 100 - 199: Informational i.e., request received and continuing process
    2. 200 - 299: Successfull i.e., request received and completed
    3. 300 - 339: Redirection i.e., action needed to complete the request
    4. 400 - 499: Client error i.e., request contain bad syntax or can't be fulfilled
    5. 500 - 599: Server error i.e., failed to fulfill valid request
    6. 600 - 999: non-HTTP status, it should take as a server error
'''
# To render my form.html
@app.route('/form_html')
def myForm():
    return render_template('form.html')

@app.route('/form_submit', methods=['POST','GET'])
def funA():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        gender = request.form['gender']
        empid = request.form['empid']
        desg = request.form['desg']
        phone = request.form['phone']
        emp_dict = [empid,fname+" "+lname,gender,desg,phone]
    return render_template('result.html',output=emp_dict)

if __name__ == '__main__':
    app.run(debug=True)

'''

Note: -
----
1. There are two ways to run flask: -
    (a) In command line: -
        ----------------
        export FLASK_APP=[file name with py extension]
        flask run

    (b) Add below text at the end of the file: -
        if __name__ == '__main__':
            app.run()

        Then run in command line: python [file name with py extension]
    (a) is recommended for deploying purpose.
    (b) is recommended for unit testing purpose. 

2. Re-loader: Reloads the server whenever source code file modifies. (Useful for developent purpose)
                Run in command line: -
                --------------------
                    export FLASK_DEBUG=1
   Debugger: Web-based tool which has interactive stacktrace if any error occurs.
                Run editing main source file: -
                ----------------------------
                    Add debug=True as argument within app.run() e.g., app.run(debug=True)

3. Request-Response Cycle: -
   ----------------------
                               Request using Context
                                     /     \
                                    /       \
            Request                /         \
   Client------------->Flask Server---------->Multiple View Functions with request parameter
            Response                Response

   1. We need different request object for different request.
   2. There are two types of context: -
        (a) app context: current_app (instance of current object), g (handle each request using temporary storage).
        (b) request context: request (encapsulate content of HTTP request sent by client), session (store value in a dictionary that are remembered between the requests).
'''
