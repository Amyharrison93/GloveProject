#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (200)

Adafruit_BNO055 StoreSensor = Adafruit_BNO055(-1, BNO055_ADDRESS_A);
Adafruit_BNO055 ReadSensor = Adafruit_BNO055(-1, BNO055_ADDRESS_B);

int sensor = 0;
int pattern[] = {0,0,0,0,0,0};
int patternDefault[] = {0,0,0,0,0,0};
int pinOffset = 0;
int milldiff = 0; 
int startPin = 0;
int endPin = 5;
int PinArry[] = {PIND0,PIND1,PIND2,PIND3,PIND4,PIND5};
float timer = 0;
String output ="";
imu::Vector<3> euler;

void setup(void)
{
  Serial.begin(115200);
  while (!Serial) delay(5);

  Serial.println("Glove sensor test: START");
  Serial.println("Calibration status values: 0=uncalibrated, 3=fully calibrated");
  Serial.println("initialise PIN control");

  for (int pin = startPin; pin <= endPin; pin++) {
    pinMode(pin, OUTPUT);
    digitalWrite(pin, HIGH);
    delay(10);

    if(!ReadSensor.begin()){
      Serial.println("no BNO055 detected on pin " + String(pin));
    }
    else{
      Serial.println("BNO055 #" + String(pin) + " found");
    }

    digitalWrite(pin, LOW);
  }
  Serial.println("initialise complete");
}

void loop(void)
{
  for(sensor = startPin; sensor <= endPin; sensor++){
    digitalWrite(sensor, HIGH);
    delay(10);
    ReadSensor.begin()
    delay(10);

    euler = ReadSensor.getVector(Adafruit_BNO055::VECTOR_EULER);

    milldiff = millis() - timer;
    //output = output+euler.x()+","+euler.y()+","+euler.z()+","+milldiff+",";
    output = output+euler.x()+","+euler.y()+","+euler.z()+",";
    timer = millis();

    digitalWrite(PinArry[sensor], LOW);
    digitalWrite(sensor, HIGH);
    digitalWrite(PinArry[sensor], LOW);
    euler = {0,0,0};
  }

  Serial.println(output);
  delay(BNO055_SAMPLERATE_DELAY_MS);

  output = "";
}
