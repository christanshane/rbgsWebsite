from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = """
    <!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Home - Recoletos de Bacolod Graduate School - UNO-RECOLETOS</title>

    <!-- Bootstrap core CSS -->
    <link href="layout1/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>

    <link href="https://cdn.jsdelivr.net/npm/startbootstrap-heroic-features@4.0.0-beta/css/heroic-features.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="layout1/css/heroic-features.css" rel="stylesheet">

  </head>

  <body>

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <a class="navbar-brand" href="#">RBGS.org</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <a class="nav-link" href="/home"> Home
                <span class="sr-only"></span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/programs">Programs</a>
            </li>			
            <li class="nav-item">
              <a class="nav-link" href="/researches">Researches</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/outreach">Outreach</a>
            </li>			
            <li class="nav-item">
              <a class="nav-link" href="/contactus">Contact Us</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/news">News</a>
            </li>			
          </ul>
        </div>
      </div>
    </nav>

    <!-- Page Content -->
    <div class="container">

      <!-- Jumbotron Header -->
	  	  <center>
      <header class="myJumbotron my-4">

<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
  </ol>
  <div class="carousel-inner" role="listbox">
    <div class="carousel-item active">
      <img class="d-block img-fluid" src="layout1/images/1.jpg" alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="d-block img-fluid" src="layout1/images/2.jpg" alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block img-fluid" src="layout1/images/3.png" alt="Third slide">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>

</div>
      </header>
  </center>
	  
      <!-- Page Features -->
      <div class="row text-center">


        <div class="col-lg-4 col-md-6 mb-4">
          <div class="card">
            <img class="card-img-top" src="http://placehold.it/500x325" alt="">
            <div class="card-body">
              <h4 class="card-title">Programs</h4>
              <p class="card-text">View the list of all programs offered by the Graduate School.</p>
            </div>
            <div class="card-footer">
              <a href="#" class="btn btn-primary">View Programs</a>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 mb-4">
          <div class="card">
            <img class="card-img-top" src="http://placehold.it/500x325" alt="">
            <div class="card-body">
              <h4 class="card-title">Researches</h4>
              <p class="card-text">The repository of all research compilations by the students.</p>
            </div>
            <div class="card-footer">
              <a href="#" class="btn btn-primary">Find Out More</a>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 mb-4">
          <div class="card">
            <img class="card-img-top" src="http://placehold.it/500x325" alt="">
            <div class="card-body">
              <h4 class="card-title">Outreach</h4>
              <p class="card-text">Reaching out to all sectors of the society, no matter what status.</p>
            </div>
            <div class="card-footer">
              <a href="#" class="btn btn-primary">See events</a>
            </div>
          </div>
        </div>

      </div>
      <!-- /.row -->
    </div>
	<span style = "font-family: arial; color: white;">
	<div style = "width: 100%; background: #191970;"> 
			<div class = "container"> 
				<div class = "row"> 
					<div class = "col-lg-5">
					</div>
					<div class = "col-lg-7">
					<br>
					<h1> <b> OUR MISSION </b> </h1>
					Recoletos de Bacolod Graduate School commits to provide excellent education that integrates Gospel values in various professions, offers opportunities for collaborative and independent researches through local, national and international linkages and produce value laden managers and leaders, educators, researchers, medical & other health related professions, social and behavioral practioners.   
					<br> <br>
					<h1> <b> OUR GOALS </b> </h1>
					Recoletos de Bacolod Graduate School provides relevant, responsible and stimulating curricula/programs for clientele to synergize theories, principles and practices to meet the challenges of a dynamic and changing society and 
					delivers higher education services in a manner that is efficient, coordinated and accessible. 
					</span>
					<br> <br>
					</div>
				</div>
			</div>
    </div>
		<div style = "background: #101055; width: 100%;"> 		
			<div class = "container">
				<div class = "row"> 
					<div class = "col-lg-12"> <center> <br>
					
					<h1> <b> THE UNIVERSITY </b> </h1>	
					Be in the know how did the university came into being.
					<br> <br>
						<a href="#" class="btn btn-primary">Learn More</a>
					<br> <br>
					</center>
					</div>
				</div>
			</div>
	     </div>
		<div style = "background: #050525; width: 100%;"> 		
			<div class = "container">
				<div class = "row"> 
					<div class = "col-lg-12"> <center> <br>
					
					<h1> <b> ADMISSION REQUIREMENTS </b> </h1>	
					How to apply for the Graduate School.
					<br> <br>
						<a href="#" class="btn btn-primary">Learn More</a>
					<br> <br>
					</center>
					</div>
				</div>
			</div>
	     </div>		 
	</span>
	</div>
    <!-- /.container -->

    <!-- Footer -->
    <footer class="py-5 bg-dark">
      <div class="container">
        <p class="m-0 text-center text-white">Copyright &copy; UNO-RECOLETOS 2017</p>
      </div>
      <!-- /.container -->
    </footer>

    <!-- Bootstrap core JavaScript -->
    <script src="layout1/vendor/jquery/jquery.min.js"></script>
    <script src="layout1/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  </body>

</html>

    """
    return HttpResponse(html)