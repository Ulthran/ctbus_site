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

    $resumeUrl = $client->getObjectUrl(getenv('AWS_BUCKET'), 'resume.pdf', '5 minutes');
    $result = $client->getObject([
        'Bucket' => getenv('AWS_BUCKET'),
	'Key' => 'resume.pdf'
    ]);
?>

<style>

</style>

<div id="container">
    <a href="<?php echo $resumeUrl ?>" download>LINK</a>
</div>
@stop
