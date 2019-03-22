#include <Arduino.h>
void serialRead();

void setup() {
  Serial1.begin(9600);
  Serial.begin(9600);
  Serial.println("begin");
  // put your setup code here, to run once:
}

void loop() {
  serialRead();
}

void serialRead(){
  char buff[8];
  while(Serial1.available()>=1){
    Serial1.readBytes(buff, 1);
    Serial1.print(buff);
    }
}