# Bin2Dec - Convertidor de Binario a Decimal

Aplicación interactiva para convertir números binarios a decimales (Bin2Dec Tier 1), resolviendo la necesidad de calcular y comprender conversiones numéricas de forma rápida mediante una interfaz sencilla.

---

## 📝 Descripción
Aplicación que permite convertir números del sistema binario a decimal de forma instantánea. El sistema valida en tiempo real que el usuario únicamente ingrese dígitos válidos (0s y 1s) notificando de inmediato cualquier error, facilitando así la conversión precisa de hasta 8 dígitos.

---

## 🎯 User Stories
- Como usuario, quiero ingresar una cadena de hasta 8 dígitos binarios (0s y 1s) en un campo de texto para su conversión.
- Como usuario, quiero ser notificado si ingreso un carácter distinto de 0 o 1, para corregir el error inmediatamente.
- Como usuario, quiero ver el resultado decimal equivalente mostrado en pantalla al presionar un botón de conversión.

---

## ⚙️ Metodología
**Ágil (Kanban)** — Seleccionamos esta metodología utilizando un tablero visual debido a la naturaleza incremental de las funciones del proyecto (validación, algoritmo e interfaz). Nos permite dividir las user stories en tareas cortas y visualizar el avance del equipo en tiempo real.

---

## 👥 Integrantes del equipo
- **Andrés Molina Espinoza** — [@am4525300-star](https://github.com/am4525300-star)
- **Kevin Peña Ontiveros** — @usuario_github_2
- **Cristofer Herrera** — @usuario_github_3

---

## 🛠️ Requisitos del Sistema
* **Lenguaje:** Python 3.8 o superior
* **Librerías externas:** Ninguna (módulos estándar)
* **Compatibilidad:** Windows, macOS, Linux

---

## 🚀 Instalación y Ejecución

Clonar el Repositorio
Abre la terminal (CMD o PowerShell en Windows, o la Terminal en Mac/Linux) y ejecuta el siguiente comando para descargar una copia de tu repositorio:
1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/am4525300-star/bin2dec-equipo_tal.git](https://github.com/am4525300-star/bin2dec-equipo_tal.git)

Entrar a la carpeta del proyecto
Una vez que se complete la descarga, entra a la carpeta del proyecto usando el comando cd: cd bin2dec-equipo-tal

Verificar la instalación de Python
Asegúrate de tener Python instalado en tu sistema. Puedes comprobar la versión ejecutando: 
En Windows:   python --version
En Mac / Linux:  python3 --version

Ejecutar el Programa
Ejecuta el archivo principal main.py escribiendo:
En Windows: python main.py
En Mac / Linux:  python3 main.py

Probar la Aplicación
Una vez iniciada la aplicación:

Introduce un número binario cuando la consola o la interfaz lo solicite (por ejemplo: 1010 o 11111111).

Presiona Enter (o el botón de convertir) para ver la conversión a decimal (10 o 255).

Intenta ingresar un valor inválido (como 102 o abc) para probar las alertas de validación de errores.

