@extends('layouts.app')

@section('content')
<style>
.container {
    display: flex;
}
.sidebar {
    display: flex;
    flex-direction: column;
    width: 25%;
    padding: 20px;
    border-radius: 20px;
    margin: 20px;
}
.title {
    font-size: 25px;
    font-weight: bold;
    padding-bottom: 20px;
}
.overview {

}
.link {
    text-decoration: underline;
}
.body {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    padding: 20px;
    width: 100%;
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
    $bodyUrl = '';
    $videoUrl = '';
    $slidesUrl = '';
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
    $linkList = [];
    if($links['Body'] != '') {
        foreach(explode(',', $links['Body']) as $kv) {
	    list($k, $v) = explode(' => ', $kv);
	    $linkList[$k] = $v;
        }
    }
    try {
	$body = $client->getObject([
            'Bucket' => getenv('AWS_BUCKET'),
	    'Key' => 'projects/' . $_GET['projName'] . '/body.pdf'
	]);
        $bodyUrl = $client->getObjectUrl(
            getenv('AWS_BUCKET'),
	    'projects/' . $_GET['projName'] . '/body.pdf',
	    '5 minutes'
    	);
    } catch (S3Exception $e) {

    } catch (AwsException $e) {

    }
    try {
	$video = $client->getObject([
            'Bucket' => getenv('AWS_BUCKET'),
	    'Key' => 'projects/' . $_GET['projName'] . '/video.mp4'
	]);
        $videoUrl = $client->getObjectUrl(
            getenv('AWS_BUCKET'),
	    'projects/' . $_GET['projName'] . '/video.mp4',
	    '5 minutes'
        );
    } catch (S3Exception $e) {

    } catch (AwsException $e) {

    }
    try {
	$slides = $client->getObject([
            'Bucket' => getenv('AWS_BUCKET'),
	    'Key' => 'projects/' . $_GET['projName'] . '/slides.pptx'
	]);
        $slidesUrl = $client->getObjectUrl(
            getenv('AWS_BUCKET'),
            'projects/' . $_GET['projName'] . '/slides.pptx',
	    '5 minutes'
        );
    } catch (S3Exception $e) {

    } catch (AwsException $e) {

    }
?>

<div class="container">
    <div class="sidebar">
        <p class="title"><?php echo $title['Body']; ?></p>
        <p>Links and Downloads:</p>
        <?php
            foreach ($linkList as $key => $value) {
                ?>
                <a href="<?php echo $value; ?>" class="link"><?php echo $key; ?></a>
                <?php
            }
        ?>
        <?php if($bodyUrl != '') { ?>
	    <a href="<?php echo $bodyUrl; ?>" class="link">Paper</a>
        <?php } ?>
        <?php if($videoUrl != '') { ?>
	    <a href="<?php echo $videoUrl; ?>" class="link">Video</a>
        <?php } ?>
        <?php if($slidesUrl != '') { ?>
	    <a href="<?php echo $slidesUrl; ?>" class="link">Slides</a>
        <?php } ?>
    </div>
    <div class="body">
	<?php if($bodyUrl != '') { ?>
	    <embed src="<?php echo $bodyUrl; ?>" width="100%" height="1150px" />
	<?php } ?>
        <?php if($videoUrl != '') { ?>
            <video width="100%" controls style="padding: 20px;">
	        <source src="<?php echo $videoUrl; ?>" type="video/mp4">
                Your browser doesn't support the video tag. :(
            </video>
        <?php } ?>
    </div>
</div>
@stop
