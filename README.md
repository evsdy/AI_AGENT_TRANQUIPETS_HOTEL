# 🐾🏨 Tranquipets - AI Agent

¡Bienvenido al repositorio oficial del **AI Agent de Tranquipets**! Esta es una aplicación web interactiva diseñada para actuar como el asistente virtual premium del hotel de mascotas. Utiliza Inteligencia Artificial avanzada y técnicas de **RAG (Generación Aumentada por Recuperación)** para responder con total precisión a las consultas de los clientes basándose estrictamente en las políticas internas, tarifas, reglamentos y preguntas frecuentes del hotel.

---

## 📄 Descripción General del Proyecto

El objetivo principal de esta aplicación es automatizar y elevar la calidad de la atención al cliente de **Tranquipets**. Los usuarios e integrantes del equipo pueden interactuar con un chat inteligente que no "alucina" ni inventa datos, ya que sus respuestas están limitadas por el contexto extraído de los documentos oficiales del hotel. 

Además, la aplicación cuenta con una barra lateral dinámica que permite la carga de nuevos documentos PDF en tiempo real para expandir el conocimiento del agente de manera inmediata.

---

## 🏗️ Arquitectura de la Solución Implementada

La solución se construyó bajo el patrón de arquitectura **RAG (Retrieval-Augmented Generation)** simplificado, estructurado de la siguiente manera:

1. **Carga e Ingesta:** Al arrancar la aplicación, los archivos PDF base (`faq_preguntas-frecuentes.pdf` y `politicas_hotel_tranquipets.pdf`) son procesados secuencialmente a través de un lector de documentos de **LangChain** (`PyPDFLoader`).
2. **Unificación de Contexto:** El texto extraído de las páginas se estructura e identifica con su fuente original, consolidándose en una base de conocimiento unificada en memoria.
3. **Inyección de Prompt de Sistema:** Cuando el usuario envía una pregunta a través de la interfaz de **Streamlit**, el texto de la consulta se encapsula junto a directrices estrictas de comportamiento (System Prompt) y la base de conocimiento previamente unificada.
4. **Generación de Respuesta:** La estructura completa se envía a la API de **Cohere** utilizando el modelo avanzado `command-r-plus-08-2024`, el cual analiza el contexto y genera una respuesta empática, profesional y concisa.

---

## 🛠️ Tecnologías y Herramientas Utilizadas

El proyecto utiliza un stack tecnológico moderno y eficiente optimizado para entornos Cloud:

* ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) **Streamlit:** Framework utilizado para construir la interfaz gráfica web y el flujo del chat interactivo.
* ![Cohere](https://img.shields.io/badge/Cohere-335FFF?style=for-the-badge&logo=cohere&logoColor=white) **Cohere API (ClientV2):** Motor de Inteligencia Artificial que procesa el lenguaje natural mediante el modelo `command-r-plus-08-2024`.
* ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white) **LangChain Community:** Módulo `PyPDFLoader` utilizado para la extracción limpia de texto e ingesta de metadatos desde archivos PDF.
* ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) **Python 3.10+:** Lenguaje base del ecosistema del proyecto.
* ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) **GitHub & Streamlit Cloud:** Herramientas para el control de versiones y despliegue continuo (CI/CD) de la aplicación web.

---

## 🚀 Instrucciones para Ejecutar el Proyecto

### Prerrequisitos
* Tener instalado Python 3.10 o superior en tu máquina local.
* Una cuenta en Cohere para obtener una API Key válida.

### 1. Clonar el repositorio
```bash
git clone https://github.com/evsdy/AI_AGENT_TRANQUIPETS_HOTEL.git 
cd ai_agent_tranquipets_hotel 
```

## 💻 Configurar el Entorno Virtual
# En Mac / Linux
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate

## 📀 Instalar Dependencias
pip install -r requirements.txt

## 🖱️ Configurar Variables de Entorno Locales
Crea una carpeta llamada .streamlit en la raíz del proyecto y dentro de ella un archivo secrets.toml:
COHERE_API_KEY = "tu_api_key_secreta_aquí"

## ▶️ Ejecutar la Aplicación
streamlit run streamlit_app.py
La aplicación se abrirá automáticamente en tu navegador web local en la dirección http://localhost:8501.

---

# 💬 Ejemplos de Interacción con el Agente

## ❓ Ejemplos de preguntas que el agente puede responder:


¿Cuáles son los horarios de check-in y check-out para el hotel de mascotas?

¿Qué requisitos médicos o vacunas solicitan antes de recibir a un perrito?

¿Cuáles son las tarifas vigentes por noche para habitaciones VIP?

¿Qué protocolo siguen si mi mascota requiere administración de medicamentos?

## ❕ Ejemplos de respuestas generadas por el agente:


1. ¿Cuáles son los horarios de check-in y check-out para el hotel de mascotas?

Los horarios de ingreso (check-in) son de lunes a sábado de 8:00 AM a 11:00 AM. Es importante destacar que no se reciben mascotas por la tarde para garantizar un tiempo de adaptación antes de la noche.

En cuanto a las salidas (check-out), estas se realizan de lunes a domingo de 9:00 AM a 12:00 PM. Si se realiza una salida tardía, se aplicará un cargo adicional.

2. ¿Qué requisitos médicos o vacunas solicitan antes de recibir a un perrito?

Para garantizar la salud y seguridad de todos los huéspedes, Tranqui Pets requiere que los perros cumplan con ciertos requisitos médicos antes de su ingreso:

Vacunas: Es obligatorio que el perro tenga la cartilla de vacunación al día y que se le hayan aplicado las vacunas de la Rabia, la Séxtuple y la Bordetella (tos de las perreras) al menos 15 días antes de su llegada al hotel.

Desparasitación: El canino debe haber sido desparasitado interna y externamente en los últimos 30 días, ya sea con pipeta o pastilla para pulgas y garrapatas.

Evaluación de temperamento: Los perros que visitan Tranqui Pets por primera vez deben pasar una prueba de socialización de 15 minutos para asegurarse de que no muestren conductas agresivas hacia otros perros o humanos.

Recuerda que es importante cumplir con estos requisitos para poder ingresar a tu mascota al hotel. Si tienes alguna duda sobre la cartilla de vacunación o los requisitos, no dudes en consultar con tu veterinario o ponerte en contacto con nosotros.

3. ¿Cuáles son las tarifas vigentes por noche para habitaciones VIP?  

Lamento informarte que no encuentro información sobre las tarifas vigentes para habitaciones VIP en los manuales actuales del hotel Tranqui Pets. Si deseas conocer los precios y las opciones disponibles, te recomiendo contactar directamente al hotel para obtener los detalles más recientes. Estarán encantados de brindarte toda la información que necesites.

4. ¿Qué protocolo siguen si mi mascota requiere administración de medicamentos?

El personal de Tranqui Pets puede administrar medicamentos a su mascota por vía oral o tópica sin costo adicional. Para ello, es necesario que usted, como dueño, proporcione la receta médica firmada y las instrucciones claras por escrito sobre el horario y la dosis de la medicación. Es importante destacar que no se aplican medicamentos inyectables.

Recuerde que es su responsabilidad entregar la medicación y la información necesaria para que el personal pueda administrarla adecuadamente durante la estadía de su mascota en el hotel.

## 📸 Vista Previa de la Interfaz
A continuación puedes ver cómo luce el panel de control y el flujo de conversación de Tranquipets:

1. Panel Principal y Documentación
Aquí se gestionan las preguntas y políticas del hotel desde la barra lateral.

<img width="1470" height="834" alt="Captura de pantalla 2026-07-20 a la(s) 2 58 17 p  m" src="https://github.com/user-attachments/assets/97901213-2366-47da-ba56-f3c896b2283d" />


2. Flujo de Chat con el Agente
Demostración de una consulta en tiempo real utilizando una paleta fria y minimalista.


<img width="1168" height="786" alt="thumbnail" src="https://github.com/user-attachments/assets/9b934230-6abf-47f9-9567-098098be18c9" />

## 📎 Link: 
https://tranquipets-hotel.streamlit.app/
