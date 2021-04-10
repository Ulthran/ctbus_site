@extends('layouts.app')

@section('content')
<style>
.content {
    display: flex;
    padding: 25px;
    padding-left: 10%;
    padding-right: 10%;
}
</style>
<div class="content">
    <p>Hi there!</p>
    <p>There's some more text here :)</p>
    <?php echo "Look, some PHP"; ?>
</div>
@stop
