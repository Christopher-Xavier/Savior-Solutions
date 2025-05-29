document.addEventListener("scroll", function() {
  document.querySelectorAll(".fade-in").forEach(element => {
    if (element.getBoundingClientRect().top < window.innerHeight) {
      element.style.opacity = "1";
      element.style.transform = "translateY(0)";
    }
  });
});