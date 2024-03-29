from flask import Flask, render_template
from flask_serial import Serial

app = Flask(__name__)
app.config['SERIAL_TIMEOUT'] = 0.2
app.config['SERIAL_PORT'] = '/dev/ttyUSB0'
app.config['SERIAL_BAUDRATE'] = 19200
app.config['SERIAL_BYTESIZE'] = 8
app.config['SERIAL_PARITY'] = 'N'
app.config['SERIAL_STOPBITS'] = 1


ser = Serial(app)

@app.route('/')
def use_serial():
    return render_template('main.html')

@app.route('/homeplus')
def homescoreUp():
    ser.on_send("0")
    return("Homescore Up")

@app.route('/homeminus')
def homescoreDown():
    ser.on_send("1")
    return("Homescore Down")

@app.route('/clear')
def homescoreClear():
    ser.on_send("2")
    return("Homescore Clear")
    
@app.route('/awayplus')
def guestscoreUp():
    ser.on_send("3")
    return("Guestscore Up")

@app.route('/awayminus')
def guestscoreDown():
    ser.on_send("4")
    return("Guestscore Down")
    
@app.route('/roundplus')
def inningscoreUp():
    ser.on_send("5")
    return("InningSore Up")
   
@app.route('/roundminus')
def inningscoreDown():
    ser.on_send("6")
    return("Inningscore Down")
    
@app.route('/strike')
def strikeTotal():
    ser.on_send("7")
    return("Strike Total")
    
@app.route('/ball')
def ballTotal():
    ser.on_send("8")
    return("Ball Total")
    
@app.route('/out')
def outTotal():
    ser.on_send("9")
    return("Out Total")
    
@app.route('/calendar')
def calendar():
    ser.on_send("a")
    return("Calendar")
    
@ser.on_message()
def handle_message(msg):
    stripped = msg.decode()
    print("receive a message:", stripped)

@ser.on_log()
def handle_logging(level, info):
    print(level, info)
    

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
