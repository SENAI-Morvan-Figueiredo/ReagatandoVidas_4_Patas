(function() {
  const toggle = document.getElementById('userToggle');
  const dropdown = document.getElementById('userDropdown');

  if (!toggle || !dropdown) return;

  // Define função que abre/fecha e atualiza atributos ARIA
  function setOpen(open) {
    if (open) {
      dropdown.classList.add('open');
      toggle.setAttribute('aria-expanded', 'true');
      dropdown.setAttribute('aria-hidden', 'false');
    } else {
      dropdown.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      dropdown.setAttribute('aria-hidden', 'true');
    }
  }

  // Toggle com proteção contra múltiplos cliques rápidos
  let animating = false;
  function toggleDropdown(e) {
    e.preventDefault();
    e.stopPropagation();

    if (animating) return;
    animating = true;

    const willOpen = !dropdown.classList.contains('open');
    setOpen(willOpen);

    // pequeno timeout para evitar cliques muito rápidos (sincroniza com transition CSS)
    setTimeout(() => { animating = false; }, 220);
  }

  // Abrir/fechar via teclado (Enter / Space)
  function onToggleKey(e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      toggleDropdown(e);
    } else if (e.key === 'Escape') {
      setOpen(false);
    }
  }

  // Fecha ao clicar fora
  function onDocumentClick(ev) {
    // se clicou no toggle, ignora (já tratado)
    if (toggle.contains(ev.target)) return;
    // se clicou dentro do dropdown, ignora
    if (dropdown.contains(ev.target)) return;
    setOpen(false);
  }

  // Fecha ao redimensionar ou ao mudar foco para outra aba
  function closeOnResizeOrBlur() {
    setOpen(false);
  }

  // Eventos principais
  toggle.addEventListener('click', toggleDropdown);
  toggle.addEventListener('keydown', onToggleKey);

  // Suporte para toque (touchstart) em alguns dispositivos
  document.addEventListener('touchstart', onDocumentClick, { passive: true });
  document.addEventListener('click', onDocumentClick);
  window.addEventListener('resize', closeOnResizeOrBlur);
  window.addEventListener('blur', closeOnResizeOrBlur);

  // Fecha com ESC quando dropdown estiver focado
  dropdown.addEventListener('keydown', (ev) => {
    if (ev.key === 'Escape') setOpen(false);
  });

  // Acessibilidade: permite navegar com TAB dentro do menu e fecha quando perde foco
  dropdown.addEventListener('focusout', (ev) => {
    // se o novo foco estiver fora do dropdown e do toggle, fecha
    const newTarget = ev.relatedTarget;
    if (!dropdown.contains(newTarget) && !toggle.contains(newTarget)) {
      setOpen(false);
    }
  });

})();
