
<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Replace with your own database credentials
    $servername = "localhost";
    $username = "root";
    $password_db = "";
    $dbname = "gpa_predictor";

    // Create connection
    $conn = new mysqli($servername, $username, $password_db, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $email = $_POST['email'];
    $password = $_POST['password'];
    

    $sql = "SELECT id FROM users WHERE email='$email' AND password='$password'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $user = $result->fetch_assoc();
        $_SESSION['user_id'] = $user['id'];
        header("Location: http://127.0.0.1:5000/home/dashboard");
        exit;
    } else {
        $error = "Invalid email or password";
        header("Location: http://127.0.0.1:5000/login");
       
        exit;
        
    }

}
$data=$_SESSION['user_id'];

$conn->close();

?>


