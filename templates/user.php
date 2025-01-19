<?php
session_start();
$servername = "localhost";
$username = "root";
$password_db = "";
$dbname = "gpa_predictor";

$conn =new mysqli($servername, $username, $password_db, $dbname);

if($conn->connect_error){
    die("Connection error:".$conn->connect_error);
}
$data =$_SESSION['user_id'];

echo "$data";
?>



