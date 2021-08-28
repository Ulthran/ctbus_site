<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
  <head>
      @include('includes.head')
  </head>

  <body>
    <div class='container'>
      <header class='row'>
        @include('includes.header')
      </header>

      <div id='main' class='row'>
        @yeild('content')
      </div>

      <footer>
        @yeild('includes.footer')
      </footer>
    </div>
  </body>

</html>
