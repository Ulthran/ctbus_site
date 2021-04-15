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
.image {
    border: 5px outset silver;
}
.caption {
    font-weight: bold;
}
</style>
<div class"container">
    <div class="content-container">
        <img src="<?php echo $bifImgUrl; ?>" align="right" style="margin: 0px 0px 0px 10px;" class="image"/>
        <p class="content">Hi there! My name is Charlie Bushman, I'm graduating this June from Carleton College (Class of 2021) with a major in physics and 5+ years of interning and project experience in software engineering. At Carleton, I'm a two-year captain of the Gods of Plastic frisbee team (3x DIII national champs) and two-year director of the Queens of Comedy standup group, I completed my thesis project (we call it COMPS) on <a href="https://charliebushman.com/project?projName=comps" class="link">physical reservoir computing</a>, and I was a finalist in the Carleton startup competition for a React Native party planning app.<br/ ><br />In the summers since high school, I have spent my time in software engineering internships. I worked for HepatoChem, a small chem-tech startup, for two summers and a winter to develop a user friendly database. No one at the company had experience beyond the Excel sheets they were using so I was working independently with the president, Marc, to learn on the job and come up with a solution that fit their needs. From there, I spent two summers at Owl Labs where I developed a unit testing framework for their Android code base using GTest and then created an internal website for the marketing team, becoming much more familiar with AWS in the process. And finally I went to HPE where I jumped into the newly formed Gelato team to work on the stories that had to get done before launch later that year. My main interests now lie in the intersections between computation, physics, and big data where, I would argue, the most exciting advancements are happening in all three.<br /><br />On this website, you can find a number of links relevant to me including GitHub and LinkedIn as well as my re&#769;sume&#769;. Under the projects tab, you'll find a lot of the work I have done ranging from math to physics to software and covering all the ground in between. If you have questions about any of them or anything further you'd like to know about me, you can reach me at <a href="mailto:ctbushman@gmail.com" class="link">ctbushman@gmail.com</a>. I look forward to your questions, comments, or other!</p>
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
