int ZeroVal=0;
int ThreeVal=0;
int TwoVal=0;
int TwentyVal=0;
int EightVal=0;
int ebyte=255;
int incomingByte=0;
int runtime=0;
int i=0;

int ZeroPin=A0;
int ThreePin=A1;
int TwoPin=A2;
int TwentyPin=A3;
int EightPin=A4;
int pumpPin=2;
int airPin=10;
int ethPin=11;


//VALUES OUT OF DATE
//TGS2620 536 neutral reading (Detected 70% Ethyl Alcohol)
//TGS2602 627 netural reading
//TGS2600 542 netural Reading (Detected 70% Eythl Alcohol
//TGS2603 583 neutral reading


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(pumpPin,OUTPUT);
  pinMode(airPin,OUTPUT);
  pinMode(ethPin, OUTPUT);


}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte=='H'){
      while(true){
        ZeroVal=analogRead(A0);
        ThreeVal=analogRead(A1);
        TwoVal=analogRead(A2);
        TwentyVal=analogRead(A3);
        EightVal=analogRead(A4);
              
        Serial.println(ZeroVal);
        Serial.println(ThreeVal);
        Serial.println(TwoVal);
        Serial.println(TwentyVal);
        Serial.println(EightVal);
        Serial.println(ebyte);
        delay(500);
        incomingByte = Serial.read();
        if(incomingByte=='L'){
          digitalWrite(LED_BUILTIN, HIGH); 
          break;
        }
      }
    incomingByte=0;
    }
    if (incomingByte=='M'){
      while(true){
        digitalWrite(airPin,LOW);
        digitalWrite(ethPin,LOW);
        digitalWrite(pumpPin,HIGH);
        incomingByte = Serial.read();
        if(incomingByte=='O'){
          digitalWrite(pumpPin,LOW); 
          break;
        }
      }
    incomingByte=0;
    }
    if(incomingByte=='A'){
      digitalWrite(airPin,HIGH);
    }
    if(incomingByte=='E'){
      digitalWrite(ethPin,HIGH);
    }
  }
  
}
