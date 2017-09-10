int DAT_A = 6;
int DAT_B = 7;
int CLR = 8;
int CLK = 9;

float PULSE_WIDTH = 0.00000001;
char incoming_byte = 0;

void setup() {
  pinMode(DAT_A, OUTPUT);
  pinMode(DAT_B, OUTPUT);
  pinMode(CLK, OUTPUT);
  pinMode(CLR, OUTPUT);
  
  digitalWrite(DAT_A,LOW);
  digitalWrite(DAT_B,LOW);
  digitalWrite(CLK,HIGH);
  digitalWrite(CLR,HIGH);
  
  Serial.begin(9600);
}

void clear_pulse(){
  digitalWrite(CLR,LOW);
  delay(PULSE_WIDTH);
  digitalWrite(CLR,HIGH);
}

void write_one(int data){
  digitalWrite(DAT_A, data);
  digitalWrite(DAT_B, data);
  delay(PULSE_WIDTH);
  digitalWrite(CLK,LOW);
  digitalWrite(CLK,HIGH);
} 

void loop() {
  if(Serial.available() > 0){
    incoming_byte = Serial.read();
    Serial.write(incoming_byte);
    if(incoming_byte == 'c'){
      clear_pulse();
    } else if(incoming_byte == 'h') {
      write_one(1);
    } else if(incoming_byte == 'l') {
      write_one(0);
    }
  }
}
