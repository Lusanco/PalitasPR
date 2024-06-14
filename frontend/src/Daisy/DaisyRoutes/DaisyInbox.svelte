<script>
  let openIndex = null;

  function toggleItem(index) {
    if (openIndex === index) {
      openIndex = null;
    } else {
      openIndex = null; // Cierra la tarjeta actual inmediatamente
      setTimeout(() => {
        openIndex = index; // Abre la nueva tarjeta después de cerrar la anterior
      }, 0);
    }
  }

  let messages = [
    {
      sender: "Juan Pérez",
      subject: "Consulta sobre el servicio",
      date: "2024-06-13",
      body: "Hola, tengo una consulta sobre el servicio que ofrecen. Me gustaría saber más detalles sobre los precios y la disponibilidad. Gracias.",
    },
    {
      sender: "María González",
      subject: "Problema con la reserva",
      date: "2024-06-12",
      body: "Hola, tuve un problema al intentar reservar un servicio. La página me da un error y no puedo completar la reserva. ¿Podrían ayudarme?",
    },
    {
      sender: "Carlos Ramírez",
      subject: "Agradecimiento",
      date: "2024-06-11",
      body: "Quería agradecerles por el excelente servicio que recibí. La atención fue muy buena y el servicio cumplió con mis expectativas.",
    },
  ];
</script>

<div class="flex flex-col items-center justify-center h-full min-h-screen py-20 m-auto">
  <div class="flex flex-col w-full max-w-5xl gap-4 px-2">
    <div class="flex flex-col gap-4 text-center">
      <h2 class="text-5xl text-gray-800">Inbox</h2>
      <p class="max-w-sm mx-auto">
        Aquí están tus mensajes. Haz clic en un mensaje para ver los detalles.
      </p>
    </div>
    {#each messages as { sender, subject, date, body }, index}
      <div class="max-w-3xl mx-auto border-b border-gray-200 bg-base-200">
        <button
          class="w-full px-2 py-4 text-xl font-medium text-left text-gray-800 hover:bg-gray-300 focus:outline-none"
          on:click={() => toggleItem(index)}
        >
          <div class="flex justify-between">
            <div>{subject}</div>
            <div class="text-sm text-gray-600">{date}</div>
          </div>
          <div class="text-sm text-gray-600">From: {sender}</div>
        </button>
        <div class={`overflow-hidden transition-all duration-300 ${openIndex === index ? "max-h-screen" : "max-h-0"}`}>
          <div class="px-4 py-2">
            <p>{body}</p>
          </div>
        </div>
      </div>
    {/each}
  </div>
</div>