from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''<form >
	Category:
        <input type=text size=30 name=category><br>
        Priority:
        <input type=number name=priority ><br>
	Description:
	<input type=text name=description ><br>
        <input type=submit value=Add>
      
    </form>'''


if __name__ == '__main__':
    app.run()
