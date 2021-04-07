@extends('layouts.app')

@section('content')
<?php
    function displayProject($projName) {
        // Pull objects from S3
        $description = $client->getObject([
            'Bucket' => getenv('AWS_BUCKET'),
            'Key' => $projName . '/description.txt'
        ]);
        $thumbnail = $client->getObject([
            'Bucket' => getenv('AWS_BUCKET'),
            'Key' => $projName . '/thumbnail.png'
        ]);

        // Dissect
        $descriptionStr = $description['Body']

        // Return project clip

    }
    $resumeUrl = $client->getObjectUrl(getenv('AWS_BUCKET'), 'resume.pdf', '5 minutes');
    $result = $client->getObject([
        'Bucket' => getenv('AWS_BUCKET'),
	'Key' => 'resume.pdf'
    ]);
?>

<style>

</style>

<div id="container">

</div>
@stop
