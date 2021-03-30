<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        @include('includes.head')
    </head>
    <body class="font-sans antialiased">
        <div class="min-h-screen bg-gray-100">

            <!-- Page Heading -->
            <header class="bg-white shadow">
                <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
                    @include('includes.header')
                </div>
            </header>

            <!-- Page Content -->
            <main>
                @yield('content')
            </main>

            <!-- Page Footer -->
            <footer>
                @include('includes.footer')
            </footer>
        </div>
    </body>
</html>
