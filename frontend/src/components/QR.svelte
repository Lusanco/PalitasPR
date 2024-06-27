<script>
  let image = "";

  function handleFileChange(event) {
    image = event.target.files[0];
    console.log("Image file selected:", event.target.files[0]);
  }
</script>

<div class="flex items-center justify-center min-h-screen m-5 overflow-x-auto">
  <div class="w-full p-12 m-2 bg-white rounded-md md:m-20 card">
    <label for="imageInput" class="w-full mb-2">
      Subir imagen
      <input
        type="file"
        name="image"
        id="imageInput"
        on:change={handleFileChange}
        class="w-full px-8 py-12 text-[#1f1f1f] bg-[#f1f1f1] border-2 border-[#cc2936] border-dashed rounded-md"
        accept="image/*"
      /></label
    >
    <div class="flex w-full gap-2 mt-4">
      <button class="flex-1 text-lg btn"
        ><i class="mt-1 text-lg fa-solid fa-check"></i> Save</button
      >
      <button class="flex-1 text-lg btn"
        ><i class="mt-1 text-lg fa-solid fa-xmark"></i> Cancel</button
      >
    </div>
  </div>
</div>

<style></style>
