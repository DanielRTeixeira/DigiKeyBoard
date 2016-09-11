#include "DigiKeyboard.h"
#define KEY_DELETE 76

  void setup() {
  DigiKeyboard.update();
}

void loop() {
  delay(100);
  DigiKeyboard.update();
  delay(100);
  
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  delay(100);
  DigiKeyboard.sendKeyStroke(KEY_DELETE);
  delay(50);
  DigiKeyboard.println("CMD");
  delay(900000);
}
