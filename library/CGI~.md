## CGI~

### Overview

### Code
````
'CGI~' vocab{
  "CGI"
  [ "s-"  'Content-type: ' display display tty.cr tty.cr ] 'content-type' :
  [ "-s"  'PATH_INFO' get-environment-value ] 'PATH_INFO' :
  [ "-f"  PATH_INFO '(no)' eq? ] '-path?' :
  [ "s-f" PATH_INFO eq? ] 'path?' :


  "General Structure"
  [ [ '<html>' ] dip invoke '</html>' ] 'html' :
  [ [ '<head>' ] dip invoke '</head>' ] 'head' :
  [ [ '<body>' ] dip invoke '</body>' ] 'body' :
  [ [ '<html>' ] dip invoke '</html>' ] 'html' :
  [ [ '<head>' ] dip invoke '</head>' ] 'head' :
  [ [ '<body>' ] dip invoke '</body>' ] 'body' :
  [ [ '<span>' ] dip invoke '</span>' ] 'span' :
  [ [ '<span class="{v}">' interpolate ] dip invoke '</span>' ] 'span:class' :
  [ [ '<span id="{v}">' interpolate ] dip invoke '</span>' ] 'span:id' :
  [ [ '<div>' ] dip invoke '</div>' ] 'div' :
  [ [ '<div class="{v}">' interpolate ] dip invoke '</div>' ] 'div:class' :
  [ [ '<div id="{v}">' interpolate ] dip invoke '</div>' ] 'div:id' :

  "CSS"
  [ [ '<style>' ] dip invoke '</style>' ] 'css' :
  [ [ '<link rel="stylesheet" href="' ] dip invoke '"/>' ] 'stylesheet' :

  "Metadata"
  [ [ '<title>' ] dip invoke '</title>' ] 'title' :
  [ '<meta name="viewport" content="width=device-width, initial-scale=1">' ] 'meta:viewport' :

  "JavaScript"
  [ [ '<script>' ] dip invoke '</script>' ] 'script' :

  "Links"
  [ '<a href="{v}">{v}</a>' interpolate ] 'link' :

  "Content Formatting"
  [ [ '<h1>' ] dip invoke '</h1>' ] 'h1' :
  [ [ '<h2>' ] dip invoke '</h2>' ] 'h2' :
  [ [ '<h3>' ] dip invoke '</h3>' ] 'h3' :
  [ [ '<h4>' ] dip invoke '</h4>' ] 'h4' :
  [ [ '<em>' ] dip invoke '</em>' ] 'em' :
  [ [ '<strong>' ] dip invoke '</strong>' ] 'strong' :
  [ [ '<p>' ] dip invoke '</p>' ] 'p' :
  [ [ '<p class="{v}">' interpolate ] dip invoke '</p>' ] 'p:class' :
  [ [ '<p id="{v}">' interpolate ] dip invoke '</p>' ] 'p:id' :
  [ [ '<pre>' ] dip invoke '</pre>' ] 'pre' :
  [ [ '<pre class="{v}">' interpolate ] dip invoke '</pre>' ] 'pre:class' :
  [ [ '<pre id="{v}">' interpolate ] dip invoke '</pre>' ] 'pre:id' :
  [ [ '<code>' ] dip invoke '</code>' ] 'code' :
  [ [ '<code class="{v}">' interpolate ] dip invoke '</code>' ] 'code:class' :
  [ [ '<code id="{v}">' interpolate ] dip invoke '</code>' ] 'code:id' :
  [ '<hr>' ] 'hr' :
}vocab
````
