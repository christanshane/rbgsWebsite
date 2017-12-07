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

        <title>Programs | Recoletos de Bacolod Graduate School</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>

        <link href="https://cdn.jsdelivr.net/npm/startbootstrap-heroic-features@4.0.0-beta/css/heroic-features.css" rel="stylesheet">

      </head>
      <body>

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <a class="navbar-brand" href="#">RBGS</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
                <li class="nav-item">
              <a class="nav-link" href="/home">Home</a>
            </li>
			<li class="nav-item">
              <a class="nav-link" href="news.html"> News
              </a>
            </li>
            <li class="nav-item active">
              <a class="nav-link" href="programs.html">Programs</a>
            </li>			
            <li class="nav-item">
              <a class="nav-link" href="researches.html">Researches</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="outreach.html">Outreach</a>
            </li>			
            <li class="nav-item">
              <a class="nav-link" href="contactus.html">Contact Us</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Page Content -->
    <div class="container">

      <!-- Jumbotron Header -->
      <header class="jumbotron my-4">
        <h1 class="display-3">Recoletos de Bacolod Graduate School Programmes</h1>
        <p class="lead">Educational Programs provided by the Recoletos de Bacolod Graduate School</p>
      </header>

	  
      <!-- Page Features -->
      <div class="row text-center">

        <div class="col-lg-3 col-md-6 mb-4">                                        <!--Card-->
          <div class="card">
            <img class="card-img-top" src="http://placehold.it/500x325" alt="">
            <div class="card-body">
              <h4 class="card-title">Program 1</h4>
              <p class="card-text">Lorem Ipsum Dolor Sit Amet Consequitor</p>
            </div>
            <div class="card-footer">
              <a href="#" class="btn btn-primary">See Full Detail</a>
            </div>
          </div>
        </div>
        
        <div class="col-lg-3 col-md-6 mb-4">                                        <!--Card-->
          <div class="card">
            <img class="card-img-top" src="http://placehold.it/500x325" alt="">
            <div class="card-body">
              <h4 class="card-title">Program 2</h4>
              <p class="card-text">Lorem Ipsum Dolor Sit Amet Consequitor</p>
            </div>
            <div class="card-footer">
              <a href="#" class="btn btn-primary">See Full Detail</a>
            </div>
          </div>
        </div>
        
        <div class="col-lg-3 col-md-6 mb-4">                                        <!--Card-->
          <div class="card">
            <img class="card-img-top" src="http://placehold.it/500x325" alt="">
            <div class="card-body">
              <h4 class="card-title">Program 3</h4>
              <p class="card-text">Lorem Ipsum Dolor Sit Amet Consequitor</p>
            </div>
            <div class="card-footer">
              <a href="#" class="btn btn-primary">See Full Detail</a>
            </div>
          </div>
        </div>
        
        <div class="col-lg-3 col-md-6 mb-4">                                        <!--Card-->
          <div class="card">
            <img class="card-img-top" src="http://placehold.it/500x325" alt="">
            <div class="card-body">
              <h4 class="card-title">Program 4</h4>
              <p class="card-text">Lorem Ipsum Dolor Sit Amet Consequitor</p>
            </div>
            <div class="card-footer">
              <a href="#" class="btn btn-primary">See Full Detail</a>
            </div>
          </div>
        </div>
      </div>
      
      <div class="row text-center">

        <div class="col-lg-3 col-md-6 mb-4">                                        <!--Card-->
          <div class="card">
            <img class="card-img-top" src="http://placehold.it/500x325" alt="">
            <div class="card-body">
              <h4 class="card-title">Program 5</h4>
              <p class="card-text">Lorem Ipsum Dolor Sit Amet Consequitor</p>
            </div>
            <div class="card-footer">
              <a href="#" class="btn btn-primary">See Full Detail</a>
            </div>
          </div>
        </div>
        
        <div class="col-lg-3 col-md-6 mb-4">                                        <!--Card-->
          <div class="card">
            <img class="card-img-top" src="http://placehold.it/500x325" alt="">
            <div class="card-body">
              <h4 class="card-title">Program 6</h4>
              <p class="card-text">Lorem Ipsum Dolor Sit Amet Consequitor</p>
            </div>
            <div class="card-footer">
              <a href="#" class="btn btn-primary">See Full Detail</a>
            </div>
          </div>
        </div>
        
        <div class="col-lg-3 col-md-6 mb-4">                                        <!--Card-->
          <div class="card">
            <img class="card-img-top" src="http://placehold.it/500x325" alt="">
            <div class="card-body">
              <h4 class="card-title">Program 7</h4>
              <p class="card-text">Lorem Ipsum Dolor Sit Amet Consequitor</p>
            </div>
            <div class="card-footer">
              <a href="#" class="btn btn-primary">See Full Detail</a>
            </div>
          </div>
        </div>
        
        <div class="col-lg-3 col-md-6 mb-4">                                        <!--Card-->
          <div class="card">
            <img class="card-img-top" src="http://placehold.it/500x325" alt="">
            <div class="card-body">
              <h4 class="card-title">Program 8</h4>
              <p class="card-text">Lorem Ipsum Dolor Sit Amet Consequitor</p>
            </div>
            <div class="card-footer">
              <a href="#" class="btn btn-primary">See Full Detail</a>
            </div>
          </div>
        </div>
        
      </div>

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
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  </body>
  </html>
    """
    return HttpResponse(html)