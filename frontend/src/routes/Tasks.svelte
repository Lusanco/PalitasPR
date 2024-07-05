<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { data, response, userSession } from "../scripts/stores";
  import { writable } from "svelte/store";
  import { Link, link } from "svelte-routing";
  import Loading from "../components/Loading.svelte";
  import servicesID from "../scripts/servicesID";
  import Button from "../components/Button.svelte";
  import { split } from "postcss/lib/list";
  import { afterUpdate } from "svelte";
  import QR from "../components/QR.svelte";

  const today = new Date();
  const year = today.getFullYear();
  const month = String(today.getMonth() + 1).padStart(2, "0");
  const day = String(today.getDate()).padStart(2, "0");

  let view;
  let providerName;

  let image = null;
  let someterTask = {
    name: "Someter",
    method: "POST",
    url: "/api/tasks/",
    headers: "application/json", // "application/json"
    twcss:
      "w-full p-2 mb-4 mt-4 font-semibold text-primary bg-accent/90 border-none btn hover:bg-accent transition-all duration-150 ease-in-out",
    misc: { "App Location": "Submit Task" },
  };

  let deleteTask = {
    name: "Eliminar",
    method: "PUT",
    url: "/api/initial-contact",
    headers: "application/json", // "application/json"
    twcss:
      "w-full grow font-semibold bg-accent/90 transition-all duration-150 ease-in-out shadow-md text-primary btn hover:bg-accent",
    misc: { "App Location": "Delete Task" },
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

  // MODIFIED: Reactive statement for clearing inputs
  $: {
    if ($sentReceived !== undefined || $initial_contact_id !== undefined) {
      clearInputs();
      console.log("Inputs cleared due to sentReceived or contactRes change");
    }
  }

  // ADDED: Function to clear inputs
  function clearInputs() {
    price = "";
    bulletPointsStore.set([]);
    inputValue = "";
    // Clear any other inputs you have
  }

  $: {
    bulletPointsStore.subscribe((value) => {
      pipeSeperatedStringStore.set(value.join("|"));
      console.log($pipeSeperatedStringStore);
    });
  }

  let contacts = writable();
  let received = writable();
  let sent = writable();
  let promo = writable("");
  let initial_contact_id = writable(null);
  let sentReceived = writable(true);
  let contactRes = writable([]);
  let promoRequestID = writable();
  let userDetails = writable();
  let submitData = writable();
  let price = "";
  let terms;
  let taskClosed = false;
  let myTask = "";
  let bulletPoints = [];

  let contactResponses = [];

  afterUpdate(() => {
    contactResponses = [...$contactRes];
  });

  $: {
    $submitData = {
      initial_contact_id: $initial_contact_id,
      terms: $pipeSeperatedStringStore,
      price,
    };
    // sentReceived.set($sentReceived);
    if ($sentReceived) {
      sentReceived.set(true);
      console.log("Inside Received If Block");
      if (
        $submitData.initial_contact_id &&
        $submitData.terms &&
        $submitData.price &&
        $contactRes[0].promo_id
      ) {
        console.log("If promo_id exist: ", $contactRes[0].promo_id);
        data.set($submitData);
        console.log("If Submit on Received: ", $data);
      } else if (
        $submitData.initial_contact_id &&
        $submitData.terms &&
        $submitData.price &&
        $contactRes[0].request_id
      ) {
        console.log("If request_id exist: ", $contactRes[0].request_id);
        data.set($submitData);
        console.log("If Submit on Sent: ", $data);
      } else if (
        !$submitData.initial_contact_id ||
        !$submitData.terms ||
        !$submitData.price
      ) {
        $data = {
          id: $initial_contact_id,
          receiver_hide: $sentReceived,
        };
        data.set($data);
        console.log("Else If For Received: ", $data);
      }
      console.log("End of Received If Block");
    } else {
      console.log("Inside Sent Else Block");
      if (
        $submitData.initial_contact_id &&
        $submitData.terms &&
        $submitData.price &&
        $contactRes[0].promo_id
      ) {
        console.log("If promo_id exist: ", $contactRes[0].promo_id);
        data.set($submitData);
        console.log("If Submit on Received: ", $data);
      } else if (
        $submitData.initial_contact_id &&
        $submitData.terms &&
        $submitData.price &&
        $contactRes[0].request_id
      ) {
        console.log("If request_id exist: ", $contactRes[0].request_id);
        data.set($submitData);
        console.log("If Submit on Sent: ", $data);
      } else if (
        !$submitData.initial_contact_id ||
        !$submitData.terms ||
        !$submitData.price
      ) {
        $data = {
          id: $initial_contact_id,
          sender_hide: !$sentReceived,
        };
        data.set($data);
        console.log("Else If For Sent: ", $data);
      }
      console.log("End of Sent If Block");
    }
  }

  let loading = true;

  onMount(() => {
    loading = true;
    axios
      .get("/api/user/status")
      .then((userStatusRes) => {
        userSession.set(true);
        userDetails.set(userStatusRes.data);
        console.log("userStatusRes", userStatusRes.data);
        console.log($userDetails);

        return axios.get("/api/user/contacts");
      })
      .then((userContactsRes) => {
        console.log("Contacts", userContactsRes);
        contacts.set(userContactsRes.data);
        received.set($contacts.results.received);
        sent.set($contacts.results.sent);
        initial_contact_id.set($received.id);

        if ($sentReceived === true) {
          contactRes.set($received);
          console.log("ContactRes Received", $contactRes);
        } else if ($sentReceived === false) {
          contactRes.set($sent);
          console.log("ContactRes Sent", $contactRes);
        }

        let promoRequest_id;
        if (!$contactRes === null || !$contactRes[0] === null) {
          promoRequestID.set(
            $contactRes[0].promo_id
              ? $contactRes[0].promo_id
              : $contactRes[0].request_id
          );
          promoRequest_id = $contactRes[0].promo_id;
          if (
            $contactRes[0].task != null &&
            $contactRes[0].task.status === "closed"
          ) {
            taskClosed = true;
          }

          if ($contactRes[0].promo_id) {
            return axios.get(`/api/promotion/${promoRequest_id}`);
          } else {
            return axios.get(`/api/request/${promoRequest_id}`);
          }
        }
        if (promoRequest_id === null) {
          promoRequest_id = "No valid ID";
        }
        return axios.get(`/api/promotion/${promoRequest_id}`);
      })
      .then((promoRes) => {
        promo.set(promoRes.data.results);
        console.log("Promo", promoRes.data);
      })
      .catch((axiosError) => {
        userSession.set(false);
        console.error(".catch() Error Log: ", axiosError);
      })
      .finally(() => {
        loading = false;
      });
  });

  let openIndex = null;
  let activeButton = "received";

  function toggleItem(index) {
    if (openIndex === index) {
      openIndex = null;
      initial_contact_id.set(null); // Clear the ID when closing
    } else {
      openIndex = index;

      $received && $received[index]
        ? initial_contact_id.set($received[index].id)
        : initial_contact_id.set($sent[index].id);
      // if ($received && $received[index]) {
      //   initial_contact_id.set($received[index].id);
      // }
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

  function handleReceivedClick() {
    activeButton = "received";
    cardLoading = true;
    axios
      .get("/api/user/contacts")
      .then((userContactsRes) => {
        contacts.set(userContactsRes.data);
        received.set(userContactsRes.data.results.received);
        contactRes.set(userContactsRes.data.results.received);
        sentReceived.set(true);
        console.log($sentReceived);
      })
      .catch((error) => {
        console.error("Error fetching received contacts:", error);
      })
      .finally(() => {
        cardLoading = false;
      });
  }

  let cardLoading = false;

  function handleSentClick() {
    activeButton = "sent";
    cardLoading = true;
    axios
      .get("/api/user/contacts")
      .then((userContactsRes) => {
        contacts.set(userContactsRes.data);
        sent.set(userContactsRes.data.results.sent);
        contactRes.set(userContactsRes.data.results.sent);
        sentReceived.set(false);
        console.log($sentReceived);
      })
      .catch((error) => {
        console.error("Error fetching sent contacts:", error);
      })
      .finally(() => {
        cardLoading = false;
      });
  }

  console.log("This is the result of userDetails", $userDetails);
</script>

{#if loading}
  <Loading />
{:else}
  <div
    class="flex flex-col items-center w-full min-h-screen px-4 py-20 mx-auto"
  >
    <h1 class="text-3xl font-semibold">Tareas</h1>
    <br />
    <div
      class="flex flex-wrap items-center justify-center w-full max-w-6xl gap-1 mx-auto md:gap-2"
    >
      <button
        on:click={handleReceivedClick}
        class="w-full p-2 mt-4 mb-4 font-semibold transition-all duration-150 ease-in-out border-2 border-white shadow-md grow md:w-fit bg-accent/90 text-primary btn hover:bg-accent
        {activeButton === 'received'
          ? 'bg-accent/90 text-primary hover:text-primary hover:bg-accent'
          : 'bg-white text-secondary hover:text-primary hover:bg-accent'} "
      >
        Recibidos
      </button>
      <button
        on:click={handleSentClick}
        class="w-full p-2 mt-4 mb-4 font-semibold transition-all duration-150 ease-in-out border-2 border-white shadow-md grow md:w-fit bg-accent/90 text-primary btn hover:bg-accent
        {activeButton === 'sent'
          ? 'bg-accent/90 text-primary hover:text-primary hover:bg-accent'
          : 'bg-white text-secondary hover:text-primary hover:bg-accent'} "
      >
        Enviados
      </button>
    </div>
    <div class="flex flex-col w-full h-full py-4 mx-auto">
      {#if $contactRes}
        {#if $contactRes.length === 0}
          {#if cardLoading}
            <Loading />
          {:else}
            <div class="">
              <h1
                class="flex justify-center mt-12 text-xl font-semibold text-center md:mt-24 md:text-3xl"
              >
                Aún no tiene tareas
              </h1>
            </div>
          {/if}
        {/if}
        {#each contactResponses as response, index}
          {#if cardLoading}
            <Loading />
          {:else}
            <div
              class="flex flex-col w-full max-w-6xl px-4 mx-auto mt-2 transition-all duration-100 bg-white border-b-2 rounded-lg border-accent text-secondary hover:bg-accent/10"
            >
              <!-- class="w-full overflow-hidden transition-all duration-200 ease-in-out transform border-b-2 md:border-b-[3px] rounded-md shadow-md min-h-40 md:rounded-2xl card card-side bg-white hover:bg-accent hover:bg-opacity-10 active:scale-95 border-accent" -->
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
                  {#if response.task === null}
                    <span class="bg-[#f1f1f1] p-2 rounded-badge text-[#1f1f1f]"
                      >Nuevo</span
                    >
                  {:else if response.task.status === "closed"}
                    <span class="bg-[#f1f1f1] p-2 rounded-badge text-[#1f1f1f]"
                      >Cerrado</span
                    >
                  {:else if response.task.status === "active"}
                    <span class="p-2 bg-green-500 rounded-badge text-[#1f1f1f]"
                      >Activo</span
                    >
                  {:else if response.task.status === "pending"}
                    <span class="p-2 bg-yellow-500 rounded-badge text-[#1f1f1f]"
                      >Pendiente</span
                    >
                  {:else if response.task.status === "rejected"}
                    <span class="p-2 bg-red-500 rounded-badge text-[#1f1f1f]"
                      >Rechazado</span
                    >
                  {:else if response.task.status === "reviewed"}
                    <span class="bg-[#f1f1f1] p-2 rounded-badge text-[#1f1f1f]"
                      >Reseñado</span
                    >
                  {/if}
                  {#if response.promo_id}
                    <span class="bg-[#f1f1f1] p-2 rounded-badge text-[#1f1f1f]"
                      >Servicio</span
                    >
                  {:else}
                    <span class="bg-[#f1f1f1] p-2 rounded-badge text-[#1f1f1f]"
                      >Solicitud</span
                    >
                  {/if}
                  {#if response.receiver_read === false}
                    <span
                      class="w-10 h-10 bg-accent rounded-badge animate-ping"
                    >
                    </span>
                  {:else if response.receiver_read === true}
                    <span class="w-10 h-10 bg-[#f1f1f1] rounded-badge"> </span>
                  {/if}
                </div>
                <br />
                <div
                  class="flex flex-wrap justify-center w-full md:justify-between"
                >
                  <span>
                    Nombre: {$sentReceived
                      ? `${response.contact_first_name} ${response.contact_last_name}`
                      : `${$userDetails.first_name} ${$userDetails.last_name}`}
                  </span>
                  <span>
                    {response.updated_at}
                  </span>
                </div>
                <div
                  class="flex flex-wrap justify-center w-full gap-2 md:justify-between"
                >
                  <span class="text-center md:text-start">
                    {$sentReceived ? response.phone : $userDetails.phone}
                  </span>
                  <span class="text-center md:text-end">
                    {$sentReceived
                      ? response.contact_email
                      : $userDetails.email}
                  </span>
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
                  <span>{response.promoRequest_title} -</span>
                  <span>{response.promoRequest_description}</span>
                </div>
                <br />

                {#if response.task === null}
                  <div
                    class="w-full min-w-full min-h-full bg-white shadow-lg rounded-2xl"
                  >
                    <div
                      class="flex flex-col overflow-y-scroll min-h-40 max-h-96 md:p-8 lg:p-12 md:card"
                    >
                      <br />
                      <div class="card-header">
                        <h1
                          class="flex justify-center pb-4 text-2xl font-bold border-b-2 text-secondary md:mb-2 md:pb-8 md:text-4xl lg:text-5xl"
                        >
                          Acuerdo de Servicio
                        </h1>
                      </div>
                      <br />
                      <div class="px-2 md:card-body">
                        <!--* Provider Details -->
                        <div class="pb-4 border-b-2">
                          <h1
                            class="mb-4 text-xl font-bold text-center text-secondary md:mb-8 md:text-2xl"
                          >
                            Detalles del Proveedor
                          </h1>
                          <div
                            class="grid grid-cols-1 gap-2 mt-4 md:grid-cols-2"
                          >
                            <!--* Provider Name -->
                            <label
                              for="service-provider"
                              class="col-span-1 font-bold text-secondary text-md"
                            >
                              Nombre
                              {#if response.promo_id}
                                <input
                                  readonly
                                  id="service-provider"
                                  type="text"
                                  class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0"
                                  value={$sentReceived
                                    ? `${$userDetails.first_name} ${$userDetails.last_name}`
                                    : `${response.contact_first_name} ${response.contact_last_name}`}
                                />
                              {:else}
                                <input
                                  readonly
                                  id="service-provider"
                                  type="text"
                                  class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0"
                                  value={$sentReceived
                                    ? `${response.contact_first_name} ${response.contact_last_name}`
                                    : `${$userDetails.first_name} ${$userDetails.last_name}`}
                                />
                              {/if}
                            </label>
                            <!--* Service Provided -->
                            <label
                              for="service"
                              class="col-span-1 font-bold text-secondary text-md"
                            >
                              Servicio
                              <input
                                readonly
                                id="service"
                                type="text"
                                class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0"
                                value={`${response.service}`}
                              />
                            </label>
                            <!-- 
                        condition       received     sent
                        $sentReceived ? response. : response.
                         -->
                            <!--* Provider Email -->
                            <label
                              for="email"
                              class="col-span-1 font-bold text-secondary text-md"
                            >
                              Correo Electrónico
                              {#if response.promo_id}
                                <input
                                  readonly
                                  id="email"
                                  type="email"
                                  value={$sentReceived
                                    ? `${$userDetails.email}`
                                    : `${response.contact_email}`}
                                  class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                />
                              {:else}
                                <input
                                  readonly
                                  id="email"
                                  type="email"
                                  value={$sentReceived
                                    ? `${response.contact_email}`
                                    : `${$userDetails.email}`}
                                  class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                />
                              {/if}
                            </label>
                            <!--* Provider Phone Number -->
                            <label
                              for="phone-number"
                              class="col-span-1 font-bold text-secondary text-md"
                            >
                              Número de Teléfono
                              {#if response.promo_id}
                                <input
                                  readonly
                                  id="phone-number"
                                  type="text"
                                  value={$sentReceived
                                    ? `${$userDetails.phone}`
                                    : `${response.phone}`}
                                  class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                />
                              {:else}
                                <input
                                  readonly
                                  id="phone-number"
                                  type="text"
                                  value={$sentReceived
                                    ? `${response.phone}`
                                    : `${$userDetails.phone}`}
                                  class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                />
                              {/if}
                            </label>
                          </div>
                        </div>
                        <!--* Client Details -->
                        <div class="pb-4 mt-4 border-b-2 md:mt-8">
                          <h1
                            class="mb-4 text-xl font-bold text-center text-secondary md:mb-8 md:text-2xl"
                          >
                            Detalles del Cliente
                          </h1>
                          <div
                            class="grid grid-cols-1 gap-2 mt-4 md:grid-cols-2"
                          >
                            <!--* Client Name -->
                            <label
                              for="service-client"
                              class="col-span-1 font-bold text-secondary text-md"
                            >
                              Nombre
                              {#if response.promo_id}
                                <input
                                  readonly
                                  id="service-client"
                                  type="text"
                                  value={$sentReceived
                                    ? `${response.contact_first_name} ${response.contact_last_name}`
                                    : `${$userDetails.first_name} ${$userDetails.last_name}`}
                                  class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0"
                                />
                              {:else}
                                <input
                                  readonly
                                  id="service-client"
                                  type="text"
                                  value={$sentReceived
                                    ? `${$userDetails.first_name} ${$userDetails.last_name}`
                                    : `${response.contact_first_name} ${response.contact_last_name}`}
                                  class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0"
                                />
                              {/if}
                            </label>
                            <!--* Client Email -->
                            <label
                              for="clientEmail"
                              class="col-span-1 font-bold text-secondary text-md"
                            >
                              Correo Electrónico
                              {#if response.promo_id}
                                <input
                                  readonly
                                  id="clientEmail"
                                  type="email"
                                  value={$sentReceived
                                    ? `${response.contact_email}`
                                    : `${$userDetails.email}`}
                                  class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                />
                              {:else}
                                <input
                                  readonly
                                  id="clientEmail"
                                  type="email"
                                  value={$sentReceived
                                    ? `${$userDetails.email}`
                                    : `${response.contact_email}`}
                                  class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                />
                              {/if}
                            </label>
                            <!--* Client Phone Number -->
                            <label
                              for="clientPhone-number"
                              class="col-span-1 font-bold text-secondary text-md"
                            >
                              Número de Teléfono
                              {#if response.promo_id}
                                <input
                                  id="clientPhone-number"
                                  readonly
                                  value={$sentReceived
                                    ? `${response.phone}`
                                    : `${$userDetails.phone}`}
                                  type="text"
                                  class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                />
                              {:else}
                                <input
                                  id="clientPhone-number"
                                  readonly
                                  value={$sentReceived
                                    ? `${$userDetails.phone}`
                                    : `${response.phone}`}
                                  type="text"
                                  class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                />
                              {/if}
                            </label>
                          </div>
                        </div>
                        <!--* Service Details -->
                        <div class="flex flex-col gap-2 my-4">
                          <!--* Service Description -->
                          {#if ($sentReceived === true && response.promo_id !== null) || ($sentReceived === false && response.request_id !== null)}
                            <h1
                              class="mb-4 text-xl font-bold text-center text-secondary md:mb-8 md:text-2xl"
                            >
                              Terminos del Servicio
                            </h1>
                            <label
                              for="agreement"
                              class="text-lg font-semibold text-secondary text-start"
                            >
                              Descripción
                              <div>
                                <p class="text-xs md:text-sm">
                                  Describa el servicio ofrecido. Puede añadir
                                  más de un artículo a la lista.
                                </p>
                                <!--* Details input -->
                                <!-- When task === null -->
                                <div class="flex gap-2 pb-4 border-b-2">
                                  <input
                                    type="text"
                                    bind:value={inputValue}
                                    on:input={handleInput}
                                    on:keydown={handleKeyDown}
                                    class="w-full p-2 my-2 font-normal bg-white border-2 rounded-md border-secondary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                  />
                                  <button
                                    on:click={addBulletPoint}
                                    class="text-white bg-accent border-none btn mt-[5px] hover:bg-[#BB2532] transition-all duration-150 ease-in-out"
                                  >
                                    <i class="block fa-solid fa-plus md:hidden"
                                    ></i><span class="hidden md:block"
                                      >Añadir</span
                                    >
                                  </button>
                                </div>
                                <ul class="h-auto pb-4 my-4 border-b-2">
                                  {#each $bulletPointsStore as bulletPoint}
                                    <div class="flex justify-between md:mx-4">
                                      <div class="flex gap-2 mt-1">
                                        <i
                                          class="fa-solid fa-check mt-[5px] text-accent"
                                        ></i>
                                        <li
                                          class="overflow-hidden text-base text-md"
                                        >
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
                                            class="transition-all duration-150 ease-in-out fa-solid fa-trash hover:text-accent"
                                          ></i></button
                                        >
                                      </div>
                                    </div>
                                  {/each}
                                </ul>
                              </div>
                            </label>
                          {/if}

                          <!--* Price and Date -->
                          <div
                            class="grid items-start grid-cols-1 gap-2 md:grid-cols-2"
                          >
                            {#if ($sentReceived === true && response.promo_id !== null) || ($sentReceived === false && response.request_id !== null)}
                              <div class="flex col-span-1">
                                <label
                                  for="price"
                                  class="text-lg font-semibold text-secondary text-start"
                                >
                                  <!-- <p>
                                  Promo id: {response.promo_id}, Contact id: {response.contact_id},
                                  User Details: {$userDetails.id}
                                </p> -->
                                  Precio
                                  <!--* Price Input -->
                                  <div class="">
                                    <input
                                      id="price"
                                      type="number"
                                      placeholder="$0.00"
                                      bind:value={price}
                                      on:keypress={restrictToNumbersAndDecimal}
                                      class="p-2 my-2 font-normal bg-white border-2 rounded-md border-secondary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                    />
                                  </div>
                                </label>
                              </div>
                            {/if}
                            <!--* Date Inputs -->
                            <!-- WHEN TASK EXISTS: date = task.created_at -->
                            <div class="flex col-span-1">
                              <label
                                for="month"
                                class="text-lg font-semibold text-secondary text-start"
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
                                    class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                  />
                                  <!--? Day -->
                                  <input
                                    id="day"
                                    type="text"
                                    placeholder="DD"
                                    readonly
                                    value={day}
                                    on:keypress={handleDateInput}
                                    class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                  />
                                  <!--? Year -->
                                  <input
                                    id="year"
                                    type="text"
                                    placeholder="AAAA"
                                    readonly
                                    value={year}
                                    on:keypress={handleDateInput}
                                    class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
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
                              class="border-none ring-2 ease-in-out transition-all duration-200 focus:ring-secondary rounded-sm ring-secondary mt-[5px] text-accent"
                            />
                            <label for="accept">
                              <p class="text-xs text-secondary md:text-base">
                                He leído y acepto los
                                <!-- href="" -->
                                <span
                                  class="no-underline hover:text-[#BB2532] hover:underline text-accent"
                                  >términos y condiciones</span
                                > de PalitasPR. De igual manera, me comprometo a
                                cumplir con los acuerdos establecidos en este documento.
                                Al someter este formulario, acepto que la información
                                proporcionada es verídica y correcta y podría ser
                                utilizada para fines de contacto y/o asuntos legales.
                              </p>
                            </label>
                          </div>
                        </div>
                        <div>
                          <!--* Submit button -->
                          {#if ($sentReceived === true && response.promo_id !== null) || ($sentReceived === false && response.request_id !== null)}
                            <Button button={someterTask} {image} />
                            <br />
                          {/if}
                        </div>
                      </div>
                    </div>
                  </div>
                {:else}
                  <div
                    class="w-full min-w-full min-h-full p-5 bg-white shadow-lg rounded-2xl"
                  >
                    <div
                      class="flex flex-col overflow-y-scroll min-h-40 max-h-96 md:p-8 lg:p-12 md:card"
                    >
                      <div class="card-header">
                        <h1
                          class="flex justify-center pb-4 -mb-4 text-2xl font-bold border-b-2 text-secondary md:mb-2 md:pb-8 md:text-4xl lg:text-5xl"
                        >
                          Revisión de Acuerdo de Servicio
                        </h1>
                      </div>
                      <div class="card-body">
                        <!--* Provider Details -->
                        <div class="pb-4 border-b-2">
                          <h1
                            class="mb-4 text-xl font-bold text-center text-secondary md:mb-8 md:text-2xl"
                          >
                            Detalles del Proveedor
                          </h1>
                          <div
                            class="grid grid-cols-1 gap-2 mt-4 md:grid-cols-2"
                          >
                            <!--* Provider Name -->
                            <label
                              for="service-provider"
                              class="col-span-1 font-bold text-secondary text-md"
                            >
                              Nombre
                              <input
                                readonly
                                id="service-provider"
                                type="text"
                                value={response.task.provider_first_name +
                                  " " +
                                  response.task.provider_last_name}
                                class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0"
                              />
                            </label>
                            <!--* Service Provided -->
                            <label
                              for="service"
                              class="col-span-1 font-bold text-secondary text-md"
                            >
                              Servicio
                              <input
                                readonly
                                id="service"
                                type="text"
                                value={response.task.service}
                                class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0"
                              />
                            </label>
                            <!--* Provider Email -->
                            <label
                              for="email"
                              class="col-span-1 font-bold text-secondary text-md"
                            >
                              Correo Electrónico
                              <input
                                readonly
                                id="email"
                                type="email"
                                value={response.task.provider_email}
                                class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                              />
                            </label>
                            <!--* Provider Phone Number -->
                            <label
                              for="phone-number"
                              class="col-span-1 font-bold text-secondary text-md"
                            >
                              Número de Teléfono
                              <input
                                readonly
                                id="phone-number"
                                type="text"
                                value={response.task.provider_phone}
                                class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                              />
                            </label>
                          </div>
                        </div>
                        <!--* Client Details -->
                        <div class="pb-4 mt-4 border-b-2 md:mt-8">
                          <h1
                            class="mb-4 text-xl font-bold text-center text-secondary md:mb-8 md:text-2xl"
                          >
                            Detalles del Cliente
                          </h1>
                          <div
                            class="grid grid-cols-1 gap-2 mt-4 md:grid-cols-2"
                          >
                            <!--* Client Name -->
                            <label
                              for="service-client"
                              class="col-span-1 font-bold text-secondary text-md"
                            >
                              Nombre
                              <input
                                readonly
                                id="service-client"
                                type="text"
                                value={response.task.receiver_first_name +
                                  " " +
                                  response.task.receiver_last_name}
                                class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0"
                              />
                            </label>
                            <!--* Client Email -->
                            <label
                              for="clientEmail"
                              class="col-span-1 font-bold text-secondary text-md"
                            >
                              Correo Electrónico
                              <input
                                readonly
                                id="clientEmail"
                                type="email"
                                value={response.task.receiver_email}
                                class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                              />
                            </label>
                            <!--* Client Phone Number -->
                            <label
                              for="clientPhone-number"
                              class="col-span-1 font-bold text-secondary text-md"
                            >
                              Número de Teléfono
                              <input
                                readonly
                                id="clientPhone-number"
                                type="text"
                                value={response.task.receiver_phone}
                                class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                              />
                            </label>
                          </div>
                        </div>
                        <!--* Service Details -->
                        <div class="flex flex-col gap-2 my-4">
                          <h1
                            class="mb-4 text-xl font-bold text-center text-secondary md:mb-8 md:text-2xl"
                          >
                            Detalles del servicio
                          </h1>
                          <!--* Service Description -->
                          <label
                            for="agreement"
                            class="text-lg font-semibold text-secondary text-start"
                          >
                            Descripción
                            <div>
                              <p class="text-xs md:text-sm">
                                Detalles del servicio adquirido. Favor leer
                                detenidamente cada punto.
                              </p>
                              <!--* Details input -->
                              <div class="border-[1px] mt-4 -mb-1"></div>
                              <ul class="h-auto pb-4 my-4 border-b-2">
                                {#each response.task.description as bulletPoint}
                                  <div class="flex justify-between mx-4">
                                    <div class="flex gap-2 mt-1">
                                      <i
                                        class="fa-solid fa-check mt-[5px] text-accent"
                                      ></i>
                                      <li class="text-base text-md">
                                        {bulletPoint}
                                      </li>
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
                                class="text-lg font-semibold text-secondary text-start"
                              >
                                Precio
                                <!--* Price Input -->
                                <div class="">
                                  <input
                                    readonly
                                    id="price"
                                    type="text"
                                    value={"$" + response.task.price}
                                    class="p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                  />
                                </div>
                              </label>
                            </div>
                            <!--* Date Inputs -->
                            <div class="flex col-span-1">
                              <label
                                for="month"
                                class="text-lg font-semibold text-secondary text-start"
                              >
                                Fecha <span class="text-xs">(actual)</span>
                                <!--? Month -->
                                <div class="flex gap-2">
                                  <input
                                    readonly
                                    id="month"
                                    type="text"
                                    value={response.task.created_at.split(
                                      " "
                                    )[1]}
                                    class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                  />
                                  <!--? Day -->
                                  <input
                                    readonly
                                    id="day"
                                    type="text"
                                    value={response.task.created_at.split(
                                      " "
                                    )[2]}
                                    class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                  />
                                  <!--? Year -->
                                  <input
                                    readonly
                                    id="year"
                                    type="text"
                                    value={response.task.created_at.split(
                                      " "
                                    )[3]}
                                    class="w-full p-2 my-2 font-normal border-2 rounded-md border-secondary bg-primary focus:outline-none focus:border-secondary focus:ring-0 placeholder:text-secondary"
                                  />
                                </div>
                              </label>
                            </div>
                          </div>
                        </div>
                        <!--* Signature and Agreement -->
                        <div>
                          <!--? Signature Input -->
                          <!-- <label for="signature">
                        <h1
                          class="text-lg font-semibold text-secondary text-start"
                        >
                          Firma <span class="text-xs">(electrónica)</span>
                        </h1>
                        <input
                          id="signature"
                          type="text"
                          class="w-full p-2 my-2 font-normal bg-white border-2 rounded-md border-secondary focus:outline-none focus:border-secondary focus:ring-0"
                        />
                      </label> -->
                          <!--? Agreement Checkbox -->
                          <div class="flex gap-2 mt-2">
                            <!-- <input
                          disabled
                          checked
                          id="accept"
                          type="checkbox"
                          class="border-none ring-2 ease-in-out transition-all duration-200 focus:ring-secondary rounded-sm ring-secondary mt-[5px] text-accent"
                        /> -->
                            <label for="accept">
                              <p class="text-xs text-secondary md:text-base">
                                He leído y acepto los
                                <a
                                  href="/"
                                  class="no-underline hover:text-[#BB2532] hover:underline text-accent"
                                  >términos y condiciones</a
                                > de PalitasPR. De igual manera, me comprometo a
                                cumplir con los acuerdos establecidos en este documento.
                                Al someter este formulario, acepto que la información
                                proporcionada es verídica y correcta y podría ser
                                utilizada para fines de contacto y/o asuntos legales.
                              </p>
                            </label>
                          </div>
                        </div>
                        <!-- <div> -->
                        <!--* Submit button -->
                        <!-- <button
                        class="w-full p-2 mt-4 font-semibold text-white bg-accent border-none btn hover:bg-[#BB2532] transition-all duration-150 ease-in-out"
                        >Someter</button
                      >
                    </div> -->
                        {#if response.task.status === "pending"}
                          {#if response.task.receiver_id === $userDetails.id}
                            <button
                              on:click={() => {
                                axios
                                  .put("/api/tasks/", {
                                    id: response.task.id,
                                    status: "active",
                                  })
                                  .then((submit) => {
                                    console.log("Data submitted", submit);
                                    window.location.href = "/tasks";
                                  })
                                  .catch((submitErr) => {
                                    console.error(
                                      "Error submitting data",
                                      submitErr
                                    );
                                  });
                              }}
                              class="flex-1 mt-2 btn bg-accent/90 text-primary hover:bg-accent"
                            >
                              Someter
                            </button>
                          {/if}
                        {/if}
                        {#if response.task.status === "active"}
                          {#if response.task.provider_id === $userDetails.id}
                            <button
                              on:click={() => {
                                axios
                                  .put("/api/tasks/", {
                                    id: response.task.id,
                                    status: "closed",
                                  })
                                  .then((submit) => {
                                    console.log("Data submitted", submit);
                                    window.location.href = "/tasks";
                                  })
                                  .catch((submitErr) => {
                                    console.error(
                                      "Error submitting data",
                                      submitErr
                                    );
                                  });
                              }}
                              class="flex-1 mt-2 btn bg-accent/90 text-primary hover:bg-accent"
                            >
                              Cerrar
                            </button>
                          {/if}
                        {/if}
                        <!--* ATH Movil QR -->
                        {#if response.task.status === "closed" || response.task.status === "reviewed"}
                          {#if response.task.provider_id === $userDetails.id}
                            <div
                              class="flex items-center justify-center w-full h-full overflow-x-auto"
                            >
                              <QR
                                view={"provider"}
                                providerName={$userDetails.first_name +
                                  " " +
                                  $userDetails.last_name}
                                imageUrl={response.task.qr_pic}
                              ></QR>
                            </div>
                          {:else if response.task.receiver_id === $userDetails.id}
                            <div
                              class="flex items-center justify-center mx-auto overflow-x-auto"
                            >
                              <QR
                                view={"receiver"}
                                providerName={response.task
                                  .provider_first_name +
                                  " " +
                                  response.task.provider_last_name}
                                imageUrl={response.task.qr_pic}
                              ></QR>
                            </div>
                          {/if}
                        {/if}
                      </div>
                    </div>
                  </div>
                {/if}
                <div class="my-4">
                  <div class="flex flex-col w-full grow">
                    {#if response.task && response.task.status === "closed"}
                      <!-- Add an additional check for response.task to avoid null/undefined errors -->
                      {#if response.task.receiver_id === $userDetails.id}
                        <Link
                          to="/create-review/{response.task.id}"
                          class="w-full p-2 mt-4 mb-4 font-semibold transition-all duration-150 ease-in-out shadow-md grow bg-accent/90 text-primary btn hover:bg-accent"
                          >Dejar reseña</Link
                        >
                      {/if}
                    {/if}
                    {#if response.task === null}
                      <Button button={deleteTask} {image} />
                    {/if}
                    {#if response.task && response.task.status !== "active"}
                      <Button button={deleteTask} {image} />
                    {/if}
                  </div>
                </div>
              </div>
              <br />
              <div
                class="flex flex-wrap items-center justify-center w-full gap-1 mx-auto md:gap-2"
              >
                <!-- Delete Task (Archive) -->
                <!-- <Button button={deleteTask} {image} /> -->
                <!-- <button
              class="grow w-full md:w-fit p-2 mb-4 mt-4 font-semibold bg-accent transition-all duration-150 ease-in-out shadow-md text-[#f1f1f1] btn hover:bg-white hover:text-[#1f1f1f] border-2 border-white"
              >Delete Task</button
            > -->
              </div>
            </div>
          {/if}
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
{/if}
