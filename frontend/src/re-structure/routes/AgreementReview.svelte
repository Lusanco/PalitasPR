<script>
  import { onMount } from "svelte";
  import { userSession } from "../../scripts/stores";
  import axios from "axios";

  /**
   ** Function to handle date inputs for month, day, and year fields
   */

  let inputValue = "";
  let bulletPoints = [
    "Corte de césped",
    "Podar arbustos",
    "Limpiar jardín",
    "Fertilizar plantas",
    "Regar plantas",
  ];
  let placeholderName = "Juan del Pueblo";
  let placeholderClient = "Pedro del Pueblo";

  let placeholderService = "Jardinería";

  let placeholderPhone = "787-123-4567";
  let placeholderClientPhone = "787-765-4321";

  let placeholderEmail = "juandelpueblo@mail.com";
  let placeholderClientEmail = "pedrodelpueblo@mail.com";
  let placeholderDate = {
    month: "06",
    day: "02",
    year: "2024",
  };

  /**
   ** Function to handle date inputs for month, day, and year fields
   */

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

<div class="flex flex-col items-center min-h-screen p-4 md:p-12 bg-slate-100">
  <div class="w-full p-4 bg-white shadow-lg md:p-8 lg:p-12 card">
    <div class="card-header">
      <h1
        class="flex justify-center pb-4 -mb-4 text-2xl font-bold text-gray-700 border-b-2 md:mb-2 md:pb-8 md:text-4xl lg:text-5xl"
      >
        Revisión de Acuerdo de Servicio
      </h1>
    </div>
    <div class="card-body">
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
              value={placeholderName}
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
              value={placeholderService}
            />
          </label>
          <!--* Provider Email -->
          <label for="email" class="col-span-1 font-bold text-gray-500 text-md">
            Correo Electrónico
            <input
              readonly
              id="email"
              type="email"
              value={placeholderEmail}
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
              value={placeholderPhone}
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
              value={placeholderClient}
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
              value={placeholderClientEmail}
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
              value={placeholderClientPhone}
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
          Detalles del servicio
        </h1>
        <!--* Service Description -->
        <label
          for="agreement"
          class="text-lg font-semibold text-gray-500 text-start"
        >
          Descripción
          <div>
            <p class="text-xs md:text-sm">
              Detalles del servicio adquirido. Favor leer detenidamente cada
              punto.
            </p>
            <!--* Details input -->
            <div class="border-[1px] mt-4 -mb-1"></div>
            <ul class="h-auto pb-4 my-4 border-b-2">
              {#each bulletPoints as bulletPoint}
                <div class="flex justify-between mx-4">
                  <div class="flex gap-2 mt-1">
                    <i class="fa-solid fa-check mt-[5px] text-[#cc2936]"></i>
                    <li class="text-base text-md">{bulletPoint}</li>
                  </div>
                </div>
              {/each}
            </ul>
          </div>
        </label>
        <!--* Price and Date -->
        <div class="grid items-start grid-cols-1 gap-2 md:grid-cols-2">
          <div class="flex col-span-1">
            <label
              for="price"
              class="text-lg font-semibold text-gray-500 text-start"
            >
              Precio
              <!--* Price Input -->
              <div class="">
                <input
                  readonly
                  id="price"
                  type="text"
                  value="$100.00"
                  on:keypress={restrictToNumbersAndDecimal}
                  class="p-2 my-2 font-normal border-2 border-gray-300 rounded-md bg-slate-100 focus:outline-none focus:border-gray-300 focus:ring-0 placeholder:text-slate-300"
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
                  value={placeholderDate.month}
                  on:keypress={handleDateInput}
                  class="w-full p-2 my-2 font-normal border-2 border-gray-300 rounded-md bg-slate-100 focus:outline-none focus:border-gray-300 focus:ring-0 placeholder:text-slate-300"
                />
                <!--? Day -->
                <input
                  id="day"
                  type="text"
                  placeholder="DD"
                  readonly
                  value={placeholderDate.day}
                  on:keypress={handleDateInput}
                  class="w-full p-2 my-2 font-normal border-2 border-gray-300 rounded-md bg-slate-100 focus:outline-none focus:border-gray-300 focus:ring-0 placeholder:text-slate-300"
                />
                <!--? Year -->
                <input
                  id="year"
                  type="text"
                  placeholder="AAAA"
                  readonly
                  value={placeholderDate.year}
                  on:keypress={handleDateInput}
                  class="w-full p-2 my-2 font-normal border-2 border-gray-300 rounded-md bg-slate-100 focus:outline-none focus:border-gray-300 focus:ring-0 placeholder:text-slate-300"
                />
              </div>
            </label>
          </div>
        </div>
      </div>
      <!--* Signature and Agreement -->
      <div>
        <!--? Signature Input -->
        <label for="signature">
          <h1 class="text-lg font-semibold text-gray-500 text-start">
            Firma <span class="text-xs">(electrónica)</span>
          </h1>
          <input
            id="signature"
            type="text"
            class="w-full p-2 my-2 font-normal bg-white border-2 border-gray-300 rounded-md focus:outline-none focus:border-gray-300 focus:ring-0"
          />
        </label>
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
              <a
                href="/"
                class="no-underline hover:text-[#BB2532] hover:underline text-[#cc2936]"
                >términos y condiciones</a
              > de PalitasPR. De igual manera, me comprometo a cumplir con los acuerdos
              establecidos en este documento. Al someter este formulario, acepto
              que la información proporcionada es verídica y correcta y podría ser
              utilizada para fines de contacto y/o asuntos legales.
            </p>
          </label>
        </div>
      </div>
      <div>
        <!--* Submit button -->
        <button
          class="w-full p-2 mt-4 font-semibold text-white bg-[#cc2936] border-none btn hover:bg-[#BB2532] transition-all duration-150 ease-in-out"
          >Someter</button
        >
      </div>
    </div>
  </div>
</div>

<style></style>
