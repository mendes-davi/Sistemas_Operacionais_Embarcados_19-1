1. Crie dois processos, e faça com que o processo-filho gere uma onda quadrada, enquanto o processo-pai faz polling de um botão no GPIO, aumentando a frequência da onda sempre que o botão for pressionado. A frequência da onda quadrada deve começar em 1 Hz, e dobrar cada vez que o botão for pressionado. A frequência máxima é de 64 Hz, devendo retornar a 1 Hz se o botão for pressionado novamente.

```C
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

#include <sys/types.h>
#include <sys/stat.h>

#include <wiringPi.h>

#define IN_PIN 11
#define OUT_PIN 7
#define MAX_FREQ 64
#define MIN_FREQ 1

int freq_pwm = 1;
double delay_time = 500000*(1/freq_pwm);

void change_freq_pwm()
{
    if (freq_pwm == MAX_FREQ)
        freq_pwm = MIN_FREQ;
    else
        freq_pwm = 2 * freq_pwm;
}

int main(int argc, char const *argv[])
{
  pid_t childPid;

  signal(SIGUSR1, change_freq_pwm);

  wiringPiSetup();
  pinMode(OUT_PIN, OUTPUT);
  pinMode(IN_PIN, INPUT);
  pullUpDnControl(IN_PIN, PUD_UP);
      
  childPid = fork();
  if (childPid == 0)
  {
    //Child Code
    while(true)
    {
        digitalWrite(OUT_PIN, HIGH);
        usleep((int) delay_time);
        digitalWrite(OUT_PIN, LOW);
        usleep((int) delay_time);
    }
  }
  else
  {
    //Parent Code

    while(digitalRead(IN_PIN) > 0);
    kill(childPid, SIGUSR1);
    while(digitalRead(IN_PIN) == 0);
    usleep(delay_time);
  }
  return 0;
}
```