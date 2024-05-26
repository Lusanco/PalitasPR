<script>
  import townsID from "../townsID";
  import servicesID from "../servicesID";
  import Button from "./Button.svelte";

  // Data points for axiosDATA
  let model = "Promotion",
    title,
    town,
    service_id,
    description,
    price_min,
    price_max;

  // For iterating town and service name and ids
  const towns = Object.entries(townsID);
  const services = Object.entries(servicesID);

  let buttonName = "Create Promotion";
  let locationURL = "/api/dashboard/promotion-request";
  let crudVERB = "POST";

  let axiosDATA = {
    model,
    title,
    town,
    service_id,
    description,
    price_min,
    price_max,
  };
</script>

<div
  class="flex flex-col items-center justify-center h-full min-h-screen bg-teal-50 md:bg-none"
>
  <div
    class="w-full h-full max-w-2xl p-2 font-semibold rounded-lg md:shadow-lg md:p-8 bg-teal-50"
  >
    <h1 class="pt-4 text-2xl text-center md:text-3xl lg:text-4xl">
      Crear Oferta de Servicio
    </h1>
    <!-- Crear Solicitud de Servicio -->
    <div class="">
      <label for="title">Titulo de su Oferta</label>
      <input
        class="w-full"
        type="text"
        name="titulo"
        id=""
        bind:value={axiosDATA.title}
      />
    </div>

    <!-- Service Filter Start -->
    <label for="service">Seleccione Servicio a Brindar</label>
    <select
      bind:value={axiosDATA.service_id}
      name="service"
      class="block w-full overflow-y-auto border-slate-600 border-1 focus:border-teal-500 focus:ring-0 disabled:cursor-not-allowed"
    >
      <option value="">---</option>
      {#each services as [service, id]}
        <option value={id}>{service}</option>
      {/each}
    </select>
    <!-- Service Filter End -->

    <!-- Town Filter Start -->
    <label for="town">Seleccione un Pueblo</label>
    <select
      bind:value={axiosDATA.town}
      name="town"
      class="block w-full overflow-y-auto border-slate-600 border-1 focus:border-teal-500 focus:ring-0 disabled:cursor-not-allowed"
    >
      <option value="0">---</option>
      {#each towns as [town, id]}
        <option value={id}>{town}</option>
      {/each}
    </select>
    <!-- Town Filter End -->
    <div class="max-h-96">
      <label for="description">Descripcion de su Oferta</label>
      <textarea
        bind:value={axiosDATA.description}
        class="w-full min-h-20 max-h-20"
        name="description"
        id=""
      ></textarea>
    </div>
    <div>
      <label for="price-min">Precio Minimo (Opcional)</label>
      <input
        class="w-full"
        type="number"
        name="price-min"
        id=""
        bind:value={axiosDATA.price_min}
      />
    </div>
    <div>
      <label for="price-max">Precio Maximo (Opcional)</label>
      <input
        class="w-full"
        type="number"
        name="price-max"
        id=""
        bind:value={axiosDATA.price_max}
      />
    </div>

    <Button {buttonName} {crudVERB} {locationURL} {axiosDATA}></Button>
  </div>
</div>
