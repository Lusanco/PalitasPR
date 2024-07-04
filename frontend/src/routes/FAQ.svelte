<script>
  import { onMount } from "svelte";
  import { userSession } from "../scripts/stores";
  import axios from "axios";

  let openIndex = null;

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

  function toggleItem(index) {
    openIndex = openIndex === index ? null : index;
  }

  let questions = [
    {
      question: "¿Qué servicios se ofrecen en su plataforma?",
      answer:
        "Nuestra plataforma ofrece una amplia gama de servicios en diversas categorías como servicios del hogar, servicios profesionales, belleza y bienestar, entre otros. Puedes explorar nuestras listas de servicios para encontrar lo que estás buscando.",
    },
    {
      question: "¿Cómo puedo reservar o programar un servicio?",
      answer:
        "Para reservar o programar un servicio, simplemente navega hasta el servicio que te interesa, selecciona la fecha y hora que mejor te convenga, y sigue las indicaciones para completar el proceso de reserva. Recibirás confirmación una vez que tu reserva sea exitosa.",
    },
    {
      question: "¿Cómo puedo pagar por los servicios en su plataforma?",
      answer:
        "Por el momento, el único método de pago con el que trabajamos es ATH Movil. Asegúrate de buscar en la configuración la opción para subir tu código QR. No te preocupes si no sabes cómo hacerlo, tenemos una guía paso a paso para ayudarte a configurarlo. Estamos trabajando en agregar más opciones de pago en el futuro. ¡Mantente atento!",
    },
    {
      question: "¿Cuáles son sus políticas de cancelación y reembolso?",
      answer:
        "Nuestras políticas de cancelación y reembolso varían según el servicio y el proveedor. Generalmente, puedes cancelar o reprogramar citas con un aviso razonable sin penalizaciones. Los reembolsos pueden ser aplicables en ciertas situaciones, como cancelaciones del proveedor o insatisfacción con el servicio prestado.",
    },
    {
      question:
        "¿Cómo se evalúan y califican los proveedores de servicios en su plataforma?",
      answer:
        "Tenemos un riguroso proceso de evaluación para asegurar que nuestros proveedores de servicios cumplan con ciertos estándares de calidad y estén debidamente licenciados y asegurados, cuando corresponda. Además, nuestra plataforma cuenta con un sistema de calificación donde los clientes pueden dejar reseñas y comentarios sobre sus experiencias, ayudando a otros a tomar decisiones informadas.",
    },
    {
      question:
        "¿Puedo dejar reseñas o comentarios para los proveedores de servicios que he utilizado?",
      answer:
        "Sí, animamos a los clientes a dejar reseñas y comentarios honestos sobre los proveedores de servicios que han utilizado en nuestra plataforma. Esto ayuda a mantener la transparencia y el control de calidad, y ayuda a otros usuarios a tomar decisiones informadas basadas en experiencias reales.",
    },
  ];
</script>

<div
  class="flex flex-col items-center justify-center h-full py-20 m-auto min-h-fit"
>
  <div class="flex flex-col w-full max-w-5xl gap-4 px-2">
    <div class="flex flex-col gap-4 text-center">
      <h2 class="text-4xl font-bold text-center text-accent">
        Preguntas frecuentes (FAQ)
      </h2>
      <br />
      <p class="w-full max-w-3xl text-xl text-center">
        Aquí tienes algunas preguntas frecuentes. Si tienes alguna otra
        pregunta, no dudes en contactarnos.
      </p>
    </div>
    <br />
    {#each questions as { question, answer }, index}
      <div
        class="max-w-3xl px-4 mx-auto transition-all duration-100 bg-white border-b-2 rounded-lg border-accent text-secondary hover:bg-accent hover:text-primary"
      >
        <button
          class="w-full px-2 py-4 text-2xl font-medium text-left rounded-lg focus:outline-none"
          on:click={() => toggleItem(index)}
        >
          {question}
        </button>
        <div
          class={`overflow-hidden transition-all duration-300 ${openIndex === index ? "max-h-screen" : "max-h-0"}`}
        >
          <div class="px-4 py-2">
            <p class="text-xl">{answer}</p>
            <br />
          </div>
        </div>
      </div>
    {/each}
  </div>
</div>
