//creamos la variable donde guardaremos la circunferencia de las llantas expresada en cm

float CircunferenciaRueda = 15.707963267948966192313216916397514420985/12;

//definimos el pin del rele
int rele = 4;

//iniciamos la variable para el contador de riego
int ContadorRiego = 0;
//Luego le asignamos el pin al que esta conectado el sensor hall
const int SensorEncoder = 11;
//configuramos sus variables de estado
//creamos la variable de estado de la ultima pulsacion del sensor hall
//creamos la variable de estado actual del sensor hall
int UltimoSensor[800];

//creamos las variables para el motor
int MotorA = 9;
int MotorA1 = 3;
int MotorA2 = 2;

//creamos la variable para la rueda girando
boolean RuedaGirando = LOW;
//creamos la variable para el tiempo que lleva girando la rueda
unsigned long TiempoInicioRuedaGirando = 0;
unsigned long TiempoActual2 = 0;
//creamos la variable para la hora de inicio de la ultima revolucion
unsigned long TiempoInicioUltimaRevolucion = 0;
//creamos la variable para el tiempo de revolcion
unsigned long TiempoRevolucion = 0;
unsigned long ContadorEncoder = 0;
unsigned long ContadorEncoder2 = 0;
unsigned long ContadorArray = 0;
//Creamos la variable para la distancia actual
float DistanciaActual;
//creamos la variable para la duracion actual
unsigned long DuracionActual;

//creamos la variable para el tiempo actual
unsigned long TiempoActual = 0;
//Creamos la variable para la distancia
float cm = 0.00;
float cm2 = 0.00;
//Creamos la variable para la velocidad
float cpm = 0.00;


//creamos las variables para las unidades de milisegundos para cada uno
unsigned long milliSecondsInSecond = 1000;
unsigned long milliSecondsInMinute = 60000;
unsigned long milliSecondsInHour = 3600000;

//Creamos la funcion para configurar las variables setup()

void setup()
{
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);
    pinMode(SensorEncoder, INPUT_PULLUP);
		pinMode(rele,OUTPUT);
    pinMode(MotorA, OUTPUT);
    pinMode(MotorA1, OUTPUT);
    pinMode(MotorA2, OUTPUT);
  	delay(1000);
   //hacemos funcionar el motor
    digitalWrite(MotorA1,HIGH);
    digitalWrite(MotorA2,LOW);
    digitalWrite(rele, LOW);
    analogWrite(MotorA,255);
    Serial.print("Inicio");
}

void loop()
{
    ContadorArray = ContadorArray + 1;
    //inicializamos la variable tiempo actual con la funcion de tiempo millis() de arduino
    TiempoActual = millis();
    TiempoActual2 = millis();
    //leemos las revoluciones del sensor hall
    if(ContadorArray == 800){
      ContadorArray = 1;
    }
    delay(70);
    UltimoSensor[ContadorArray] = digitalRead(SensorEncoder);
    
    //si la ultima revolucion es high y la revolucion actual es low
    if(UltimoSensor[ContadorArray] != UltimoSensor[ContadorArray-1]){
        // Si el mensaje inicial "PRESIONE EL BOTÓN PARA INICIAR" no se muestra y no está actualmente en pausa...
            // Aumentar el número de revoluciones de la rueda
            ContadorEncoder = ContadorEncoder + 1;
            ContadorEncoder2 = ContadorEncoder2 + 1;
            Serial.println(cm2);
            // Muestra "+" para mostrar que se registró una revolución
            //decimos que la rueda ya esta girando
            RuedaGirando = HIGH;
            //guardamos en la variable el tiempo que la rueda lleva girando
            TiempoInicioRuedaGirando = TiempoActual;
            // Calcula los milisegundos necesarios para esta última revolución.
            if(ContadorEncoder > 0 ){
                //el tiempo de revolucion va a ser igual al tiempo actual - el tiempo de la ultima revolucion
                //calculamos la distancia total recorrida multiplicando las revoluciones por hora por la circunferencia de la rueda
                cm = ContadorEncoder * (CircunferenciaRueda);
                cm2 = ContadorEncoder2 * (CircunferenciaRueda);
                
                // Calcula la velocidad actual en kilómetros por hora según el tiempo que tardó en completar la última revolución de la rueda
                //para esto dividimos la distancia por el tiempo V = x/t
                cpm = cm/TiempoActual;
            }
    }
  if(cm2 > 49 && cm2 < 51){
      digitalWrite(rele, HIGH);
      delay(1000);
      digitalWrite(rele, LOW);
      Serial.println("un giro");
      cm2 = 0;
      ContadorEncoder2 = 0;
    }
  if(cm/2 > 1000.00){
        Serial.print("acabo");
        analogWrite(MotorA,0);
        digitalWrite(MotorA1, LOW);
        digitalWrite(rele, LOW);
        cm2 = 50;
    }
}