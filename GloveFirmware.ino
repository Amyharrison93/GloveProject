#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (50)

Adafruit_BNO055 SensorRead = Adafruit_BNO055(-1, 0x29, &Wire);
Adafruit_BNO055 bno2 = Adafruit_BNO055(-1, 0x28, &Wire);

int sensor = 0;
float timer = 0;
int pattern[] = {0,0,0,0,0,0};
int patternDefault[] = {0,0,0,0,0,0};
String output ="";
int pinOffset = 0;
int milldiff = 0; 
int PinArry[] = {PIND0,PIND1,PIND2,PIND3,PIND4,PIND5};

void setup(void)
{
  Serial.begin(115200);
  while (!Serial) delay(5);

  Serial.println("Glove sensor test: START"); Serial.println("");

  Serial.println("Calibration status values: 0=uncalibrated, 3=fully calibrated");

  Serial.println("initialise PIN control");

  for (int pin = 0; pin < 6; pin++) {
    pinMode(PinArry[pin], OUTPUT);
    digitalWrite(pin, LOW);

    if(!bno2.begin())
    {
      Serial.print("no BNO055 detected");
      while(1);
    }
    delay(BNO055_SAMPLERATE_DELAY_MS); 
    digitalWrite(pin, HIGH);
  }

  Serial.println("initialise complete");
}

void loop(void)
{
  /* Display the floating point data for each sensor*/
  for(sensor = 0; sensor < 6; sensor++){
    digitalWrite(PinArry[sensor], LOW);

    delay(BNO055_SAMPLERATE_DELAY_MS);
    imu::Vector<3> euler = bno2.getVector(Adafruit_BNO055::VECTOR_EULER);
    
    milldiff = millis() - timer;
    output = output+euler.x()+","+euler.y()+","+euler.z()+","+milldiff+",";
    timer = millis();

    digitalWrite(PinArry[sensor], HIGH);
    
    delay(BNO055_SAMPLERATE_DELAY_MS/12);
  }
  Serial.println(output);
  
  output = "";
}
