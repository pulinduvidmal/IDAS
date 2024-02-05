void setup() {
  Serial.begin(9600);  // Use the same baud rate as in the Python script
}

void loop() {
  if (Serial.available() > 0) {
    // Read the received values
    String receivedData = Serial.readString();
    Serial.println(receivedData);

    // Send acknowledgment back to Python
    Serial.println("Data received successfully!");
  }
}
