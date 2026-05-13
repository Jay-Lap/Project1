

#define BLYNK_TEMPLATE_ID "TMPL6ZOC_J-ny"
#define BLYNK_TEMPLATE_NAME "switch Bot"
#define BLYNK_AUTH_TOKEN "5yg2IrhnSExtHuEtEsbSjvKoZIs0908A"

#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>
#include <ESP32Servo.h>

char auth[] = BLYNK_AUTH_TOKEN;
char ssid[] = "JCN2.4G_3B4D";
char pass[] = "D1632E3B4C";

Servo myServo;
int servoPin = 18; // 서보모터를 18번 핀에 연결

BLYNK_WRITE(V1) {
  int value = param.asInt(); //스위치 읽기 1 or 0

  if (value == 1) { // 스위치 1 입력
    Serial.println("on Switch bot: press");
    myServo.write(45); // 45도 회전
    delay(4000); // 모터 회전 후 4초간 유지
    myServo.write(0); // 0도로 복귀
    Serial.println("off Switch bot: back");
    }
}

void setup() {
  //시리얼 모니터 실행 디버깅용
  Serial.begin(115200);

  //서보 모터 설정
  myServo.attach(18); //18번 친에 서보모터 연결
  myServo.write(0); // 모터가 연결되면 초기 각도를 0도로 복귀함

  //Blynk 서버 연결 설정
  Blynk.begin(auth, ssid, pass); //인증키, 와이파이 이름, 비밀번호로 확인 후 접속
}

void loop() {
  Blynk.run(); //Blynk 서버 접속을 유지
}


