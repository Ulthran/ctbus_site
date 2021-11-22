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

$bifImgUrl = $client->getObjectUrl(getenv('AWS_BUCKET'), 'MechanicalBifurcationDiagram.PNG', '5 minutes');
?>

<style>
.container {
    background-image: url(<?php echo $bifImgUrl; ?>);
    background-blend-mode: lighten;
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
.image-container {
    position: relative;
    text-align: center;
}
.image {
    border: 5px outset silver;
}
.image:hover {
    filter: brightness(85%);
    filter: brightness(100%);
}
.caption {
    position: absolute;
    bottom: 20px;
    right: 20px;
    background-color: black;
    color: white;
    padding-left: 20px;
    padding-right: 20px;
    font-weight: bold;
}
.caption:hover {
    visibility: visible;
}
</style>
<div class"container">
    <div class="content-container">
        <div class="image-container">
            <img src="<?php echo $bifImgUrl; ?>" align="right" style="margin: 0px 0px 0px 10px;" class="image"/>
            <div class="caption"></div>
	</div>
        <p class="content">Hi there! My name is Charlie Bushman, I graduated June of 2021 from Carleton College with a major in physics and 5+ years of interning and project experience in software engineering. At Carleton, I was a two-year captain of CHOP (frisbee team, 3x DIII national champs) and two-year director of the Queens of Comedy standup group. I completed my thesis project on <a href="https://charliebushman.com/project?projName=comps" target="_blank" rel="noopener noreferrer" class="link">physical reservoir computing</a> (what I generated this cool plot for), and I was a finalist in the Carleton startup competition for a <a href="https://charliebushman.com/project?projName=latenite" target="_blank" rel="noopener noreferrer" class="link">React Native party planning app</a>.<br/ ><br />Since graduating, I have been working with Rachel Hodes (a fellow '21 Carleton alum) to bring this party planning app to life. We have incorporated under the name Nocturnal and have been designing, developing, and pitching the idea, planning for a beta launch in January 2022. The development work, up through November, has been managed by me (with Rachel taking on the design and marketing side of things) with plans to bring on additional developers in December. More recently, I have also been working for the University of Pennsylvania Department of Microbiology, migrating an existing bioinformatics pipeline into the cloud (AWS) to improve performance and cost.<br /><br />On this website, you can find a number of links relevant to me including GitHub and LinkedIn as well as my re&#769;sume&#769;. Under the projects tab, you'll find a lot of the work I have done ranging from math to physics to software and covering all the ground in between. If you have questions about any of them or anything further you'd like to know about me, you can reach me at <a href="mailto:ctbushman@gmail.com" class="link">ctbushman@gmail.com</a>. I look forward to your questions or comments!</p>
    </div>
    <div class="sidebar">
        <p style="padding: 20px; font-weight: bold; font-size: 20px;">Important Links</p>
        <a href="https://github.com/Ulthran" target="_blank" rel="noopener noreferrer" class="link">GitHub</a><br />
        <a href="https://www.linkedin.com/in/charlie-bushman-8b0b59128/" target="_blank" rel="noopener noreferrer" class="link">LinkedIn</a><br />
        <a href="https://www.carleton.edu/sport-clubs/team-pages/gop-gods-of-plastic/" target="_blank" rel="noopener noreferrer" class="link">Carleton House of Pancakes (CHOP, frisbee team)</a><br />
        <a href="https://www.carleton.edu/student/orgs/queens-of-comedy/" target="_blank" rel="noopener noreferrer" class="link">Queens of Comedy (standup club)</a><br />
        <a href="https://github.com/Ulthran/ctbus_site" target="_blank" rel="noopener noreferrer" class="link">Repo for this site</a><br />
    </div>
</div>
@stop
