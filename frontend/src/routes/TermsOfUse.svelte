<script>
  import axios from "axios";
  import { onMount } from "svelte";
  import { userSession } from "../scripts/stores";

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

<div class="container max-w-6xl px-4 py-8 mx-auto my-20 bg-base-100">
  <h1 class="text-4xl font-bold text-center text-[#1f1f1f1]">
    Terminos de Uso
  </h1>
  <br />
  <br />
  <div class="p-4 bg-white rounded-md shadow-md">
    <p>
      Bienvenido a PalitasPR. Estos Términos de Uso ("Términos") rigen tu acceso
      y uso de nuestra aplicación, un mercado local para solicitar y promocionar
      servicios en Puerto Rico. Al utilizar nuestra aplicación, aceptas cumplir
      con estos Términos. Si no estás de acuerdo con estos Términos, no uses
      nuestra aplicación.
    </p>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-[#1f1f1f1]">
      1. Aceptación de los Términos
    </h2>
    <br />
    <p class=" text-[#1f1f1f1]">
      Al acceder y utilizar PalitasPR, aceptas estar sujeto a estos Términos,
      todas las leyes y regulaciones aplicables, y aceptas que eres responsable
      de cumplir con las leyes locales aplicables.
    </p>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-[#1f1f1f1]">
      2. Descripción del Servicio
    </h2>
    <br />
    <p class=" text-[#1f1f1f1]">
      PalitasPR es una plataforma que permite a los usuarios solicitar y
      promocionar servicios localmente en Puerto Rico. Proporcionamos una
      plataforma para que los usuarios se conecten, pero no somos responsables
      de la calidad, seguridad o legalidad de los servicios proporcionados por
      los usuarios.
    </p>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-[#1f1f1f1]">
      3. Cuentas de Usuario
    </h2>
    <br />
    <p class=" text-[#1f1f1f1]">
      Para utilizar ciertas funciones de PalitasPR, debes registrar una cuenta.
      Aceptas proporcionar información precisa y completa durante el registro y
      mantener la información de tu cuenta actualizada. Eres responsable de
      mantener la confidencialidad de tu cuenta y contraseña, y aceptas
      notificar a PalitasPR de inmediato sobre cualquier uso no autorizado de tu
      cuenta.
    </p>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-[#1f1f1f1]">4. Uso Aceptable</h2>
    <br />
    <p class=" text-[#1f1f1f1]">Al utilizar PalitasPR, aceptas no:</p>
    <ul class="mt-2 list-disc list-inside">
      <li>
        Utilizar la plataforma para cualquier propósito ilegal o no autorizado.
      </li>
      <li>
        Publicar contenido que sea ofensivo, abusivo, difamatorio, o que
        infrinja los derechos de terceros.
      </li>
      <li>
        Utilizar la plataforma para distribuir spam, virus u otro software
        malicioso.
      </li>
      <li>Interferir con o interrumpir el funcionamiento de la plataforma.</li>
    </ul>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-[#1f1f1f1]">
      5. Contenido del Usuario
    </h2>
    <br />
    <p class=" text-[#1f1f1f1]">
      Eres responsable de todo el contenido que publiques en PalitasPR. Al
      publicar contenido, otorgas a PalitasPR una licencia mundial, no
      exclusiva, libre de regalías, sublicenciable y transferible para utilizar,
      reproducir, modificar, distribuir y mostrar dicho contenido en conexión
      con la operación de la plataforma.
    </p>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-[#1f1f1f1]">
      6. Terminación del Servicio
    </h2>
    <br />
    <p class=" text-[#1f1f1f1]">
      PalitasPR se reserva el derecho de suspender o terminar tu acceso a la
      plataforma en cualquier momento, sin previo aviso, por cualquier motivo,
      incluyendo pero no limitado a, el incumplimiento de estos Términos.
    </p>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-[#1f1f1f1]">
      7. Limitación de Responsabilidad
    </h2>
    <br />
    <p class=" text-[#1f1f1f1]">
      PalitasPR no será responsable por cualquier daño indirecto, incidental,
      especial, consecuente o punitivo, incluyendo pero no limitado a, la
      pérdida de beneficios, datos, uso, buena voluntad u otras pérdidas
      intangibles, resultantes de (i) tu acceso o uso de o incapacidad para
      acceder o usar la plataforma; (ii) cualquier conducta o contenido de
      cualquier tercero en la plataforma; (iii) cualquier contenido obtenido de
      la plataforma; y (iv) el acceso no autorizado, uso o alteración de tus
      transmisiones o contenido.
    </p>
  </div>
  <br />

  <div>
    <h2 class="text-2xl font-semibold text-[#1f1f1f1]">8. Indemnización</h2>
    <br />
    <p class=" text-[#1f1f1f1]">
      Aceptas indemnizar y mantener indemne a PalitasPR, sus afiliados,
      empleados y agentes, de cualquier reclamo, daño, obligación, pérdida,
      responsabilidad, costo o deuda, y gasto (incluyendo pero no limitado a los
      honorarios de abogados) que surjan de (i) tu uso y acceso a la plataforma;
      (ii) tu violación de cualquier término de estos Términos; (iii) tu
      violación de cualquier derecho de terceros, incluyendo sin limitación
      cualquier derecho de autor, propiedad, o de privacidad.
    </p>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-[#1f1f1f1]">9. Ley Aplicable</h2>
    <br />
    <p class=" text-[#1f1f1f1]">
      Estos Términos se regirán e interpretarán de acuerdo con las leyes de
      Puerto Rico, sin tener en cuenta sus disposiciones sobre conflictos de
      leyes.
    </p>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-[#1f1f1f1]">
      10. Cambios en los Términos
    </h2>
    <br />
    <p class=" text-[#1f1f1f1]">
      PalitasPR se reserva el derecho de modificar estos Términos en cualquier
      momento. Te notificaremos sobre cualquier cambio publicando los nuevos
      Términos en nuestra plataforma. Es tu responsabilidad revisar estos
      Términos periódicamente. El uso continuado de la plataforma después de
      cualquier cambio constituye la aceptación de dichos cambios.
    </p>
  </div>
  <br />
  <div>
    <h2 class="text-2xl font-semibold text-[#1f1f1f1]">11. Contacto</h2>
    <br />
    <p class=" text-[#1f1f1f]">
      Si tienes preguntas sobre estos Términos, puedes ponerte en contacto con
      nosotros a través del siguiente correo electrónico: <a
        href="mailto:palitaspr@gmail.com"
        class="text-[#cc2936] underline">palitaspr@gmail.com</a
      >.
    </p>
  </div>
  <br />

  <div class="p-4 bg-white rounded-md shadow-md">
    <p>
      Estos Términos de Uso han sido creados como parte de un proyecto de
      graduación y actualmente no se aplican a una plataforma pública
      definitiva.
    </p>
  </div>
  <br />
  <p class="text-center text-[#1f1f1f1]">
    Has visto los terminos de uso en: {currentDate}
  </p>
  <br />
</div>
