#include "md5.h"

int main()
{
  MD5 md5 ;
  puts( md5.digestString( "HELLO THERE I AM MD5!" ) ) ;

  // print the digest for a binary file on disk.
  puts( md5.digestFile( "C:\\WINDOWS\\notepad.exe" ) ) ;

  return 0;
}