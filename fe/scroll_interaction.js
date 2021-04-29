function scrollInteraction() {
  const articles = document.querySelectorAll("article");

  for (const article of articles) {
    //console.log(article);
    itemPosition = article.getBoundingClientRect().top;
    screenPosition = window.innerHeight;
    if (itemPosition + 100 < screenPosition) {
      article.classList.add("appear");
    } else {
      article.classList.remove("appear");
    }
  }
}

window.addEventListener("scroll", scrollInteraction);
