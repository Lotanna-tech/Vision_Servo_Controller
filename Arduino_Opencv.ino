#include <Servo.h>
Servo servo;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(4);
  servo.write(90);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil("\n");
    if (command == "MOVE") {
      servo.write(180);
      delay(1000);
      servo.write(90);
    }

  }

}
