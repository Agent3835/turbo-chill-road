# CHILLRoad - MAPAS PARA LO INCIERTO

![Estado](https://img.shields.io/badge/Estado-Prototipo-f59e0b?style=for-the-badge)
![Stack](https://img.shields.io/badge/Stack-Flask%20|%20Leaflet%20|%20Tailwind-blue?style=for-the-badge)

**No dejes tu seguridad al azar. Navegación de precisión optimizada para entornos seguros.**

### [Enlace a la app en vivo](https://agent3835.pythonanywhere.com/)


---

## Instalación local

Para poner en marcha el panel de control táctico localmente, sigue estos comandos en tu terminal:

**En Windows:**
```bash
python -m venv venv
cd venv
Scripts\activate
```

**En Linux/Mac:**
```bash
python -m venv venv
cd venv
source bin/activate
```

1. **Instalar dependencias: Este proyecto utiliza Flask como motor de backend.**
```bash
pip install flask
```

2. **Clonar el repositorio:**
```bash
git clone https://github.com/Agent3835/turbo-chill-road.git
cd turbo-chill-road
```

3. **Correr el proyecto:**
```bash
python main.py
```
Justificación de Diseño
<p align="justify"> Las aplicaciones de mapas suelen utilizarse en movimiento; por ello, al usar acentos ámbar sobre un fondo oscuro, reducimos la interferencia de elementos visuales y priorizamos lo que realmente importa. </p> <p align="justify"> Los controles de <strong>zoom</strong> los ubicamos abajo a la derecha, pensando en que la interfaz pueda ser utilizada con una sola mano en la versión móvil. </p> <p align="justify"> En cuanto a la <strong>Landing Page</strong>, usamos un gran botón ámbar debajo del eslogan para atraer la atención inmediata del usuario. </p>
Créditos a la IA
<p align="justify"> Este código fue co-creado con Gemini Canvas. </p> <p align="justify"> <strong>Prompt principal:</strong><br> "Crea una Landing Page HTML (ChillRoad). Debe tener un hero con una imagen de fondo de un mapa topográfico oscuro, dependiendo del color de contraste. Un título grande y llamativo, con un botón CTA prominente que diga 'Explorar Mapa'. Usa Tailwind CSS. Me interesa que el diseño utilice colores oscuros de fondo, de preferencia negros azulados con toques brillantes de colores que contrasten, como el ámbar intenso, para generar seguridad. El diseño debe inspirar aventura y seguridad." </p> <p align="justify"> <strong>Segundo prompt:</strong><br> "Genera un archivo HTML que incluya la librería Leaflet.js (vía CDN) y Tailwind CSS. Crea un contenedor div 'map' que ocupe el 100% del ancho y 500px de alto (o 'h-screen'). Inicializa el mapa centrado en [Tijuana], con un tilelayer de OpenStreetMap. Asegúrate de que los botones de zoom estén en una posición fácil de alcanzar." </p> <p align="justify"> <strong>Tercer prompt:</strong><br> "Escribe un script en JS para Leaflet. Cuando el usuario haga clic en el mapa: 1. Coloca un marcador temporal inmediatamente, con posibilidad de personalizar el nombre del marcador. 2. Abre un popup que pregunte: '¿Guardar este punto?'. 3. Al confirmar, envía las coordenadas (lat, long) a un endpoint Flask /guardar_punto usando fetch. Muestra un 'toast' o notificación de 'Guardando...' mientras se procesa." El tooltip del punto debe tener la posibilidad de descartar el punto generado. </p> <p align="justify"> <strong>Cuarto prompt:</strong><br> "Modifica la interfaz para tener dos columnas (o pestañas en móvil): 'Mapa' y 'Lista de Lugares'. Cuando se agregue un marcador en el mapa, debe aparecer también como un texto descriptivo en la sección de lista (ej.: 'Punto en Lat: X, Long: Y'). Asegúrate de que los botones del mapa tengan atributos 'aria-label', como 'Acercar mapa' o 'Alejar mapa'". Los elementos que se vayan creando en la columna lateral que almacena los puntos también deben poder eliminarse, al igual que los puntos creados, mediante un ícono de descartar. </p>
Unificación
<p align="justify"> Los prompts se realizaron por separado al inicio, pero posteriormente se unificaron para construir la aplicación que se presenta en este archivo .md. </p>
