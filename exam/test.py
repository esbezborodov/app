from flask import Flask, render_template, request

app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def first():
    if request.method=='POST':
        str=request.form.get("fstring")
        
        result=' '.join(i for i in str.split() if not any(c.isdigit() for c in i))

    return render_template("first.html", result=result)

if __name__=='__main__':
    app.run(debug=True)