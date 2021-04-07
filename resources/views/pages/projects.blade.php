@extends('layouts.app')

@section('content')
<?php
    require "/var/www/ctbus_site/vendor/autoload.php";
    use Aws\S3\S3Client;
    use Aws\Exception\AwsException;

    $sharedConfig = [
        'region' => 'us-east-1',
        'version' => 'latest'
    ];

    $sdk = new Aws\Sdk($sharedConfig);
    $client = $sdk->createS3();

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
        $descriptionStr = $description['Body'];

        // Return project clip

    }
?>

<style>

</style>

<div id="container">

</div>
@stop
