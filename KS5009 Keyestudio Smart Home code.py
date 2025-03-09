#include <Arduino.h>
#include <DHT.h>
#include <MFRC522.h>
#include <SPI.h>

// Define Pins
#define DHTPIN 4         // DHT11 sensor pin
#define DHTTYPE DHT11    // DHT sensor type
#define PIRPIN 13        // PIR motion sensor pin
#define RELAYPIN 15      // Relay module pin
#define REDPIN 18        // RGB LED Red
#define GREENPIN 19      // RGB LED Green
#define BLUEPIN 21       // RGB LED Blue
#define SS_PIN 5         // RFID SS pin
#define RST_PIN 22       // RFID reset pin

// Initialize DHT sensor
DHT dht(DHTPIN, DHTTYPE);

// Initialize RFID
MFRC522 rfid(SS_PIN, RST_PIN);

void setup() {
    Serial.begin(115200);
    dht.begin();
    SPI.begin();
    rfid.PCD_Init();
    
    // Set pin modes
    pinMode(PIRPIN, INPUT);
    pinMode(RELAYPIN, OUTPUT);
    pinMode(REDPIN, OUTPUT);
    pinMode(GREENPIN, OUTPUT);
    pinMode(BLUEPIN, OUTPUT);
    
    digitalWrite(RELAYPIN, LOW);  // Ensure relay is off
}

void loop() {
    // Read temperature and humidity
    float temperature = dht.readTemperature();
    float humidity = dht.readHumidity();
    
    if (isnan(temperature) || isnan(humidity)) {
        Serial.println("Failed to read from DHT sensor!");
    } else {
        Serial.print("Temperature: ");
        Serial.print(temperature);
        Serial.print(" C, Humidity: ");
        Serial.print(humidity);
        Serial.println("%");
    }
    
    // Read PIR sensor
    int motionDetected = digitalRead(PIRPIN);
    if (motionDetected) {
        Serial.println("Motion detected!");
        digitalWrite(RELAYPIN, HIGH);  // Turn on relay
        setRGBColor(255, 0, 0);        // Red color on motion
    } else {
        digitalWrite(RELAYPIN, LOW);   // Turn off relay
        setRGBColor(0, 255, 0);        // Green color when no motion
    }
    
    // Check for RFID card
    if (rfid.PICC_IsNewCardPresent() && rfid.PICC_ReadCardSerial()) {
        Serial.print("RFID UID: ");
        for (byte i = 0; i < rfid.uid.size; i++) {
            Serial.print(rfid.uid.uidByte[i] < 0x10 ? " 0" : " ");
            Serial.print(rfid.uid.uidByte[i], HEX);
        }
        Serial.println();
        
        rfid.PICC_HaltA(); // Halt PICC
        rfid.PCD_StopCrypto1(); // Stop encryption on PCD
    }
    
    delay(2000);  // Delay for sensor stabilization
}

void setRGBColor(int red, int green, int blue) {
    analogWrite(REDPIN, red);
    analogWrite(GREENPIN, green);
    analogWrite(BLUEPIN, blue);
}
