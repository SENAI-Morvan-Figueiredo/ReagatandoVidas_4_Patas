(function() {
  const toggle = document.getElementById('userToggle');
  const dropdown = document.getElementById('userDropdown');

  if (!toggle || !dropdown) return;

  function toggleDropdown(e) {
    e.stopPropagation();
    dropdown.classList.toggle('open');
  }

  toggle.addEventListener('click', toggleDropdown);

  // Fecha ao clicar fora
  document.addEventListener('click', (ev) => {
    if (!dropdown.contains(ev.target) && ev.target !== toggle) {
      dropdown.classList.remove('open');
    }
  });

  // Fecha com ESC
  document.addEventListener('keydown', (ev) => {
    if (ev.key === 'Escape') {
      dropdown.classList.remove('open');
    }
  });

  // Fecha ao redimensionar
  window.addEventListener('resize', () => {
    dropdown.classList.remove('open');
  });
})();
