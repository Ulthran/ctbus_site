@extends('layouts.app')

@section('content')
<style>
.project-listing {
    display: flex;
    border-radius: 20px;
    border: 1px solid #000;
    padding: 20px;
    margin: 20px;
    transition: all .2s ease-in-out;
}
.project-listing:hover {
    transform: scale(1.01);
}
.thumbnail {
    margin-right: 30px;
    width: 25%;
}
.title {
   font-size: 25px;
   font-weight: bold;
   padding-bottom: 20px;
}
.description {
   font-size: 20px;
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

    function displayProject($projName, $client, $title) {
        // Pull objects from S3
        $description = $client->getObject([
            'Bucket' => getenv('AWS_BUCKET'),
            'Key' => 'projects/' . $projName . '/description.txt'
    	]);
    	$tags = $client->getObject([
    	    'Bucket' => getenv('AWS_BUCKET'),
    	    'Key' => 'projects/' . $projName . '/tags.txt'
    	]);
            $thumbnailCmd = $client->getCommand('GetObject', [
                'Bucket' => getenv('AWS_BUCKET'),
                'Key' => 'projects/' . $projName . '/thumbnail.png'
    	]);
    	$thumbnailReq = $client->createPresignedRequest($thumbnailCmd, '+10 minutes');
    	$thumbnailUrl = (string) $thumbnailReq->getUri();
        // Display project listing
?>
	<a href="http://charliebushman.com/project?projName=<?php echo $projName; ?>">
	<!--<a href="<?php echo "http://" . $_SERVER['SERVER_NAME'] . "project?projName=" . $projName; ?>">-->
        <div class="project-listing">
            <div class="thumbnail">
    		<img src=<?php echo $thumbnailUrl; ?> alt="Uh oh ..." style="border-radius: 20px;">
    	    </div>
    	    <div style="width: 70%">
    		<div class="title">
    		<p><?php echo $title; ?></p>
    		</div>
                    <div class="description">
                        <p><?php echo $description['Body']; ?></p>
                    </div>
                    <div class="description">
    		    <br /><p>Tags: <?php echo $tags['Body']; ?></p>
                    </div>
    	    </div>
    	</div>
    	</a>
<?php
    }
?>

<div id="container">
    <?php displayProject("comps", $client, "COMPS: Physical reservoir computing for classification of temporal data"); ?>
    <?php displayProject("latenite", $client, "LateNite"); ?>
    <?php displayProject("schmidtDecomp", $client, "Schmidt decomposition in quantum information theory"); ?>
    <?php displayProject("fractalsAndChaos", $client, "Fractals and Chaos: Fractal dimension as a measure of complexity"); ?>
    <?php displayProject("fireWalls", $client, "防火墙观念和技术: Firewall theory and technology (Harbin, China)"); ?>
    <?php displayProject("qkd", $client, "Twin-fields quantum key distribution"); ?>
    <?php displayProject("earthMag", $client, "Measuring the Earth's magnetic field in the undergraduate laboratory"); ?>
    <?php displayProject("trebuchet", $client, "Optimizing a trebuchet for range"); ?>
</div>
@stop
