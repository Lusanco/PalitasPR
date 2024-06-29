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

  // Format the current date
  let currentDate = new Date();
  let formattedDate = new Intl.DateTimeFormat("es-ES", {
    day: "numeric",
    month: "long",
    year: "numeric",
  }).format(currentDate);
</script>

<div
  class="container max-w-6xl px-4 py-8 mx-auto my-20 bg-primary hover:cursor-default"
>
  <div
    class="p-5 bg-white border-b-2 rounded-md shadow-lg text-balance border-accent"
  >
    <h1 class="text-5xl font-bold text-center text-accent">Terminos de Uso</h1>
    <br />
    <p class="text-xl text-center">
      Bienvenido a <span class="font-semibold text-accent">PalitasPR</span>. El
      acceso y uso de nuestra aplicación, un mercado local para solicitar y
      promocionar servicios en Puerto Rico, está estrictamente regido bajo los
      detalles aquí proporcionados. Al utilizar nuestra aplicación, aceptas
      cumplir con los mismos. Si no estás de acuerdo, te recomendamos desistir
      de utilizar nuestra aplicación.
    </p>
  </div>
  <br />
  <div
    class="p-2 text-xl font-semibold text-center bg-white shadow-xl md:p-4 rounded-xl md:text-left"
  >
    <br />
    <div class="">
      <h2 class="text-2xl font-semibold">1. Aceptación de los Términos</h2>
      <br />
      <p class=" text-secondary">
        Al acceder y utilizar PalitasPR, aceptas estar sujeto a estos términos,
        todas las leyes y regulaciones aplicables.
      </p>
    </div>
    <br />
    <div class="border-b-2 border-accent border-opacity-30"></div>
    <br />
    <div>
      <h2 class="text-2xl font-semibold">2. Descripción del Servicio</h2>
      <br />
      <p class=" text-secondary">
        PalitasPR es una plataforma que permite a los usuarios solicitar y
        promocionar servicios localmente en Puerto Rico. Proporcionamos una
        plataforma para que los usuarios se conecten, pero no somos responsables
        de la calidad, seguridad o legalidad de los servicios proporcionados por
        los usuarios.
      </p>
    </div>
    <br />
    <div class="border-b-2 border-accent border-opacity-30"></div>
    <br />
    <div class="mt-4">
      <h2 class="text-2xl font-semibold">3. Cuentas de Usuario</h2>
      <br />
      <p class=" text-secondary">
        Para utilizar ciertas funciones de PalitasPR, debes registrar una
        cuenta. Aceptas proporcionar información precisa y completa durante el
        registro y mantener la información de tu cuenta actualizada. Eres
        responsable de mantener la confidencialidad de tu cuenta y contraseña, y
        aceptas notificar a PalitasPR de inmediato sobre cualquier uso no
        autorizado de tu cuenta.
      </p>
    </div>
    <br />
    <div class="border-b-2 border-accent border-opacity-30"></div>
    <br />
    <div class="mt-4">
      <h2 class="text-2xl font-semibold text-secondary">4. Uso Aceptable</h2>
      <br />
      <p class=" text-secondary">Al utilizar PalitasPR, aceptas no:</p>
      <ul class="mt-2 list-disc list-inside">
        <li class="list-none">
          <i class="fa-regular fa-hand-point-right"></i>
          Utilizar la plataforma para cualquier propósito ilegal o no autorizado.
        </li>
        <li class="list-none">
          <i class="fa-regular fa-hand-point-right"></i>
          Publicar contenido que sea ofensivo, abusivo, difamatorio, o que infrinja
          los derechos de terceros.
        </li>
        <li class="list-none">
          <i class="fa-regular fa-hand-point-right"></i>
          Utilizar la plataforma para distribuir spam, virus u otro software malicioso.
        </li>
        <li class="list-none">
          <i class="fa-regular fa-hand-point-right"></i>
          Interferir con o interrumpir el funcionamiento de la plataforma.
        </li>
      </ul>
    </div>
    <br />
    <div class="border-b-2 border-accent border-opacity-30"></div>
    <br />
    <div class="mt-4">
      <h2 class="text-2xl font-semibold text-secondary">
        5. Contenido del Usuario
      </h2>
      <br />
      <p class=" text-secondary">
        Eres responsable de todo el contenido que publiques en PalitasPR. Al
        publicar contenido, otorgas a PalitasPR una licencia mundial, no
        exclusiva, libre de regalías, sublicenciable y transferible para
        utilizar, reproducir, modificar, distribuir y mostrar dicho contenido en
        conexión con la operación de la plataforma.
      </p>
    </div>
    <br />
    <div class="border-b-2 border-accent border-opacity-30"></div>
    <br />
    <div>
      <h2 class="text-2xl font-semibold text-secondary">
        6. Terminación del Servicio
      </h2>
      <br />
      <p class=" text-secondary">
        PalitasPR se reserva el derecho de suspender o terminar tu acceso a la
        plataforma en cualquier momento, sin previo aviso, por cualquier motivo,
        incluyendo pero no limitado a, el incumplimiento de estos términos.
      </p>
    </div>
    <br />
    <div class="border-b-2 border-accent border-opacity-30"></div>
    <br />
    <div>
      <h2 class="text-2xl font-semibold text-secondary">
        7. Limitación de Responsabilidad
      </h2>
      <br />
      <p class=" text-secondary">
        PalitasPR no será responsable por cualquier daño indirecto, incidental,
        especial, consecuente o punitivo, incluyendo pero no limitado a, la
        pérdida de beneficios, datos, uso, buena voluntad u otras pérdidas
        intangibles, resultantes de (i) tu acceso o uso de o incapacidad para
        acceder o usar la plataforma, (ii) cualquier conducta o contenido de
        cualquier tercero en la plataforma, (iii) cualquier contenido obtenido
        de la plataforma, y (iv) el acceso no autorizado, uso o alteración de
        tus transmisiones o contenido.
      </p>
    </div>
    <br />
    <div class="border-b-2 border-accent border-opacity-30"></div>
    <br />
    <div>
      <h2 class="text-2xl font-semibold text-secondary">8. Indemnización</h2>
      <br />
      <p class=" text-secondary">
        Aceptas indemnizar y mantener indemne a PalitasPR, sus afiliados,
        empleados y agentes, de cualquier reclamo, daño, obligación, pérdida,
        responsabilidad, costo o deuda, y gasto (incluyendo pero no limitado a
        los honorarios de abogados) que surjan de (i) tu uso y acceso a la
        plataforma, (ii) tu violación de cualquiera de los términos aquí
        detallados, (iii) tu violación de cualquier derecho de terceros,
        incluyendo sin limitación cualquier derecho de autor, propiedad, o de
        privacidad.
      </p>
    </div>
    <br />
    <div class="border-b-2 border-accent border-opacity-30"></div>
    <br />
    <div>
      <h2 class="text-2xl font-semibold text-secondary">9. Ley Aplicable</h2>
      <br />
      <p class=" text-secondary">
        Estos términos se regirán e interpretarán de acuerdo con las leyes de
        Puerto Rico, sin tener en cuenta sus disposiciones sobre conflictos de
        leyes.
      </p>
    </div>
    <br />
    <div class="border-b-2 border-accent border-opacity-30"></div>
    <br />
    <div>
      <h2 class="text-2xl font-semibold text-secondary">
        10. Cambios en los Términos
      </h2>
      <br />
      <p class=" text-secondary">
        PalitasPR se reserva el derecho de modificar estos términos en cualquier
        momento. Te notificaremos sobre cualquier cambio publicando los nuevos
        términos en nuestra plataforma. Es tu responsabilidad revisar estos
        términos periódicamente. El uso continuo de la plataforma después de
        cualquier cambio constituye la aceptación de dichos cambios.
      </p>
    </div>
    <br />
    <div class="border-b-2 border-accent border-opacity-30"></div>
    <br />
    <div>
      <h2 class="text-2xl font-semibold text-secondary">11. Contacto</h2>
      <br />
      <p class=" text-secondary">
        Si tienes preguntas o dudas sobre estos términos, puedes ponerte en
        contacto con nosotros a través del siguiente correo electrónico: <a
          href="mailto:palitaspr@gmail.com"
          class="underline text-accent hover:text-accent/60"
          >palitaspr@gmail.com</a
        >.
      </p>
    </div>

    <p
      class="p-5 mt-8 text-xl font-semibold text-center border-b-2 rounded-md shadow-md text-secondary bg-primary border-accent"
    >
      Has visto los términos en <span class="underline">{formattedDate}</span>
    </p>
  </div>
</div>
