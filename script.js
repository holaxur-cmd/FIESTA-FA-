// ===================================================
// DISTORXION STUDIO — MOVISTAR ARENA (FIESTA FA!)
// Lógica Interactiva, Cotizador y Exportador PDF
// ===================================================

document.addEventListener('DOMContentLoaded', () => {
  // === 1. Loader (Mismo comportamiento y efecto que en Festival Konex) ===
  const loader = document.getElementById('loader');
  const progress = document.getElementById('loaderProgress');
  const navEl = document.getElementById('nav');
  let p = 0;

  const loaderInterval = setInterval(() => {
    p += Math.random() * 25;
    if (p >= 100) {
      p = 100;
      clearInterval(loaderInterval);
      setTimeout(() => {
        if (loader) loader.classList.add('hidden');
        if (navEl) {
          navEl.classList.add('visible');
          navEl.style.transform = 'translateY(0)';
        }
      }, 400);
    }
    if (progress) progress.style.width = p + '%';
  }, 100);

  // === 2. Custom Cursor Animation ===
  const cursor = document.getElementById('cursor');
  const follower = document.getElementById('cursorFollower');
  let mouseX = 0, mouseY = 0, curX = 0, curY = 0, folX = 0, folY = 0;

  document.addEventListener('mousemove', e => {
    mouseX = e.clientX;
    mouseY = e.clientY;
  });

  function animateCursor() {
    curX += (mouseX - curX) * 0.25;
    curY += (mouseY - curY) * 0.25;
    if (cursor) cursor.style.transform = `translate3d(${curX}px, ${curY}px, 0)`;

    folX += (mouseX - folX) * 0.08;
    folY += (mouseY - folY) * 0.08;
    if (follower) follower.style.transform = `translate3d(${folX}px, ${folY}px, 0)`;

    requestAnimationFrame(animateCursor);
  }
  animateCursor();

  document.querySelectorAll('a, button, input, .block-card, .preset-pill, .nav-social-link').forEach(el => {
    el.addEventListener('mouseenter', () => {
      if (cursor) cursor.classList.add('hover');
      if (follower) follower.classList.add('hover');
    });
    el.addEventListener('mouseleave', () => {
      if (cursor) cursor.classList.remove('hover');
      if (follower) follower.classList.remove('hover');
    });
  });

  // === 3. Dataset de Items / Bloques del Presupuesto ===
  const budgetItems = [
    {
      id: 'laser',
      name: 'Láser Escénico Sincronizado',
      sub: 'Sincronización láser y video 2 minutos (intro de show o separador durante el show)',
      category: 'Láser Escénico',
      usd: 2500,
      active: true
    },
    {
      id: 'liveOps',
      name: 'Diseño y Operación en Vivo',
      sub: 'Armado técnico, utilización durante el show y operado en vivo por personal técnico especializado en FoH',
      category: 'Operación en Vivo',
      usd: 1200,
      active: true
    },
    {
      id: 'cameras',
      name: 'Video en Vivo & Canvas de Cámaras',
      sub: 'Filtrado en tiempo real con shaders (TouchDesigner) y ruteo',
      category: 'Realtime & Cámaras',
      usd: 900,
      active: true
    },
    {
      id: 'visuals',
      name: 'Generación de Contenido Visual',
      sub: '15 días de diseño y animación para ~30 temas del repertorio',
      category: 'Arte & Dirección',
      usd: 2500,
      active: true
    },
    {
      id: 'servers',
      name: 'Servidores, Red & Infraestructura',
      sub: '2 servidores (principal + backup), placa PCI x4, 4 salidas 4K, red 10GbE',
      category: 'Infraestructura',
      usd: 800,
      active: true
    },
    {
      id: 'qrBeta',
      name: 'Plataforma Interactiva para Público (Web QR)',
      sub: 'Recopilación de fotos desde el ingreso, integración en cenefas y pantallas (Beta)',
      category: 'Experimental (Beta)',
      usd: 5200,
      active: false
    }
  ];

  window.budgetItems = budgetItems;

  // === 4. Render Cotizador Table ===
  function renderCotizador() {
    const tbody = document.getElementById('cotizadorTableBody');
    if (!tbody) return;

    tbody.innerHTML = '';

    budgetItems.forEach((item) => {
      const tr = document.createElement('tr');

      tr.innerHTML = `
        <td>
          <input type="checkbox" class="custom-checkbox" id="check_${item.id}" ${item.active ? 'checked' : ''} onchange="toggleItem('${item.id}')">
        </td>
        <td>
          <label for="check_${item.id}" style="cursor: pointer;">
            <span class="table-item-name ${item.id === 'qrBeta' ? 'accent-amber' : ''}">${item.name}</span>
            <span class="table-item-sub">${item.sub}</span>
          </label>
        </td>
        <td><span class="block-badge ${item.id === 'qrBeta' ? 'badge-amber' : item.category.includes('Láser') ? 'badge-red' : 'badge-cyan'}">${item.category}</span></td>
        <td class="table-price text-right">$ ${item.usd.toLocaleString('es-AR')} USD</td>
      `;
      tbody.appendChild(tr);
    });

    updateTotals();
  }

  window.toggleItem = function(id) {
    const found = budgetItems.find(i => i.id === id);
    if (found) {
      found.active = !found.active;
      updateTotals();
    }
  };

  window.updateTotals = function() {
    let totalUsd = 0;
    let activeCount = 0;

    budgetItems.forEach(item => {
      if (item.active) {
        totalUsd += item.usd;
        activeCount++;
      }
    });

    // Update main display
    const totalUsdEl = document.getElementById('totalUsdDisplay');
    const summaryCountEl = document.getElementById('selectedBlocksSummary');

    if (totalUsdEl) totalUsdEl.textContent = `$ ${totalUsd.toLocaleString('es-AR')} USD`;
    if (summaryCountEl) summaryCountEl.textContent = `${activeCount} de ${budgetItems.length} conceptos seleccionados`;

    // Sync checkbox states
    budgetItems.forEach(item => {
      const checkbox = document.getElementById(`check_${item.id}`);
      if (checkbox) checkbox.checked = item.active;
    });
  };

  window.applyPreset = function(type) {
    document.querySelectorAll('.preset-pill').forEach(pill => pill.classList.remove('active'));
    if (event && event.target) event.target.classList.add('active');

    if (type === 'base') {
      budgetItems.forEach(i => {
        i.active = ['visuals', 'liveOps', 'servers'].includes(i.id);
      });
    } else if (type === 'full') {
      budgetItems.forEach(i => {
        i.active = ['laser', 'liveOps', 'cameras', 'visuals', 'servers'].includes(i.id);
      });
    } else if (type === 'interactive') {
      budgetItems.forEach(i => {
        i.active = true;
      });
    }

    renderCotizador();
  };

  // Initial render
  renderCotizador();

  // === 5. Modal Handlers ===
  window.openModal = function(id) {
    const modal = document.getElementById(id);
    if (modal) {
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  };

  window.closeModal = function(id) {
    const modal = document.getElementById(id);
    if (modal) {
      modal.classList.remove('open');
      document.body.style.overflow = '';
    }
  };

  // Close modals on backdrop click or ESC key
  document.querySelectorAll('.modal-backdrop').forEach(backdrop => {
    backdrop.addEventListener('click', (e) => {
      if (e.target === backdrop) {
        backdrop.classList.remove('open');
        document.body.style.overflow = '';
      }
    });
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-backdrop.open').forEach(m => {
        m.classList.remove('open');
      });
      document.body.style.overflow = '';
    }
  });

  // === 6. PDF Export Generation via html2pdf.js ===
  const btnExport = document.getElementById('btnOpenExport');
  if (btnExport) {
    btnExport.addEventListener('click', () => {
      exportProposalPdf();
    });
  }

  function exportProposalPdf() {
    const container = document.getElementById('pdfExportContainer');
    const table = document.getElementById('pdfSummaryTable');
    const pdfTotalUsd = document.getElementById('pdfTotalUsd');

    let totalUsd = 0;
    let html = `
      <tr style="background: #222; color: #ff1a1a; font-weight: bold; border-bottom: 2px solid #ff1a1a;">
        <th style="padding: 8px; text-align: left;">CONCEPTO</th>
        <th style="padding: 8px; text-align: left;">CATEGORÍA</th>
        <th style="padding: 8px; text-align: right;">VALOR USD</th>
      </tr>
    `;

    budgetItems.filter(i => i.active).forEach(item => {
      totalUsd += item.usd;
      html += `
        <tr style="border-bottom: 1px solid #333;">
          <td style="padding: 8px; color: #fff;"><strong>${item.name}</strong><br/><span style="color: #888; font-size: 10px;">${item.sub}</span></td>
          <td style="padding: 8px; color: #00f0ff;">${item.category}</td>
          <td style="padding: 8px; text-align: right; color: #fff; font-weight: bold;">$ ${item.usd.toLocaleString('es-AR')} USD</td>
        </tr>
      `;
    });

    table.innerHTML = html;
    pdfTotalUsd.textContent = `$ ${totalUsd.toLocaleString('es-AR')} USD`;

    container.style.display = 'block';

    const opt = {
      margin:       10,
      filename:     'Distorxion_Propuesta_Presupuesto_Movistar_Arena_FA.pdf',
      image:        { type: 'jpeg', quality: 0.98 },
      html2canvas:  { scale: 2, useCORS: true, backgroundColor: '#0d0d12' },
      jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
    };

    const originalText = btnExport.innerHTML;
    btnExport.innerHTML = 'GENERANDO PDF...';

    html2pdf().set(opt).from(container).save().then(() => {
      container.style.display = 'none';
      btnExport.innerHTML = originalText;
    }).catch(err => {
      console.error('Error generating PDF:', err);
      container.style.display = 'none';
      btnExport.innerHTML = originalText;
      window.print();
    });
  }

  // === 7. Active Navigation Highlighting on Scroll ===
  const sections = document.querySelectorAll('section[id], header');
  const navLinks = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {
    let current = '';
    const scrollPos = window.scrollY + 100;

    sections.forEach(section => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      if (scrollPos >= top && scrollPos < top + height) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (current && link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });
});
