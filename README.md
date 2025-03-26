# Urban Routes Automation Testing

Este proyecto automatiza la prueba de la aplicación **Urban Routes** utilizando Selenium y Pytest. Las pruebas verifican el proceso completo de solicitud de un taxi, desde ingresar la dirección hasta confirmar el pedido.

---

## 📚 Descripción del Proyecto

El objetivo del proyecto es automatizar el flujo de solicitud de taxi en **Urban Routes**, cubriendo las siguientes funcionalidades:

- Establecer la dirección de recogida y destino.
- Seleccionar la tarifa **Comfort**.
- Ingresar el número de teléfono para verificación.
- Agregar método de pago mediante tarjeta de crédito.
- Escribir un mensaje para el conductor.
- Solicitar artículos adicionales como mantas y pañuelos.
- Pedir 2 helados adicionales.
- Esperar la asignación del conductor en la interfaz modal.

---

## 🛠️ Tecnologías y Herramientas Utilizadas

- **Python 3.11**: Lenguaje principal para la automatización.
- **Selenium 4.x**: Automatización de la interfaz web.
- **Pytest**: Marco de pruebas para ejecutar casos de prueba.
- **WebDriver**: Para interactuar con el navegador Chrome.

---

## 📂 Estructura del Proyecto

## 🚀 Instrucciones para Ejecutar las Pruebas

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu-repositorio/urban_routes_project.git
cd urban_routes_project
pip install -r requirements.txt
selenium
pytest

pytest test_urban_routes.py

✅ Funcionalidades Probadas
 Establecer la dirección de origen y destino.

 Solicitar un taxi con la tarifa Comfort.

 Ingresar el número de teléfono y confirmar con SMS.

 Agregar tarjeta de crédito y confirmar pago.

 Añadir mensajes y artículos adicionales.

 Esperar la asignación del conductor.


