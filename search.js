function search() {
  links = document.getElementsByTagName("a");
  for (var i = 0; i != links.length; i++) {
    if (links[i].innerHTML.contains("Search")) {
        links[i].click();
        console.info("Searching..."); 
    }
   
  }

var loopTime = 5000;
setInterval(search, loopTime);