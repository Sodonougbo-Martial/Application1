#include <stdlib.h>
#include <stdio.h>

int my_print_digits(void)

{

  char c;
  for(c='0';c<='9';c++)
    putchar((int)c);
  return 0 ;
}


//int main(void)
//{
//  my_print_digits(); //appeller la fonction qu'on veut
//
//  return 0;
//}
