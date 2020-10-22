// IMAGE MODALS //

// Get the modal //
var modal = document.getElementById("imageModal");

// Get the img and insert it inside the modal //
var img = document.getElementById("image");
var modalImg = document.getElementById("modalImage");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
}

// get the <span> element that closes the modal //
var span = document.getElementsByClassName("close")[0];

// when the user clicks on <span> (x), close the modal //
span.onclick = function(){
  modal.style.display = "none";
}
