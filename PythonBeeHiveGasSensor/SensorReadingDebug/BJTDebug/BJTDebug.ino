int OnPin=13;
int tickPin=12;
void setup() {
  // put your setup code here, to run once:
  pinMode(OnPin,OUTPUT);
  pinMode(tickPin,OUTPUT);

}

void loop() {
  digitalWrite(OnPin,HIGH);
  while (true){
    digitalWrite(tickPin,HIGH);
    delay(1000);
    digitalWrite(tickPin,LOW);
    delay(1000);
  }
  // put your main code here, to run repeatedly:

}
