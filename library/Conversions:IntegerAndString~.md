## Conversions:IntegerAndString~

### Overview

This provides functions for converting integers to/from strings in various bases.

### Code

````
"Integer <-> String Conversions"
[ 'hex' 'duodecimal' 'decimal' 'octal' 'senary' 'quinary'
  'quaternary' 'trinary' 'binary' 'unary' 's->n' 'n->s' ]
'Conversions:IntegerAndString~' {
  '0123456789ABCDEF' 'NUMBERS' :
  [ 'Buf' 'Base' 'Digits' 'Res' ] ::

  [ "n-s"
    &Res zero-out
    [ @Base /rem &NUMBERS swap fetch &Res push dup zero? ] until drop
    &Res :s clean-string reverse
  ] 'n->s' :

  [ 0 !Res
    [ :s &NUMBERS :s swap find @Res @Base * + !Res ] for-each
    @Res
  ] 's->n' :

  [ "-" 16 !Base ] 'hex' :
  [ "-" 12 !Base ] 'duodecimal' :
  [ "-" 10 !Base ] 'decimal' :
  [ "-"  8 !Base ] 'octal' :
  [ "-"  6 !Base ] 'senary' :
  [ "-"  5 !Base ] 'quinary' :
  [ "-"  4 !Base ] 'quaternary' :
  [ "-"  3 !Base ] 'trinary' :
  [ "-"  2 !Base ] 'binary' :
  [ "-"  1 !Base ] 'unary' :
  decimal
}}
````
