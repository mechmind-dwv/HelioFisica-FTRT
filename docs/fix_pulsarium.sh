#!/bin/bash

# Archivo a corregir
FILE="pulsarium_heliosofico_ultima_version.html"

# 1. CORREGIR ANIMACIÓN DE PLANETAS - agregar movimiento orbital real
sed -i '/function startCosmicAnimation() {/,/animateCosmos();/c\
function startCosmicAnimation() {\n    function animateCosmos() {\n        const speedMultiplier = currentMode === '"'"'resonancia'"'"' ? (bpm / 60) : 1;\n        \n        cosmicRevelation.slice(1).forEach(body => {\n            const element = document.querySelector(`.planet-master[data-name=\"${body.name}\"]`);\n            if (!element) return;\n            \n            sacredAngles[body.name] = (sacredAngles[body.name] + body.speed * speedMultiplier) % 360;\n            \n            const rad = sacredAngles[body.name] * Math.PI / 180;\n            const x = body.distance * Math.cos(rad);\n            const y = body.distance * Math.sin(rad);\n            \n            element.style.transform = `translate(calc(-50% + ${x}px), calc(-50% + ${y}px))`;\n            \n            // Efecto de pulso orgánico para la Tierra en modo resonancia\n            if (body.name === '"'"'TIERRA'"'"' && currentMode === '"'"'resonancia'"'"') {\n                const pulseScale = 1 + heartCoherence * 0.2;\n                element.style.transform += ` scale(${pulseScale})`;\n            }\n        });\n        \n        // Actualizar conexiones si están visibles\n        if (connectionsVisible) {\n            updateQuantumConnections();\n        }\n        \n        cosmicAnimationId = requestAnimationFrame(animateCosmos);\n    }\n    animateCosmos();\n}' $FILE

# 2. CORREGIR SISTEMA DE SONIDO - hacerlo funcional
sed -i '/function playSacredFrequency(frequency, color, planetName) {/,/^    }/c\
function playSacredFrequency(frequency, color, planetName) {\n    if (!quantumAudioContext) {\n        quantumAudioContext = new (window.AudioContext || window.webkitAudioContext)();\n    }\n    \n    // Solo proceder si el contexto está corriendo\n    if (quantumAudioContext.state === '"'"'suspended'"'"') {\n        quantumAudioContext.resume();\n    }\n    \n    try {\n        const oscillator = quantumAudioContext.createOscillator();\n        const gainNode = quantumAudioContext.createGain();\n        \n        // Configuración armónica sagrada\n        oscillator.type = getSacredWaveform(frequency);\n        oscillator.frequency.setValueAtTime(frequency, quantumAudioContext.currentTime);\n        \n        const now = quantumAudioContext.currentTime;\n        gainNode.gain.setValueAtTime(0, now);\n        gainNode.gain.linearRampToValueAtTime(0.3, now + 0.1);\n        gainNode.gain.exponentialRampToValueAtTime(0.001, now + 2);\n        \n        oscillator.connect(gainNode);\n        gainNode.connect(quantumAudioContext.destination);\n        \n        oscillator.start(now);\n        oscillator.stop(now + 2);\n        \n        console.log(`🎵 ${frequency}Hz - ${planetName}`);\n        \n        // Crear ripple visual cuando suena\n        createSoundRipple(color, frequency);\n        \n    } catch (error) {\n        console.log('"'"'🔇 Error de audio:'"'"', error);\n    }\n}' $FILE

# 3. AGREGAR FUNCIÓN DE RIPPLE DE SONIDO
sed -i '/function createHarmonicRipple(element) {/,/^}/a\
\nfunction createSoundRipple(color, frequency) {\n    const ripple = document.createElement('"'"'div'"'"');\n    ripple.style.position = '"'"'fixed'"'"';\n    ripple.style.top = '"'"'50%'"'"';\n    ripple.style.left = '"'"'50%'"'"';\n    ripple.style.transform = '"'"'translate(-50%, -50%)'"'"';\n    ripple.style.width = '"'"'100px'"'"';\n    ripple.style.height = '"'"'100px'"'"';\n    ripple.style.border = `2px solid ${color}`;\n    ripple.style.borderRadius = '"'"'50%'"'"';\n    ripple.style.opacity = '"'"'0.7'"'"';\n    ripple.style.zIndex = '"'"'25'"'"';\n    ripple.style.pointerEvents = '"'"'none'"'"';\n    ripple.style.animation = '"'"'soundRipple 2s ease-out forwards'"'"';\n    \n    document.body.appendChild(ripple);\n    \n    setTimeout(() => {\n        if (ripple.parentNode) {\n            ripple.parentNode.removeChild(ripple);\n        }\n    }, 2000);\n}' $FILE

# 4. AGREGAR ANIMACIÓN CSS PARA RIPPLE DE SONIDO
sed -i '/@keyframes connection-resonance {/,/^}/a\
\n@keyframes soundRipple {\n    0% { \n        transform: translate(-50%, -50%) scale(0.5);\n        opacity: 0.7; \n    }\n    100% { \n        transform: translate(-50%, -50%) scale(3);\n        opacity: 0; \n    }\n}' $FILE

# 5. CORREGIR INICIALIZACIÓN DE ÁNGULOS
sed -i '/const sacredAngles = {};/a\
// Inicializar ángulos aleatorios para movimiento orbital\ncosmicRevelation.slice(1).forEach((body, index) => {\n    sacredAngles[body.name] = Math.random() * 360;\n});' $FILE

# 6. MEJORAR DETECCIÓN DE CLICK EN PLANETAS
sed -i '/celestialBody.addEventListener(/c\
                // Evento de revelación\n                celestialBody.addEventListener('"'"'click'"'"', () => {\n                    playSacredFrequency(body.freq, body.color, body.name);\n                    revealCosmicTruth(body);\n                    createHarmonicRipple(celestialBody);\n                });' $FILE

# 7. AGREGAR BOTÓN DE ACTIVACIÓN DE AUDIO
sed -i '/<button onclick="revealQuantumConnections()"/a\
        <button onclick="activateAudioSystem()" style="flex:1; padding:12px; background:linear-gradient(45deg,#ec4899,#fbbf24); color:white; border:none; border-radius:10px; cursor:pointer; font-weight:bold; margin-top:10px;">\n            🔊 ACTIVAR SONIDO\n        </button>' $FILE

# 8. AGREGAR FUNCIÓN DE ACTIVACIÓN DE AUDIO
sed -i '/function playSolarFrequency() {/,/^}/a\
\nfunction activateAudioSystem() {\n    if (!quantumAudioContext) {\n        quantumAudioContext = new (window.AudioContext || window.webkitAudioContext)();\n    }\n    \n    // En algunos navegadores necesitas una interacción de usuario\n    if (quantumAudioContext.state === '"'"'suspended'"'"') {\n        quantumAudioContext.resume().then(() => {\n            showQuantumMessage('"'"'🔊 SISTEMA DE SONIDO ACTIVADO'"'"');\n            // Tocar frecuencia del Sol para demostrar\n            playSacredFrequency(432, '"'"'#FFD700'"'"', '"'"'SOL'"'"');\n        });\n    } else {\n        showQuantumMessage('"'"'🔊 SISTEMA DE SONIDO LISTO'"'"');\n        playSacredFrequency(432, '"'"'#FFD700'"'"', '"'"'SOL'"'"');\n    }\n}' $FILE

echo "🔧 CORRECIONES APLICADAS AL PULSARIUM"
echo "🎵 Sistema de sonido reparado"
echo "🌌 Animaciones orbitales activadas"
echo "✨ Efectos visuales mejorados"

