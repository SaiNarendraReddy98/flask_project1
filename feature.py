from flask import Flask

FAI = Flask(__name__)

@FAI.route('/stringResponse')
def stringResponse():
    return '<center><h1>Hai...! This is the frist Http Response From Flask '



@FAI.route('/stringResponse2')
def stringResponse2():
    return '<center><h1>Hai...! This is the Second Http Response From Flask '





if __name__ == '__main__':
    FAI.run(debug=True)



