
Линковка библиотеки под Linux/Mac
```bash
g++ -shared -o ../libcalc.so -fPIC calculate.cc RPNConverter.cc
```

Линковка библиотеки под Windows
```bash
g++ -shared -o ../calc.dll calculate.cc RPNConverter.cc
```