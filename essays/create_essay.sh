#!/bin/zsh
touch /Users/tanishqkumar/Dropbox/backup/Desktop/projects/personal-site/essays/"$2".html

cat > /Users/tanishqkumar/Dropbox/backup/Desktop/projects/personal-site/essays/"$2".html << EOF

<html>
<head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-153791322-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'UA-153791322-1');
  </script>
    <!-- endof Global site tag (gtag.js) - Google Analytics -->



<style>
.accordion {
  background-color: #000;
  color: #fff;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: 1px solid white;
  /* border-top: 0.1px solid black; */
  text-align: left;
  outline: none;
  font-size: 15px;
  transition: 0.4s;
}

.active, .accordion:hover {
  background-color: #000; 
}

/* panel css and js at bottom */

li.sick {
  color: rgb(38, 150, 255);
}

li.audited {
  color: rgb(52,168,83);
}

</style>


  <link rel="stylesheet" href="/static/style.css">
  <meta charset="utf-8">
  <title>$1· Tanishq Kumar</title>
</head>
<body>
<div id="menu">
<span class="title">Tanishq Kumar</span>
<ul>
  <li><a href="/index.html">Home</a></li>
  <li><a href="/about.html">About</a></li>
  <!-- <li><a href="/culture">Culture</a></li> -->
  <li><a href="/books.html">Bookshelf</a></li>
  <li><a href="/essays.html">Essays</a></li>
    <!-- <li><a href="/notes.html">Notes</a></li> -->
    <!-- <li><a href="/articles.html">Articles</a></li> -->
      <li><a href="/courses.html">Coursework</a>
        <!-- <li><a href="/papers.html">Papers</a> -->
</ul>
</div>
<div id="left"></div>
<div id="content">

<h3>$1</h3>

<p>
Write here!

</p>

</div>

EOF