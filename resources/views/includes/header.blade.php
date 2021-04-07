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
?>

<style>
.navbar-inner {
    border-bottom: 1px solid #000;
    border-radius: 50px;
    display: flex;
    justify-content: space-between;
    padding-right: 10%;
    padding-left: 10%;
}

.navbar-item {
    font-size: large;
    display: flex;
    justify-content: space-between;
    padding-bottom: 10px;
}
</style>

<div class="navbar">
   <div class="navbar-inner">
       <div class="navbar-item"><a href="/projects">Projects</a></div>
       <div class="navbar-item"><a href="/">Home</a></div>
       <div class="navbar-item"><a href="/resume">Resume&#769;</a></div>
   </div>
</div>
