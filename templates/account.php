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

if($_SERVER['REQUEST_METHOD']=='POST'){
    $name=$_POST['name'];
    $email=$_POST['email'];
    $university = $_POST['university'];
    $password=$_POST['password'];

$hashed_password = password_hash($password, PASSWORD_DEFAULT);
$sql = "INSERT INTO users(name,email,university,password,hashed_password) VALUES('$name','$email','$university','$password','$hashed_password')";

if ($conn->query($sql)) {
    // Redirect to a login page or dashboard
    header("Location: http://127.0.0.1:5000/");
    exit;
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
    header("Location: http://127.0.0.1:5000/register");
}

}
$conn->close();
?>



