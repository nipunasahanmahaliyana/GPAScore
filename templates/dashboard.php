
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GPA Score</title>
    <link rel="stylesheet" href="http://localhost:3000/templates/dashboard.css">
</head>
<body>
    
    <div class="sidebar">
            <div class="logo">
                <img src="http://localhost:3000/templates/image/img1.png" alt="Logo" class="logo">
                <span class="brand">GPASCORE</span>
            </div>
            <nav>
                <ul>
                    <li class="active"><a href="http://127.0.0.1:5000/home/dashboard/">Dashboard</a><li>
                    <li><a href="http://127.0.0.1:5000/home/dashboard/factors">Statistics</a></li>
                    <li><a href="http://127.0.0.1:5000/home/dashboard/features">Features</a></li>
                    <li><a href="http://127.0.0.1:5000/home/dashboard/logout">Logout</a></li>
                </ul>
            </nav>
            <div class="bottom-links">
                <a href="http://localhost:3000/templates/form.html">Survey</a>
                <?php include 'http://localhost:3000/templates/user.php'; ?>
                <a href="#"></a>
            </div>
    </div>
        <main class="main-content">
            <header class="header">
                <div class="user-info">
                    <img src="http://localhost:3000/templates/image/img5.png" alt="student">
                 
                </div>
                 <div class="search-bar">
                    <img src="https://img.icons8.com/ios-filled/50/000000/search.png" width="20" height="20"/>
                    <input type="text" placeholder="Search here...">
                   
                </div>
               
             </header>
            <h1>Dashboard</h1>
            <section class="dashboard">
                <div class="card green">
                    <h2>Let's make a try</h2>
                    <p>We will ask some questions and by answering<br> those questions, we can predict the GPA<br> performance.</p>
                    <a href="http://127.0.0.1:5000/home/dashboard/predict"><button class="predict-button">Predict</button></a>
                </div>
                <div class="card yellow">
                    <h2>Statistics</h2>
                    <a href="http://127.0.0.1:5000/home/dashboard/factors"><button class="arrow-button">➜</button></a>
                    <p>Get a statistical review of how these features affect GPA performance.</p>
                    
                </div>
                <div class="card blue">
                    <h2>Features</h2>
                    <p>To predict a student's GPA performance, we require about 11 factors from the user.</p>
                    <a href="http://127.0.0.1:5000/home/dashboard/features"><button class="arrow-button">➜</button></a>
                </div>
                <div class="card white">
                    <h2>Join with us</h2>
                    <p>Join our surveys and help us improve the prediction.</p>
                    <a href="http://localhost:3000/templates/form.html"><button class="arrow-button">➜</button></a>
                </div>
                <div class="active-users">
             
                </div>
            </section>
    </main> 
    
    
   
</body>
</html>