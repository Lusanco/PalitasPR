<script>
  import { onMount } from 'svelte';

  let currentDate;

  onMount(() => {
    const today = new Date();
    currentDate = today.toLocaleDateString();
  });
</script>

<div class="container p-8 mx-auto my-4 bg-white rounded-lg shadow-lg">
  <h1 class="mb-4 text-4xl font-bold text-center text-black">Política de Privacidad</h1>
  <p class="mb-8 text-center text-gray-500">Fecha de entrada en vigor: {currentDate}</p>

  <div class="p-4 mb-6 bg-gray-100 rounded-md shadow-md">
    <p>PalitasPR ("nosotros", "nuestro" o "la aplicación") opera como un mercado local para solicitar y promocionar servicios en Puerto Rico. Esta política de privacidad describe cómo recopilamos, usamos y protegemos la información personal de nuestros usuarios. Esta política aplica a todos los usuarios de nuestra aplicación.</p>
  </div>

  <div>
    <h2 class="mb-4 text-2xl font-semibold text-black">1. Información que Recopilamos</h2>
    <p class="mb-6 text-gray-700">Recopilamos los siguientes tipos de información personal de los usuarios:</p>
    <ul class="mt-2 list-disc list-inside">
      <li>Nombre</li>
      <li>Correo electrónico</li>
      <li>Dirección</li>
      <li>Número de teléfono</li>
    </ul>
  </div>

  <div>
    <h2 class="mb-4 text-2xl font-semibold text-black">2. Uso de la Información</h2>
    <p class="mb-6 text-gray-700">La información personal que recopilamos se utiliza para:</p>
    <ul class="mt-2 list-disc list-inside">
      <li>Proporcionar y mejorar nuestros servicios.</li>
      <li>Facilitar la comunicación entre usuarios y proveedores de servicios.</li>
      <li>Responder a consultas y brindar soporte al usuario.</li>
    </ul>
  </div>

  <div>
    <h2 class="mb-4 text-2xl font-semibold text-black">3. Seguridad de la Información</h2>
    <p class="mb-6 text-gray-700">Implementamos medidas de seguridad para proteger la información personal de nuestros usuarios:</p>
    <ul class="mt-2 list-disc list-inside">
      <li>Cifrado: La información personal, incluido el correo electrónico y la contraseña, se cifra para evitar el acceso no autorizado.</li>
    </ul>
  </div>

  <div>
    <h2 class="mb-4 text-2xl font-semibold text-black">4. Cookies</h2>
    <p class="mb-6 text-gray-700">Actualmente, PalitasPR no utiliza cookies ni tecnologías de seguimiento similares.</p>
  </div>

  <div>
    <h2 class="mb-4 text-2xl font-semibold text-black">5. Derechos de los Usuarios</h2>
    <p class="mb-6 text-gray-700">Los usuarios tienen derecho a:</p>
    <ul class="mt-2 list-disc list-inside">
      <li>Acceder: Ver la información personal que hemos recopilado sobre ellos.</li>
      <li>Rectificar: Corregir cualquier información incorrecta o desactualizada.</li>
      <li>Eliminar: Solicitar la eliminación de su información personal de nuestros registros.</li>
    </ul>
    <p class="mb-6">Para ejercer estos derechos, los usuarios pueden ponerse en contacto con nosotros utilizando la información de contacto proporcionada en esta política.</p>
  </div>

  <div>
    <h2 class="mb-4 text-2xl font-semibold text-black">6. Menores de Edad</h2>
    <p class="mb-6 text-gray-700">PalitasPR no está destinada a menores de edad. No permitimos el uso de la aplicación por parte de menores ya que se trata de una plataforma de trabajo y búsqueda de empleadores.</p>
  </div>

  <div>
    <h2 class="mb-4 text-2xl font-semibold text-black">7. Contacto</h2>
    <p class="mb-6 text-gray-700">Si tienes preguntas o preocupaciones sobre esta política de privacidad, puedes ponerte en contacto con nosotros a través del siguiente correo electrónico: <a href="mailto:palitaspr@gmail.com" class="text-blue-600 underline">palitaspr@gmail.com</a>.</p>
  </div>

  <div>
    <h2 class="mb-4 text-2xl font-semibold text-black">8. Cambios en la Política de Privacidad</h2>
    <p class="mb-6 text-gray-700">Nos reservamos el derecho de actualizar esta política de privacidad en cualquier momento. Notificaremos a los usuarios sobre cualquier cambio publicando la nueva política en nuestra aplicación. Se recomienda a los usuarios revisar esta política periódicamente para estar al tanto de cualquier cambio.</p>
  </div>

  <div class="p-4 mb-6 bg-gray-100 rounded-md shadow-md">
    <p>Esta política de privacidad ha sido creada como parte de un proyecto de graduación y actualmente no se aplica a una plataforma pública definitiva.</p>
  </div>
</div>
