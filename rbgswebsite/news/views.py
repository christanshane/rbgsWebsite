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
    
        <title>News - Recoletos de Bacolod Graduate School - UNO-RECOLETOS</title>
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
                  <a class="nav-link" href="/home">Home
                  </a>
                </li>
                <li class="nav-item active">
                  <a class="nav-link" href="/news">News</a>
                </li>
                <li class="nav-item">
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
        <br />
          <div class="row">
            <div class="col-lg-8 col-md-10 pull-left">
              <div class="panel">
                    <div class="panel-heading">
                        <div class="text-center">
                            <div class="row">
                                <div class="col-sm-9">
                                    <h2 class="pull-left left">Post With image</h2>
                                </div>
                                <div class="col-sm-3">
                                    <h4 class="pull-right">
                                    <small><em>2014-07-30 18:30:00</em></small>
                                    </h4>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                <div class="panel-body">
                    <a href="#" class="thumbnail">
                        <img alt="Image" src="http://i.imgur.com/tAHVmXi.jpg">
                    </a>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
                    quis nostrud exercitation... <a href="#">Read more</a>
                </div>
                
                <div class="panel-footer">
                    <span class="label label-default">Image</span> <span class="label label-default">Updates</span> <span class="label label-default">July</span>
                </div>
            </div>
              <hr>
              <div class="post-preview">
                <a href="post.html">
                  <h2 class="post-title">
                    I believe every human has a finite number of heartbeats. I don't intend to waste any of mine.
                  </h2>
                </a>
                <p class="post-meta">Posted by
                  <a href="#">Start Bootstrap</a>
                  on September 18, 2017</p>
              </div>
              <hr>
              <div class="post-preview">
                <a href="post.html">
                  <h2 class="post-title">
                    Science has not yet mastered prophecy
                  </h2>
                  <h3 class="post-subtitle">
                    We predict too much for the next year and yet far too little for the next ten.
                  </h3>
                </a>
                <p class="post-meta">Posted by
                  <a href="#">Start Bootstrap</a>
                  on August 24, 2017</p>
              </div>
              <hr>
              <div class="post-preview">
                <a href="post.html">
                  <h2 class="post-title">
                    Failure is not an option
                  </h2>
                  <h3 class="post-subtitle">
                    Many say exploration is part of our destiny, but it’s actually our duty to future generations.
                  </h3>
                </a>
                <p class="post-meta">Posted by
                  <a href="#">Start Bootstrap</a>
                  on July 8, 2017</p>
              </div>
              <hr>
              <!-- Pager -->
              <div class="clearfix">
                <a class="btn btn-primary float-right" href="#">Older Posts &rarr;</a>
              </div>
              <br>
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
        <script src="vend   or/bootstrap/js/bootstrap.bundle.min.js"></script>
    
      </body>
    
    </html>
    """
    return HttpResponse(html)