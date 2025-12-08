/* --- Minimal JS Interactions for Magenta Alien Theme 👾 --- */

/* Fade-in reveal on scroll */
document.addEventListener("scroll", () => {
  const reveals = document.querySelectorAll(".reveal");
  const trigger = window.innerHeight * 0.88;

  reveals.forEach((el) => {
    const rect = el.getBoundingClientRect();
    if (rect.top < trigger) {
      el.classList.add("visible");
    }
  });
});

/* Soft link pulse on click */
document.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    link.style.transition = "opacity 0.4s ease";
    link.style.opacity = "0.4";
    setTimeout(() => link.style.opacity = "1", 400);
  });
});

/* Navbar fade-in on load */
window.addEventListener("load", () => {
  const nav = document.querySelector(".tibas-navbar");
  if (nav) {
    nav.style.opacity = 0;
    nav.style.transition = "opacity 1s ease";
    requestAnimationFrame(() => nav.style.opacity = 1);
  }
});
