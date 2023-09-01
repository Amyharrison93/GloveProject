#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <MPU6050.h>

/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (1000/250)

//Adafruit_BNO055 StoreSensor = Adafruit_BNO055(-1, BNO055_ADDRESS_A);
//Adafruit_BNO055 ReadSensor = Adafruit_BNO055(-1, BNO055_ADDRESS_B);

MPU6050 StoreSensor;
MPU6050 ReadSensor;

int sensor = 0;
int milldiff = 0; 
int startPin = 0;
int endPin = 5;
int PinArry[] = {PIND0,PIND1,PIND2,PIND3,PIND4,PIND5};
int16_t ax, ay, az;
int16_t gx, gy, gz;
float timer = 0;
float startLoopTime = 0;
float endLoopTime = 0;
float loopTime = 0;
String output ="";
float euler[] = {0.0,0.0,0.0};

void setup(void)
{
  Serial.begin(115200);
  while (!Serial) delay(5);
  Wire.begin();

  Serial.println("Glove sensor test: START");
  Serial.println("Calibration status values: 0=uncalibrated, 3=fully calibrated");
  Serial.println("initialise PIN control");

  for (int pin = startPin; pin <= endPin; pin++) {
    pinMode(pin, OUTPUT);
    digitalWrite(pin, HIGH);
  }

  for (int pin = startPin; pin <= endPin; pin++) {
    pinMode(pin, OUTPUT);
    digitalWrite(pin, LOW);
    delay(5);

    ReadSensor.initialize();
    digitalWrite(pin, HIGH);
  }
  Serial.println("initialise complete");
}

void loop(void)
{
  startLoopTime = millis();
  for(sensor = startPin; sensor <= endPin; sensor++){
    digitalWrite(sensor, LOW);

    ReadSensor.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
    euler[0] = map(ax, -17000, 17000, 0, 180);
    euler[1] = map(ay, -17000, 17000, 0, 180);
    euler[2] = map(az, -17000, 17000, 0, 180);

    milldiff = millis() - timer;
    output = output+euler[0]+","+euler[1]+","+euler[2]+","+milldiff+",";
    //output = output+euler[2]+",";
    timer = millis();
    digitalWrite(sensor, HIGH);

    euler[0] = 0;
    euler[1] = 0;
    euler[2] = 0;
  }
  Serial.println(output);
  output = "";

  endLoopTime = millis();
  loopTime = (endLoopTime - startLoopTime);
  if(loopTime < BNO055_SAMPLERATE_DELAY_MS){
    delay(BNO055_SAMPLERATE_DELAY_MS - loopTime);
  }
}
