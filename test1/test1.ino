char serialChar='q';
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()>0){
    serialChar=Serial.read();
    
    if(serialChar=='1'){
      digitalWrite(LED_BUILTIN, HIGH);
      delay(288);
    }
    
    if(serialChar=='0'){
      digitalWrite(LED_BUILTIN, LOW);
      delay(288);
    }
    
  }
                       
}
