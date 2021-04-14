@extends('layouts.app')

@section('content')
<style>
.container {
}
.content-container {
    display: inline-block;
    padding: 20px;
    width: 80%;
    margin: 20px;
}
.sidebar {
    display: inline-block;
    vertical-align: top;
    padding: 20px;
    width: 15%;
    text-align: center;
}
.content {
    padding: 20px;
    padding-left: 5%;
    font-size: 20px;
}
.link {
    text-decoration: underline;
    padding-top: 10px;
}
.image {
    border: 5px outset silver;
}
.caption {
    font-weight: bold;
}
</style>
<div class"container">
<div class="content-container">
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

	$bifImgUrl = $client->getObjectUrl(getenv('AWS_BUCKET'), 'MechanicalBifurcationDiagram.PNG', '5 minutes');
    ?>

    <img src="<?php echo $bifImgUrl; ?>" align="right" style="margin: 0px 0px 0px 10px;" class="image"/>
    <p class="content">Hi there! My name is Charlie Bushman, I'm graduating this June from Carleton College (Class of 2021) with a major in physics and 5+ years of interning and project experience in software engineering. As you might guess from this, my main interests lie in the intersections between computation, physics, and big data where, I would argue, the most exciting advancements are happening in both fields.<br /><br />In quantum computing, <a href="http://charliebushman.com/project?projName=qkd" class="link">provably secure, optical communications encryption protocols</a> could become widespread means of sensitive information transfer and the promise of quantum supremacy seems very near to fruition, which would enable things like using <a href="http://charliebushman.com/project?projName=comps" class="link">recurrent quantum circuits as computational reservoirs</a> for solving real-world problems. And these computational reservoirs aren't just limited to quantum circuits, they be any suitably complex physical system. This opens up a whole new world for programming and training physical networks to further machine learning capabilities. Add on to this, the capacity that blockchain has to revolutionize everything from finance to IoT, and we could soon see a world where everything we interact with is even smarter and even better connected than anything existing today. These are the kinds of problems I want to work on solving and the kind of vision I want to work towards building.</p>
</div>
<div class="sidebar">
    <p style="padding: 20px; font-weight: bold; font-size: 20px;">Important Links</p>
    <a href="https://github.com/Ulthran" target="_blank" rel="noopener noreferrer" class="link">GitHub</a><br />
    <a href="https://www.linkedin.com/in/charlie-bushman-8b0b59128/" target="_blank" rel="noopener noreferrer" class="link">LinkedIn</a><br />
    <a href="https://www.carleton.edu/sport-clubs/team-pages/gop-gods-of-plastic/" target="_blank" rel="noopener noreferrer" class="link">Gods of Plastic (frisbee team)</a><br />
    <a href="https://www.carleton.edu/student/orgs/queens-of-comedy/" target="_blank" rel="noopener noreferrer" class="link">Queens of Comedy (standup club)</a><br /> 
    <a href="https://github.com/Ulthran/ctbus_site" target="_blank" rel="noopener noreferrer" class="link">Repo for this site</a><br />
</div>
</div>
@stop
