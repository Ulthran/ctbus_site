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
?>

<div style="text-decoration: underline; display: flex; justify-content: center; padding-top: 10px;">
    <a href="<?php echo $resumeUrl ?>" download>Download Re&#769;sume&#769;</a>
</div>
<div style="display: flex; justify-content: center; padding: 20px;">
    <embed src="<?php echo $resumeUrl; ?>" width="90%" height="1150px"/>
</div>
@stop
