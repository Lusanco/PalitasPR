<script>
  import UploadImage from "./UploadImage.svelte";
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
      <input class="w-full" type="text" name="titulo" id="" />
    </div>
    <div class="">
      <label for="service">Tipo de Servicio</label>
      <input class="w-full" type="text" name="service" />
    </div>
    <div class="max-h-96">
      <label for="description">Descripcion de su Oferta</label>

      <textarea class="w-full min-h-20 max-h-20" name="description" id=""
      ></textarea>
    </div>
    <div>
      <label for="price-min">Precio Minimo (Opcional)</label>
      <input class="w-full" type="number" name="price-min" id="" />
    </div>
    <div>
      <label for="price-max">Precio Maximo (Opcional)</label>
      <input class="w-full" type="number" name="price-max" id="" />
    </div>
    <div>
      <label for="imageInput">Subir Imagenes (Opcional)</label>
      <UploadImage></UploadImage>
    </div>
    <button
      type="button"
      class="w-full px-8 py-3 font-semibold bg-teal-600 rounded-md text-teal-50"
      >Crear</button
    >
  </div>
</div>
