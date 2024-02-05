import serial
import time

# Define the serial port and baud rate
port = 'COM7'  # Change this to your Arduino port
baud_rate = 9600

# Initialize the serial connection
ser = serial.Serial(port)

# Wait for a moment to ensure the connection is established
time.sleep(2)

# Send values to Arduino
ser.write(b'Hello, Arduino!')

# Wait for an acknowledgment from Arduino
acknowledgment = ser.readline().decode('utf-8').strip()
print(f"Received acknowledgment from Arduino: {acknowledgment}")

# Close the serial connection
ser.close()
