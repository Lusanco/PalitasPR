<script>
  import { onMount } from "svelte";
  import { userSession } from "../scripts/stores";
  import axios from "axios";

  let name, email, subject, message;

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
</script>

<div class="flex flex-col justify-center p-5 m-5">
  <div class="relative py-3 sm:max-w-xl sm:mx-auto">
    <div
      class="absolute inset-0 transform shadow-lg bg-gradient-to-tr from-accent to-secondary via-accent -rotate-6 rounded-3xl"
    ></div>
    <div
      class="relative p-20 px-4 py-10 shadow-lg bg-gradient-to-tr from-white to-white via-primary text-accent rounded-3xl"
    >
      <div class="pb-6 text-center">
        <h1 class="text-3xl">¡Contáctanos!</h1>
        <p class="text-secondary">
          Completa el formulario a continuación para enviarnos un mensaje.
        </p>
      </div>
      <form>
        <input
          class="flex items-center w-full gap-2 px-3 py-2 mb-4 bg-white text-accent input input-bordered"
          type="text"
          placeholder="Nombre"
          name="name"
          bind:value={name}
        />
        <input
          class="flex items-center w-full gap-2 px-3 py-2 mb-4 bg-white text-accent input input-bordered"
          type="email"
          placeholder="Correo electrónico"
          name="email"
          bind:value={email}
        />
        <input
          class="flex items-center w-full gap-2 px-3 py-2 mb-4 bg-white text-accent input input-bordered"
          type="text"
          placeholder="Asunto"
          name="_subject"
          bind:value={subject}
        />
        <textarea
          class="flex items-center w-full h-64 min-h-0 gap-2 px-3 py-2 mb-4 bg-white text-accent input input-bordered"
          placeholder="Escribe tu mensaje aquí..."
          name="message"
          bind:value={message}
          style="height: 121px;"
        ></textarea>
        <div class="flex justify-center w-full">
          <button
            class="flex-1 p-2 mt-2 font-semibold text-center rounded-md shadow-xl text-primary bg-accent hover:bg-white hover:text-accent focus:outline-none focus:shadow-outline"
            type="submit">Enviar</button
          >
        </div>
      </form>
    </div>
  </div>
</div>
