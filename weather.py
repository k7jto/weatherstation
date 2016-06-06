from flask import Flask, render_template
import time
import datetime
import serial
app = Flask(__name__)
port = serial.Serial("/dev/ttyACM1", baudrate=9600)

@app.route("/")
def hello():
    # First, set the time
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    
    # Next, get weather data from Arduino via serial
    # Uses int to request temp, press, humidiy
    #port.write('1')		# write 1 for temp
    #tmp = port.readline()	# receive temp

    #port.write('2')		# write 2 for pressure
    #bmp = port.readline()	# receive pressure

    #port.write('3')		# write 3 for humidity
    #hum = port.readline()	# receive humidity
    
    #port.write('4')		# write 4 for windspeed
    #wspd = port.readline()	# receive windspeed

    #port.write('5')		# write 5 for winddir
    #wdir = port.readline()	# receive winddir

    #port.write('6')		# write 6 for light
    #light = port.readline()	# receive light
    
     # Next, get weather data from Arduino via serial
    # Uses int to request temp, press, humidiy
    port.write('7')		# write 1 for temp
    tmp = port.readline()	# receive temp

    #port.write('2')		# write 2 for pressure
    bmp = port.readline()	# receive pressure

    #port.write('3')		# write 3 for humidity
    hum = port.readline()	# receive humidity
    
    #port.write('4')		# write 4 for windspeed
    wspd = port.readline()	# receive windspeed

    #port.write('5')		# write 5 for winddir
    wdir = port.readline()	# receive winddir

    #port.write('6')		# write 6 for light
    light = port.readline()	# receive light
    
    templateData = {
        'title' : 'Weather!',
        'time' : timeString,
        'temperature' : tmp,
        'pressure' : bmp,
        'humidity' : hum,
        'windspeed' : wspd,
        'winddir' : wdir,
        'light' : light
        }
    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)