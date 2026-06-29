(function () {
  let current = 0;
  const slides = document.querySelectorAll('.slide');
  const counter = document.querySelector('.slide-counter');
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const progressBar = document.getElementById('progressBar');

  function show(n) {
    slides.forEach(s => s.classList.remove('active'));
    slides[n].classList.add('active');
    counter.textContent = (n + 1) + ' / ' + slides.length;
    prevBtn.disabled = n === 0;
    nextBtn.disabled = n === slides.length - 1;
    if (progressBar) {
      progressBar.style.width = ((n + 1) / slides.length * 100) + '%';
    }
    current = n;
  }

  prevBtn.addEventListener('click', function () { if (current > 0) show(current - 1); });
  nextBtn.addEventListener('click', function () { if (current < slides.length - 1) show(current + 1); });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') nextBtn.click();
    if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')   prevBtn.click();
  });

  // Touch swipe
  let tx = 0;
  document.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; });
  document.addEventListener('touchend', function (e) {
    const dx = e.changedTouches[0].clientX - tx;
    if (Math.abs(dx) > 50) { if (dx < 0) nextBtn.click(); else prevBtn.click(); }
  });

  show(0);
})();
