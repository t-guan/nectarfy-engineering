const int pumpPin = 3;        //pump connected to digital pin 3
const int switchPin = 2;      //switch connected to digital pin 2
int pumpState = 0;             //pump status

void setup() {
  pinMode(pumpPin, OUTPUT);
  pinMode(switchPin, INPUT);
  attachInterrupt(digitalPinToInterrupt(switchPin), stateSwitch, FALLING);
}

void loop() {
  if (pumpState == 1) {
    digitalWrite(pumpPin, HIGH);
    delay(5000); //delaying 5 seconds
    digitalWrite(pumpPin, LOW);
    delay(5000);
  } else {
    digitalWrite(pumpPin, LOW);
  }
}

void stateSwitch() {
  if (pumpState == 0) {
    pumpState = 1;
  } else {
    pumpState = 0;
  }
}
