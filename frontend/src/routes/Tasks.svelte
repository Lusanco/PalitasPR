<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { data, response } from "../scripts/stores";
  import { writable } from "svelte/store";
  import { link } from "svelte-routing";
  import Loading from "../components/Loading.svelte";
  import servicesID from "../scripts/servicesID";
  import Button from "../components/Button.svelte";

  const today = new Date();
  const year = today.getFullYear();
  const month = String(today.getMonth() + 1).padStart(2, "0");
  const day = String(today.getDate()).padStart(2, "0");

  let image = null;
  let button = {
    name: "Someter",
    method: "POST",
    url: "/api/tasks/",
    headers: "application/json", // "application/json"
    twcss:
      "w-full p-2 mb-4 mt-4 font-semibold text-white bg-[#cc2936] border-none btn hover:bg-[#BB2532] transition-all duration-150 ease-in-out",
    misc: { "App Location": "Tasks" },
  };

  const serviceNamesByID = Object.entries(servicesID).reduce(
    (obj, [key, value]) => {
      obj[value] = key;
      return obj;
    },
    {}
  );

  let bulletPointsStore = writable([]);
  let pipeSeperatedStringStore = writable("");

  $: {
    bulletPointsStore.subscribe((value) => {
      pipeSeperatedStringStore.set(value.join("|"));
      console.log($pipeSeperatedStringStore);
    });
  }

  let contacts = writable();
  let received = writable();
  let sent = writable();
  let promo = writable();
  let userSession = writable();
  let price = "";
  let initial_contact_id = writable(null);
  let terms;

  $: {
    $data = {
      initial_contact_id: $initial_contact_id,
      terms: $pipeSeperatedStringStore,
      price,
    };

    data.set($data);
    console.log("Data updated:", $data);
  }

  onMount(() => {
    axios
      .get("/api/user/status")
      .then((userStatusRes) => {
        userSession.set(userStatusRes.data);
        // console.log(".then() User Session Log: ", $userSession);
        if ($userSession) {
          return axios.get("/api/user/contacts");
        } else {
          userSession.set(null);
        }
      })
      .then((userContactsRes) => {
        console.log("Contacts", userContactsRes);
        response.set(userContactsRes);
        contacts.set(userContactsRes.data);
        received.set($contacts.results.received);
        sent.set($contacts.results.sent);
        initial_contact_id.set($received.id);

        // *************** Finding the Specific Task Key **************
        const targetKey = "promo_id";
        const foundTask = $received.find((item) =>
          item.task.hasOwnProperty(targetKey)
        );
        const promo_id = foundTask.task[targetKey];

        // console.log("RECEIVED =>");
        // console.table($received);
        // console.log("RECEIVED.TASK =>");
        // $received.forEach((item) => {
        //   console.table(item.task);
        // });
        // console.log("SENT =>");
        // console.table($sent);
        // console.log("SENT.TASK =>");
        // $sent.forEach((item) => {
        //   console.table(item.task);
        // });
        return axios.get(`/api/promotion/${promo_id}`);
      })
      .then((promoRes) => {
        promo.set(promoRes.data);
        // console.log($promo);
      })
      .catch((axiosError) => {
        console.error(".catch() Error Log: ", axiosError);
      });
  });

  let openIndex = null;

  function toggleItem(index) {
    if (openIndex === index) {
      openIndex = null;
      initial_contact_id.set(null); // Clear the ID when closing
    } else {
      openIndex = index;
      if ($received && $received[index]) {
        initial_contact_id.set($received[index].id);
      }
    }
  }

  /**
   ** Function to handle date inputs for month, day, and year fields
   */

  let inputValue = "";

  function handleInput(event) {
    inputValue = event.target.value;
  }

  /**
   ** Function to handle keydown events for the Description input field
   */

  function handleKeyDown(event) {
    if (event.key === "Enter" && inputValue.trim() !== "") {
      addBulletPoint();
      event.preventDefault(); // Prevent default form submission
    }
  }

  /**
   ** Function to add bullet points to the list
   */

  function addBulletPoint() {
    if (inputValue.trim() !== "") {
      bulletPointsStore.update((points) => [...points, inputValue]);
      inputValue = "";
    }
  }

  /**
   ** Function to handle date inputs for month, day, and year fields
   */

  function handleDateInput(event) {
    const input = event.target;
    const key = event.key;
    const value = input.value;

    // Allow numbers
    const allowedKeys = /[0-9]/;
    if (!allowedKeys.test(key)) {
      event.preventDefault();
      return;
    }
  }

  /**
   ** Function to restrict input to digits and dashes only, and limit to a specific
   ** format
   */

  function restrictToNumbersAndDashes(event) {
    const input = event.target;
    const key = event.key;
    const value = input.value;

    // Allow numbers, dashes, and control keys (backspace, delete, arrow keys)
    const allowedKeys = /[0-9-]|Backspace|Delete|ArrowLeft|ArrowRight|Tab/;
    if (!allowedKeys.test(key)) {
      event.preventDefault();
      return;
    }

    // Add dashes to the input value
    if ((/[0-9-]/.test(key) && value.length === 3) || value.length === 7) {
      input.value = `${value}-`;
    }
    if (value.length >= 12 && /[0-9-]/.test(key)) {
      event.preventDefault();
    }
  }

  /**
   ** Function to restrict input to digits, dots, and commas only for price input
   */

  function restrictToNumbersAndDecimal(event) {
    const input = event.target;
    const key = event.key;

    // Allow numbers, dots, commas, $, and control keys (backspace, delete, arrow keys)
    const allowedKeys = /[0-9.,$]|Backspace|Delete|ArrowLeft|ArrowRight|Tab/;
    if (!allowedKeys.test(key)) {
      event.preventDefault();
      return;
    }

    // Allow only one dot or comma in the input value
    if (key === "." && input.value.includes(key)) {
      event.preventDefault();
      return;
    }
  }

  /**
   *! Placeholder values for the form fields
   */
</script>

<div class="flex flex-col items-center w-full min-h-screen px-4 py-20 mx-auto">
  <h1 class="text-3xl font-semibold">Tasks</h1>
  <div class="flex flex-col w-full h-full py-4 mx-auto">
    {#if $received && $sent && $promo && $contacts}
      {#each $received as received, index}
        <div
          class="max-w-6xl px-4 mx-auto w-full bg-white border-b-2 rounded-lg border-[#cc2936] text-[#1f1f1f] flex flex-col transition-all duration-100 hover:bg-[#cc2936] hover:text-[#f1f1f1]"
        >
          <button
            class="flex flex-col w-full gap-1 px-2 py-4 text-lg font-medium text-left rounded-lg md:text-xl focus:outline-none"
            on:click={() => toggleItem(index)}
            on:click={() => {
              axios
                .put("/api/initial-contact", {
                  id: $initial_contact_id,
                  receiver_read: true,
                })
                .then((readRes) => {
                  console.log({
                    id: $initial_contact_id,
                    receiver_read: true,
                  });
                  console.log(readRes);
                })
                .catch((readErr) => {
                  console.log(readErr);
                });
            }}
          >
            <div class="flex flex-wrap justify-between w-full">
              {#if received.task === null}
                <span class="bg-[#f1f1f1] p-2 rounded-badge text-[#1f1f1f]"
                  >new</span
                >
              {:else if received.task.status === "closed"}
                <span class="bg-[#f1f1f1] p-2 rounded-badge text-[#1f1f1f]"
                  >{received.task.status}</span
                >
              {:else if received.task.status === "active"}
                <span class="p-2 bg-green-500 rounded-badge text-[#1f1f1f]"
                  >{received.task.status}</span
                >
              {:else if received.task.status === "pending"}
                <span class="p-2 bg-yellow-500 rounded-badge text-[#1f1f1f]"
                  >{received.task.status}</span
                >
              {:else if received.task.status === "rejected"}
                <span class="p-2 bg-red-500 rounded-badge text-[#1f1f1f]"
                  >{received.task.status}</span
                >
              {/if}
              {#if received.receiver_read === false}
                <span class="w-10 h-10 bg-[#cc2936] rounded-badge animate-ping">
                </span>
              {:else if received.receiver_read === true}
                <span class="w-10 h-10 bg-[#f1f1f1] rounded-badge"> </span>
              {/if}
            </div>
            <br />
            <div
              class="flex flex-wrap justify-center w-full md:justify-between"
            >
              <span>
                Name: {received.sender_first_name}
                {received.sender_last_name}
              </span>
              <span>
                {received.updated_at}
              </span>
            </div>
            <div
              class="flex flex-wrap justify-center w-full md:justify-between"
            >
              <span>{received.phone}</span>
              <span> {received.sender_email} </span>
            </div>
          </button>
          <div
            class={`overflow-hidden transition-all duration-300  rounded-2xl  ${openIndex === index ? "max-h-screen" : "max-h-0"}`}
          >
            <br />
            <div
              class="flex justify-center w-full pb-4 -mb-4 text-xl font-bold md:border-b-2 md:mb-2 md:pb-8 md:text-2xl lg:text-3xl"
            >
              Servicio Solicitado
            </div>

            <br />
            <div class="w-full text-justify">
              <span>
                {$promo.results.title}:
              </span>
              <span>
                {$promo.results.description}
              </span>
            </div>
            <br />

            <div
              class="w-full min-w-full min-h-full bg-white shadow-lg rounded-2xl"
            >
              <div
                class="flex flex-col overflow-y-scroll min-h-40 max-h-96 md:p-8 lg:p-12 md:card"
              >
                <br />
                <div class="card-header">
                  <h1
                    class="flex justify-center pb-4 text-2xl font-bold text-gray-700 border-b-2 md:mb-2 md:pb-8 md:text-4xl lg:text-5xl"
                  >
                    Acuerdo de Servicio
                  </h1>
                </div>
                <br />
                <div class="px-2 md:card-body">
                  <!--* Provider Details -->
                  <div class="pb-4 border-b-2">
                    <h1
                      class="mb-4 text-xl font-bold text-center text-gray-700 md:mb-8 md:text-2xl"
                    >
                      Detalles del Proveedor
                    </h1>
                    <div class="grid grid-cols-1 gap-2 mt-4 md:grid-cols-2">
                      <!--* Provider Name -->
                      <label
                        for="service-provider"
                        class="col-span-1 font-bold text-gray-500 text-md"
                      >
                        Nombre
                        <input
                          id="service-provider"
                          type="text"
                          readonly
                          class="w-full p-2 my-2 font-normal border-2 border-gray-300 rounded-md bg-slate-100 focus:outline-none focus:border-gray-300 focus:ring-0"
                          value={`${$promo.results.first_name} ${$promo.results.last_name}`}
                        />
                      </label>
                      <!--* Service Provided -->
                      <label
                        for="service"
                        class="col-span-1 font-bold text-gray-500 text-md"
                      >
                        Servicio
                        <input
                          id="service"
                          type="text"
                          readonly
                          class="w-full p-2 my-2 font-normal border-2 border-gray-300 rounded-md bg-slate-100 focus:outline-none focus:border-gray-300 focus:ring-0"
                          value={serviceNamesByID[$promo.results.service_id]}
                        />
                      </label>
                      <!--* Provider Email -->
                      <label
                        for="email"
                        class="col-span-1 font-bold text-gray-500 text-md"
                      >
                        Correo Electrónico
                        <input
                          readonly
                          id="email"
                          type="email"
                          value={$userSession.email}
                          class="w-full p-2 my-2 font-normal border-2 border-gray-300 rounded-md bg-slate-100 focus:outline-none focus:border-gray-300 focus:ring-0 placeholder:text-slate-300"
                        />
                      </label>
                      <!--* Provider Phone Number -->
                      <label
                        for="phone-number"
                        class="col-span-1 font-bold text-gray-500 text-md"
                      >
                        Número de Teléfono
                        <input
                          readonly
                          id="phone-number"
                          required
                          pattern="\d{3}-\d{3}-\d{4}"
                          on:keypress={restrictToNumbersAndDashes}
                          value={$userSession.phone}
                          type="text"
                          class="w-full p-2 my-2 font-normal border-2 border-gray-300 rounded-md bg-slate-100 focus:outline-none focus:border-gray-300 focus:ring-0 placeholder:text-slate-300"
                        />
                      </label>
                    </div>
                  </div>
                  <!--* Client Details -->
                  <div class="pb-4 mt-4 border-b-2 md:mt-8">
                    <h1
                      class="mb-4 text-xl font-bold text-center text-gray-700 md:mb-8 md:text-2xl"
                    >
                      Detalles del Cliente
                    </h1>
                    <div class="grid grid-cols-1 gap-2 mt-4 md:grid-cols-2">
                      <!--* Client Name -->
                      <label
                        for="service-client"
                        class="col-span-1 font-bold text-gray-500 text-md"
                      >
                        Nombre
                        <input
                          id="service-client"
                          type="text"
                          readonly
                          class="w-full p-2 my-2 font-normal border-2 border-gray-300 rounded-md bg-slate-100 focus:outline-none focus:border-gray-300 focus:ring-0"
                          value={`${received.sender_first_name} ${received.sender_last_name}`}
                        />
                      </label>
                      <!--* Client Email -->
                      <label
                        for="clientEmail"
                        class="col-span-1 font-bold text-gray-500 text-md"
                      >
                        Correo Electrónico
                        <input
                          readonly
                          id="clientEmail"
                          type="email"
                          value={received.sender_email}
                          class="w-full p-2 my-2 font-normal border-2 border-gray-300 rounded-md bg-slate-100 focus:outline-none focus:border-gray-300 focus:ring-0 placeholder:text-slate-300"
                        />
                      </label>
                      <!--* Client Phone Number -->
                      <label
                        for="clientPhone-number"
                        class="col-span-1 font-bold text-gray-500 text-md"
                      >
                        Número de Teléfono
                        <input
                          id="clientPhone-number"
                          readonly
                          pattern="\d{3}-\d{3}-\d{4}"
                          value={received.phone}
                          type="text"
                          class="w-full p-2 my-2 font-normal border-2 border-gray-300 rounded-md bg-slate-100 focus:outline-none focus:border-gray-300 focus:ring-0 placeholder:text-slate-300"
                        />
                      </label>
                    </div>
                  </div>
                  <!--* Service Details -->
                  <div class="flex flex-col gap-2 my-4">
                    <h1
                      class="mb-4 text-xl font-bold text-center text-gray-700 md:mb-8 md:text-2xl"
                    >
                      Terminos del Servicio
                    </h1>
                    <!--* Service Description -->
                    <label
                      for="agreement"
                      class="text-lg font-semibold text-gray-500 text-start"
                    >
                      Descripción
                      <div>
                        <p class="text-xs md:text-sm">
                          Describa el servicio ofrecido. Puede añadir más de un
                          artículo a la lista.
                        </p>
                        <!--* Details input -->
                        <div class="flex gap-2 pb-4 border-b-2">
                          <input
                            type="text"
                            bind:value={inputValue}
                            on:input={handleInput}
                            on:keydown={handleKeyDown}
                            class="w-full p-2 my-2 font-normal bg-white border-2 border-gray-300 rounded-md focus:outline-none focus:border-gray-300 focus:ring-0 placeholder:text-slate-300"
                          />
                          <button
                            on:click={addBulletPoint}
                            class="text-white bg-[#cc2936] border-none btn mt-[5px] hover:bg-[#BB2532] transition-all duration-150 ease-in-out"
                          >
                            <i class="block fa-solid fa-plus md:hidden"
                            ></i><span class="hidden md:block">Añadir</span>
                          </button>
                        </div>

                        <ul class="h-auto pb-4 my-4 border-b-2">
                          {#each $bulletPointsStore as bulletPoint}
                            <div class="flex justify-between md:mx-4">
                              <div class="flex gap-2 mt-1">
                                <i
                                  class="fa-solid fa-check mt-[5px] text-[#cc2936]"
                                ></i>
                                <li class="overflow-hidden text-base text-md">
                                  <p
                                    class="max-w-full line-clamp-none md:line-clamp-4 overflow-ellipsis"
                                  >
                                    {bulletPoint}
                                  </p>
                                </li>
                              </div>
                              <div>
                                <button
                                  on:click={() => {
                                    bulletPointsStore.update((points) =>
                                      points.filter(
                                        (point) => point !== bulletPoint
                                      )
                                    );
                                  }}
                                  class="rounded btn-sm"
                                  ><i
                                    class="fa-solid fa-trash hover:text-[#cc2936] ease-in-out transition-all duration-150"
                                  ></i></button
                                >
                              </div>
                            </div>
                          {/each}
                        </ul>
                      </div>
                    </label>
                    <!--* Price and Date -->
                    <div
                      class="grid items-start grid-cols-1 gap-2 md:grid-cols-2"
                    >
                      <div class="flex col-span-1">
                        <label
                          for="price"
                          class="text-lg font-semibold text-gray-500 text-start"
                        >
                          Precio
                          <!--* Price Input -->
                          <div class="">
                            <input
                              id="price"
                              type="number"
                              placeholder="$0.00"
                              bind:value={price}
                              on:keypress={restrictToNumbersAndDecimal}
                              class="p-2 my-2 font-normal bg-white border-2 border-gray-300 rounded-md focus:outline-none focus:border-gray-300 focus:ring-0 placeholder:text-slate-300"
                            />
                          </div>
                        </label>
                      </div>
                      <!--* Date Inputs -->
                      <div class="flex col-span-1">
                        <label
                          for="month"
                          class="text-lg font-semibold text-gray-500 text-start"
                        >
                          Fecha <span class="text-xs">(actual)</span>
                          <!--? Month -->
                          <div class="flex gap-2">
                            <input
                              id="month"
                              type="text"
                              placeholder="MM"
                              readonly
                              value={month}
                              on:keypress={handleDateInput}
                              class="w-full p-2 my-2 font-normal border-2 border-gray-300 rounded-md bg-slate-100 focus:outline-none focus:border-gray-300 focus:ring-0 placeholder:text-slate-300"
                            />
                            <!--? Day -->
                            <input
                              id="day"
                              type="text"
                              placeholder="DD"
                              readonly
                              value={day}
                              on:keypress={handleDateInput}
                              class="w-full p-2 my-2 font-normal border-2 border-gray-300 rounded-md bg-slate-100 focus:outline-none focus:border-gray-300 focus:ring-0 placeholder:text-slate-300"
                            />
                            <!--? Year -->
                            <input
                              id="year"
                              type="text"
                              placeholder="AAAA"
                              readonly
                              value={year}
                              on:keypress={handleDateInput}
                              class="w-full p-2 my-2 font-normal border-2 border-gray-300 rounded-md bg-slate-100 focus:outline-none focus:border-gray-300 focus:ring-0 placeholder:text-slate-300"
                            />
                          </div>
                        </label>
                      </div>
                    </div>
                  </div>
                  <!--* Signature and Agreement -->
                  <!--? Signature Input -->
                  <div>
                    <!--? Agreement Checkbox -->
                    <div class="flex gap-2 mt-2">
                      <input
                        required
                        id="accept"
                        type="checkbox"
                        class="border-none ring-2 ease-in-out transition-all duration-200 focus:ring-gray-300 rounded-sm ring-gray-300 mt-[5px] text-[#cc2936]"
                      />
                      <label for="accept">
                        <p class="text-xs text-gray-500 md:text-base">
                          He leído y acepto los
                          <!-- href="" -->
                          <span
                            class="no-underline hover:text-[#BB2532] hover:underline text-[#cc2936]"
                            >términos y condiciones</span
                          > de PalitasPR. De igual manera, me comprometo a cumplir
                          con los acuerdos establecidos en este documento. Al someter
                          este formulario, acepto que la información proporcionada
                          es verídica y correcta y podría ser utilizada para fines
                          de contacto y/o asuntos legales.
                        </p>
                      </label>
                    </div>
                  </div>
                  <div>
                    <!--* Submit button -->
                    <Button {button} {image} />
                    <br />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <br />
        </div>
      {/each}
    {:else}
      <div
        class="flex flex-col items-center justify-center w-full min-h-screen py-20 m-auto skeleton"
      >
        <Loading />
      </div>
    {/if}
  </div>
</div>
