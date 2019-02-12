#include <Servo.h>
#include <Ethernet.h>
#include <SPI.h>

Servo myservo;
int pos = 0;


byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
//byte ip[] = {192, 168, 0, 105    };
byte server[] = { 192, 168, 0, 102 }; 


EthernetClient client;

void setup() {
  Serial.begin(9600);
  myservo.attach(9);
  Serial.println("connecting...");
  
  int ret = Ethernet.begin(mac);
  Serial.println(ret);

  delay(1000);

  Serial.println("connecting...");

  if (client.connect(server, 5005)) {
    Serial.println("connected");
    //client.println("G");
  } else {
    Serial.println("connection failed");
  }
}

void loop() {
  client.print("G");
  delay(10);
  int p_value = 0;
  char p[3] = {'0','0','0'};
  int i = 0;
  bool got = false;
  Serial.print("Get: ");
  while (client.available()) {
    char c = client.read();
    if (i < 3){
      p[i] = c;
      i++;
      got = true;
    }    
  }
  if (got){
    int digits = i;
    i = i -1;
    
    for (int k = 0; k < digits; k++){
      p_value = (p[k]-48)*round(pow(10,i)) + p_value;
      i--;
    }
    pos = p_value;
    myservo.write(pos);
    delay(200);
    Serial.print(pos);
  }
  Serial.print("\n");
  

  client.print(pos);
  delay(10);
  Serial.print("Post: ");
  while (client.available()) {
    char c = client.read();
    Serial.print(c);
  }
  Serial.print("\n");
  if (!client.connected()) {
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();
    for(;;)
      ;
  }
}
