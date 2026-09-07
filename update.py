import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_blocks = '''
      <div class="proposals-container">

        <!-- BLOQUE 1: LÁSER ESCÉNICO -->
        <article class="proposal-row" id="bloque-1">
          <div class="proposal-visual">
            <img src="img/01-laser.jpg" alt="LÁSER ESCÉNICO" loading="lazy" />
            <div class="proposal-visual-overlay"></div>
          </div>
          <div class="proposal-info">
            <div class="proposal-index-bg">01</div>
            <div class="proposal-tag badge-red">LÁSER & TIME-CODE</div>
            <h2 class="proposal-title">LÁSER ESCÉNICO SINCRONIZADO</h2>
            <p class="proposal-subtitle">DISEÑO Y PROGRAMACIÓN MILIMÉTRICA</p>
            <p class="proposal-description">
              Diseño, programación milimétrica y sincronización de intervenciones de láser de alta potencia integrados con la narrativa musical y el contenido de video.
            </p>
            
            <div class="proposal-specs-grid">
              <div class="spec-col">
                <div class="spec-col-title">DISEÑO & ESTÉTICA</div>
                <ul class="spec-list">
                  <li class="spec-item">Diseño conceptual de momentos de impacto lumínico/láser.</li>
                </ul>
              </div>
              <div class="spec-col">
                <div class="spec-col-title">TÉCNICA</div>
                <ul class="spec-list">
                  <li class="spec-item">Programación y sincronización con código de tiempo (SMPTE / MIDI / OSC).</li>
                  <li class="spec-item">Integración en vivo con el sistema TouchDesigner y visuales.</li>
                </ul>
              </div>
              <div class="spec-col">
                <div class="spec-col-title">OPERATIVA</div>
                <ul class="spec-list">
                  <li class="spec-item">Pruebas de calibración espacial, zonas de seguridad y alineación en venue.</li>
                  <li class="spec-item">Operación técnica dedicada durante el espectáculo.</li>
                </ul>
              </div>
            </div>

            <div class="proposal-footer">
              <div class="proposal-price-box">
                <span class="price-label">FEE ESTIMADO / REFERENCIA</span>
                <span class="price-value">.500</span>
                <span class="price-currency">USD</span>
              </div>
              <div class="proposal-actions">
                <button class="btn-details" onclick="openModal('laserModal')">VER DETALLES →</button>
              </div>
            </div>
          </div>
        </article>

        <!-- BLOQUE 2: VIDEO EN VIVO & CÁMARAS -->
        <article class="proposal-row" id="bloque-2">
          <div class="proposal-visual">
            <img src="img/02-video.jpg" alt="VIDEO EN VIVO" loading="lazy" />
            <div class="proposal-visual-overlay"></div>
          </div>
          <div class="proposal-info">
            <div class="proposal-index-bg">02</div>
            <div class="proposal-tag badge-cyan">REALTIME SHADERS</div>
            <h2 class="proposal-title">VIDEO EN VIVO & CANVAS DE CÁMARAS</h2>
            <p class="proposal-subtitle">SISTEMA DE CAPTURA Y PROCESAMIENTO</p>
            <p class="proposal-description">
              Sistema de captura y procesamiento en tiempo real de las señales de cámara del venue, convirtiéndolas en una pieza viva y reactiva del lenguaje escénico.
            </p>
            
            <div class="proposal-specs-grid">
              <div class="spec-col">
                <div class="spec-col-title cyan">DISEÑO & ESTÉTICA</div>
                <ul class="spec-list cyan">
                  <li class="spec-item">Generación de mezclas híbridas (cámaras en vivo + visuales generativos).</li>
                </ul>
              </div>
              <div class="spec-col">
                <div class="spec-col-title cyan">TÉCNICA</div>
                <ul class="spec-list cyan">
                  <li class="spec-item">Recepción de señales de cámara mediante capturadoras profesionales SDI/NDI.</li>
                  <li class="spec-item">Filtrado, post-procesamiento y efectos reactivos por shaders (TouchDesigner).</li>
                </ul>
              </div>
              <div class="spec-col">
                <div class="spec-col-title cyan">OPERATIVA</div>
                <ul class="spec-list cyan">
                  <li class="spec-item">Composición y ruteo a los distintos canvas y pantallas del estadio.</li>
                  <li class="spec-item">Operación y control de switch de capas en tiempo real durante el show.</li>
                </ul>
              </div>
            </div>

            <div class="proposal-footer">
              <div class="proposal-price-box">
                <span class="price-label">FEE ESTIMADO / REFERENCIA</span>
                <span class="price-value">.800</span>
                <span class="price-currency">USD</span>
              </div>
              <div class="proposal-actions">
                <button class="btn-details" onclick="openModal('camerasModal')">VER DETALLES →</button>
              </div>
            </div>
          </div>
        </article>

        <!-- BLOQUE 3: DESARROLLO DE VISUALES -->
        <article class="proposal-row" id="bloque-3">
          <div class="proposal-visual">
            <img src="img/03-visuales.jpg" alt="DESARROLLO DE VISUALES" loading="lazy" />
            <div class="proposal-visual-overlay"></div>
          </div>
          <div class="proposal-info">
            <div class="proposal-index-bg">03</div>
            <div class="proposal-tag badge-red">CONTENIDOS // 15 DÍAS</div>
            <h2 class="proposal-title">GENERACIÓN DE CONTENIDO VISUAL</h2>
            <p class="proposal-subtitle">SISTEMA MODULAR ADAPTATIVO</p>
            <p class="proposal-description">
              Desarrollo de piezas visuales a medida para acompañar la progresión del show de ~30 temas, con criterio de reutilización, adaptación y combinación dinámica.
            </p>
            
            <div class="proposal-specs-grid">
              <div class="spec-col">
                <div class="spec-col-title">DISEÑO & ESTÉTICA</div>
                <ul class="spec-list">
                  <li class="spec-item">15 días de diseño, animación 2D/3D y producción de piezas clave.</li>
                  <li class="spec-item">Sistema modular de loops adaptativos según la intensidad del tema.</li>
                </ul>
              </div>
              <div class="spec-col">
                <div class="spec-col-title">TÉCNICA</div>
                <ul class="spec-list">
                  <li class="spec-item">Masterización en las resoluciones nativas del canvas LED del estadio.</li>
                </ul>
              </div>
              <div class="spec-col">
                <div class="spec-col-title">OPERATIVA</div>
                <ul class="spec-list">
                  <li class="spec-item">Co-diseño y reuniones con la dirección creativa del show.</li>
                  <li class="spec-item">Incluye hasta 2 rondas de correcciones y ajustes antes de ensayos.</li>
                </ul>
              </div>
            </div>

            <div class="proposal-footer">
              <div class="proposal-price-box">
                <span class="price-label">VALOR PRELIMINAR DEFINIDO</span>
                <span class="price-value" style="color: var(--accent-red);">.000</span>
                <span class="price-currency" style="color: var(--accent-red);">USD</span>
              </div>
              <div class="proposal-actions">
                <button class="btn-details" onclick="openModal('visualsModal')">VER DETALLES →</button>
              </div>
            </div>
          </div>
        </article>

        <!-- BLOQUE 4: DIRECCIÓN TÉCNICA, SERVIDORES & OPERACIÓN -->
        <article class="proposal-row" id="bloque-4">
          <div class="proposal-visual">
            <img src="img/04-infra.jpg" alt="INFRAESTRUCTURA" loading="lazy" />
            <div class="proposal-visual-overlay"></div>
          </div>
          <div class="proposal-info">
            <div class="proposal-index-bg">04</div>
            <div class="proposal-tag badge-cyan">INFRAESTRUCTURA // HOST</div>
            <h2 class="proposal-title">SERVIDORES, RED & OPERACIÓN EN VIVO</h2>
            <p class="proposal-subtitle">PROCESAMIENTO MASIVO EN GPU</p>
            <p class="proposal-description">
              Infraestructura de hardware de grado broadcast con procesamiento masivo en GPU, estación redundante de respaldo y operación técnica durante el show.
            </p>
            
            <div class="proposal-specs-grid">
              <div class="spec-col">
                <div class="spec-col-title cyan">DISEÑO & ESTÉTICA</div>
                <ul class="spec-list cyan">
                  <li class="spec-item">Pruebas & Ensayos: 1 a 2 semanas de testing en estudio y calibración.</li>
                </ul>
              </div>
              <div class="spec-col">
                <div class="spec-col-title cyan">TÉCNICA</div>
                <ul class="spec-list cyan">
                  <li class="spec-item">Servidor Principal: GPU NVIDIA RTX A6000 + Captura 8K Multicanal ( USD).</li>
                  <li class="spec-item">Segundo Servidor: Backup redundante y procesamiento de cámaras en tiempo real.</li>
                  <li class="spec-item">Red de Alta Velocidad: Switches dedicados 10GbE / baja latencia.</li>
                </ul>
              </div>
              <div class="spec-col">
                <div class="spec-col-title cyan">OPERATIVA</div>
                <ul class="spec-list cyan">
                  <li class="spec-item">Operación en Vivo: Técnicos y operadores en el evento (.200 USD).</li>
                </ul>
              </div>
            </div>

            <div class="proposal-footer">
              <div class="proposal-price-box">
                <span class="price-label">HARDWARE + OPERACIÓN</span>
                <span class="price-value">.600</span>
                <span class="price-currency">USD</span>
              </div>
              <div class="proposal-actions">
                <button class="btn-details" onclick="openModal('infraModal')">VER DETALLES →</button>
              </div>
            </div>
          </div>
        </article>

        <!-- BLOQUE 5: EXPERIMENTAL / BETA QR INTERACTIVO -->
        <article class="proposal-row" id="bloque-5">
          <div class="proposal-visual">
            <img src="img/05-beta.jpg" alt="MÓDULO EXPERIMENTAL" loading="lazy" />
            <div class="proposal-visual-overlay"></div>
          </div>
          <div class="proposal-info">
            <div class="proposal-index-bg">05</div>
            <div class="proposal-tag badge-amber">MÓDULO EXPERIMENTAL // BETA</div>
            <h2 class="proposal-title">PLATAFORMA INTERACTIVA PÚBLICO (QR)</h2>
            <p class="proposal-subtitle">EXPERIENCIA WEB PROPIETARIA</p>
            <p class="proposal-description">
              Desarrollo de una experiencia web propietaria accesible mediante código QR proyectado en las pantallas. El público participa desde su smartphone en vivo.
            </p>
            
            <div class="proposal-specs-grid">
              <div class="spec-col">
                <div class="spec-col-title amber">DISEÑO & ESTÉTICA</div>
                <ul class="spec-list amber">
                  <li class="spec-item">Captura / subida de fotografías instantáneas desde el celular del público.</li>
                  <li class="spec-item">Integración en pantallas del estadio como banners, mosaicos o canvas interactivos.</li>
                </ul>
              </div>
              <div class="spec-col">
                <div class="spec-col-title amber">TÉCNICA</div>
                <ul class="spec-list amber">
                  <li class="spec-item">Recepción e ingesta en servidor local de producción en tiempo real.</li>
                  <li class="spec-item">Sistema de cupos y cola inteligente para gestionar alta concurrencia de usuarios.</li>
                </ul>
              </div>
              <div class="spec-col">
                <div class="spec-col-title amber">OPERATIVA</div>
                <ul class="spec-list amber">
                  <li class="spec-item">Requisito Crítico: Requiere red WiFi dedicada o canal 5GHz provisto en el estadio.</li>
                  <li class="spec-item">Fase Beta: Requiere pruebas previas de estrés y validación de infraestructura.</li>
                </ul>
              </div>
            </div>

            <div class="proposal-footer">
              <div class="proposal-price-box">
                <span class="price-label">DESARROLLO WEB + SERVER LOCAL (PRELIMINAR)</span>
                <span class="price-value" style="color: var(--accent-amber);">.800</span>
                <span class="price-currency" style="color: var(--accent-amber);">USD</span>
              </div>
              <div class="proposal-actions">
                <button class="btn-details" onclick="openModal('qrModal')">VER ARQUITECTURA TÉCNICA BETA</button>
              </div>
            </div>
          </div>
        </article>

      </div>
'''

new_content = re.sub(r'<div class="blocks-grid">.*?</section>\s*<!-- Section 2: Cotizador Interactivo & Presupuesto -->', new_blocks + '\n    </div>\n  </section>\n\n  <!-- Section 2: Cotizador Interactivo & Presupuesto -->', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
