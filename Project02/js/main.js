AOS.init({
	duration: 800,
	easing: 'slide',
	once: false
});
function myMove() {
	var pos = 0;
	var elem = document.getElementById("mySubheading");   
	var id = setInterval(frame, 5);
	
	function frame() {
	  if (pos == 150) {
		clearInterval(id);
	  } else {
		pos++; 
		elem.style.position = "absolute";
		elem.style.left = pos + "px"; 
	  }
	}
  }
  

 
 

