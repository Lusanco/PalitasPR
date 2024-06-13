<script>
  export let showModal = false;
  export let onClose;

  function closeModal() {
    onClose();
  }
</script>

{#if showModal}
  <div class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
    <div class="w-10/12 p-6 bg-white rounded-lg shadow-lg md:w-1/2">
      <h2 class="mb-4 text-xl font-bold">Autorización de Contacto</h2>
      <p class="mb-4">Al aceptar, usted autoriza proporcionar sus datos de contacto y ser contactado por el dueño del post.</p>
      <div class="flex justify-end">
        <button class="mr-2 btn bg-stone-200" on:click={closeModal}>Cancelar</button>
        <button class="mr-2 btn bg-stone-200" on:click={closeModal}>Aceptar</button>
      </div>
    </div>
  </div>
{/if}
