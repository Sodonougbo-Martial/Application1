
#include <stdlib.h>
#include <stdio.h>

int my_print_revalpha(void)

{

  char c;
  for(c='z';c>='a';c--)
    putchar((int)c);
  return 0 ;
}


//int main(void)
//{
//  my_print_revalpha(); //appeller la fonction qu'on veut
//
//  return 0 ;
//}
