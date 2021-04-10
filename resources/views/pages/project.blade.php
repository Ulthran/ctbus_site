@extends('layouts.app')

@section('content')
<style>
.container {
    display: flex;
}
.sidebar {
    display: flex;
    width: 25%;
    padding: 20px;
    border: 1px solid #000;
    border-radius: 20px;
    margin: 20px;
}
.title {

}
.overview {

}
.link {
    text-decoration: underline;
}
.body {
    display: flex;
    padding: 20px;
}
</style>

<?php
    require "/var/www/ctbus_site/vendor/autoload.php";
    use Aws\S3\S3Client;
    use Aws\Exception\AwsException;

    header('Content-Type: text/html; charset=utf-8'); // For Chinese characters

    $sharedConfig = [
        'region' => 'us-east-1',
        'version' => 'latest'
    ];

    $sdk = new Aws\Sdk($sharedConfig);
    $client = $sdk->createS3();

    // Get page material from S3
    $body = '';
    $video = '';
    $slides = '';
    $title = $client->getObject([
        'Bucket' => getenv('AWS_BUCKET'),
        'Key' => 'projects/' . $_GET['projName'] . '/title.txt'
    ]);
    $overview = $client->getObject([
        'Bucket' => getenv('AWS_BUCKET'),
        'Key' => 'projects/' . $_GET['projName'] . '/overview.txt'
    ]);
    $links = $client->getObject([
        'Bucket' => getenv('AWS_BUCKET'),
        'Key' => 'projects/' . $_GET['projName'] . '/links.txt'
    ]);
    $linkList = explode(",", $links['Body']);
    try {
        $body = $client->getObject([
            'Bucket' => getenv('AWS_BUCKET'),
            'Key' => 'projects/' . $_GET['projName'] . '/body.pdf'
    	]);
    } catch (S3Exception $e) {
        //echo $e->getMessage();
    } catch (AwsException $e) {
        //echo $e->getAwsRequestId() . "\n";
        //echo $e->getAwsErrorType() . "\n";
        //echo $e->getAwsErrorCode() . "\n";

        //var_dump($e->toArray());
    }
    try {
        $video = $client->getObject([
            'Bucket' => getenv('AWS_BUCKET'),
            'Key' => 'projects/' . $_GET['projName'] . '/video.mp4'
        ]);
    } catch (S3Exception $e) {

    } catch (AwsException $e) {

    }
    try {
        $slides = $client->getObject([
            'Bucket' => getenv('AWS_BUCKET'),
            'Key' => 'projects/' . $_GET['projName'] . '/slides.pptx'
        ]);
    } catch (S3Exception $e) {

    } catch (AwsException $e) {

    }
?>

<div class="container">
    <div class="sidebar">
        <p class="title"><?php echo $title['Body']; ?></p>
        <?php
            foreach ($linkList as $key => $value) {
                ?>
                <a href="<?php echo $value; ?>" class="link"><?php echo $key; ?></a>
                <?php
            }
        ?>
    </div>
    <div class="body">

    </div>
</div>
@stop
