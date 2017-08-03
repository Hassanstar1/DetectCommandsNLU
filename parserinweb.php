<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">

        <title>the initial stage of our parser</title>
    </head>

    <body>
        <nav class="navbar navbar-inverse">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="#">Maverick Parser</a>
            </div>
          </div>
        </nav>

        <div class="container">

           
                <div class="row">
                    
                </div>
            
            <div class="row">
                <form action="parserinweb.php" method="POST">
                    <textarea class="form-control" name="contents" placeholder="please, Write your command here"></textarea>
                    <input type="submit" name="submit" value="Parse the command">
                </form>
            </div>

        </div>

<?php
// This is the data you want to pass to Python
if(isset($_POST['submit'])){
$text=$_POST['contents'];
//$content = explode("\n", str_replace("\r", " ", $text));
$content = trim(preg_replace('/\s+/', ' ', $text));
//echo $content;

//print_r($_GET)
}
//$data = "send an sms to dad at 9 am  repeat everyday  say it loudly content take your medication";
$data = $content;

// Execute the python script with the JSON data
$result = shell_exec('python parserinweb.py ' . escapeshellarg(json_encode($data)));
//$result = shell_exec('python test.py ' . escapeshellarg($data));
echo "<pre>$result</pre>";
//print_r(explode(']',$result,-1));
// Decode the result
//$resultData = json_decode($result, true);

// This will contain: array('status' => 'Yes!')
//var_dump($resultData);
//$command = escapeshellcmd('test.py');
//$output = shell_exec($command);
//echo '\n hello';


?>








</body>
</html>
