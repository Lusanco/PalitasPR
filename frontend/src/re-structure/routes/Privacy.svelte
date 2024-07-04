<script>
  import axios from "axios";
  import { onMount } from "svelte";
  import { userSession } from "../../scripts/stores";

  onMount(() => {
    axios
      .get("/api/user/status")
      .then((userStatusRes) => {
        userSession.set(true);
        console.log(userStatusRes.data);
      })
      .catch((userStatusErr) => {
        userSession.set(false);
        console.log(userStatusErr);
        console.log($userSession);
      });
  });

  let currentDate = new Date().toLocaleDateString();
</script>

<div class="container max-w-6xl px-4 py-8 mx-auto my-20 bg-primary">
  <h1 class="text-4xl font-bold text-center text-secondary">
    Política de Privacidad
  </h1>
  <br />
  <br />
  <div class="p-4 bg-white rounded-md shadow-md">
    <p>
      PalitasPR ("nosotros", "nuestro" o "la aplicación") opera como un mercado
      local para solicitar y promocionar servicios en Puerto Rico. Esta política
      de privacidad describe cómo recopilamos, usamos y protegemos la
      información personal de nuestros usuarios. Esta política aplica a todos
      los usuarios de nuestra aplicación.
    </p>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-secondary">
      1. Información que Recopilamos
    </h2>
    <br />
    <p class=" text-secondary">
      Recopilamos los siguientes tipos de información personal de los usuarios:
    </p>

    <ul class="mt-2 list-disc list-inside">
      <li>Nombre</li>
      <li>Correo electrónico</li>
      <li>Dirección</li>
      <li>Número de teléfono</li>
    </ul>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-secondary">
      2. Uso de la Información
    </h2>
    <br />
    <p class=" text-secondary">
      La información personal que recopilamos se utiliza para:
    </p>

    <ul class="mt-2 list-disc list-inside">
      <li>Proporcionar y mejorar nuestros servicios.</li>
      <li>
        Facilitar la comunicación entre usuarios y proveedores de servicios.
      </li>
      <li>Responder a consultas y brindar soporte al usuario.</li>
    </ul>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-secondary">
      3. Seguridad de la Información
    </h2>
    <br />
    <p class="text-secondary">
      Implementamos medidas de seguridad para proteger la información personal
      de nuestros usuarios:
    </p>
    <ul class="mt-2 list-disc list-inside">
      <li>
        Cifrado: La información personal, incluido el correo electrónico y la
        contraseña, se cifra para evitar el acceso no autorizado.
      </li>
    </ul>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-secondary">4. Cookies</h2>
    <br />
    <p class="text-secondary">
      Actualmente, PalitasPR no utiliza cookies ni tecnologías de seguimiento
      similares.
    </p>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-secondary">
      5. Derechos de los Usuarios
    </h2>
    <br />
    <p class=" text-secondary">Los usuarios tienen derecho a:</p>
    <ul class="mt-2 list-disc list-inside">
      <li>
        Acceder: Ver la información personal que hemos recopilado sobre ellos.
      </li>
      <li>
        Rectificar: Corregir cualquier información incorrecta o desactualizada.
      </li>
      <li>
        Eliminar: Solicitar la eliminación de su información personal de
        nuestros registros.
      </li>
    </ul>
    <br />
    <p class="">
      Para ejercer estos derechos, los usuarios pueden ponerse en contacto con
      nosotros utilizando la información de contacto proporcionada en esta
      política.
    </p>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-secondary">6. Menores de Edad</h2>
    <br />
    <p class="text-secondary">
      PalitasPR no está destinada a menores de edad. No permitimos el uso de la
      aplicación por parte de menores ya que se trata de una plataforma de
      trabajo y búsqueda de empleadores.
    </p>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-secondary">7. Contacto</h2>
    <br />
    <p class=" text-secondary">
      Si tienes preguntas o preocupaciones sobre esta política de privacidad,
      puedes ponerte en contacto con nosotros a través del siguiente correo
      electrónico: <a
        href="mailto:palitaspr@gmail.com"
        class="underline text-accent hover:text-accent/60">palitaspr@gmail.com</a
      >.
    </p>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-secondary">
      8. Cambios en la Política de Privacidad
    </h2>
    <br />
    <p class=" text-secondary">
      Nos reservamos el derecho de actualizar esta política de privacidad en
      cualquier momento. Notificaremos a los usuarios sobre cualquier cambio
      publicando la nueva política en nuestra aplicación. Se recomienda a los
      usuarios revisar esta política periódicamente para estar al tanto de
      cualquier cambio.
    </p>
  </div>
  <br />
  <div class="p-4 bg-white rounded-md shadow-md">
    <p>
      Esta política de privacidad ha sido creada como parte de un proyecto de
      graduación y actualmente no se aplica a una plataforma pública definitiva.
    </p>
  </div>
  <br />
  <p class="text-center text-secondary">
    Has visto sobre el manejo de privacidad en: {currentDate}
  </p>
  <br />
</div>
