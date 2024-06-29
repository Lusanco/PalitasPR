<script>
  import axios from "axios";

  let image = null;
  let fileInput;

  // Function to handle the file change event
  function handleFileChange(event) {
    image = event.target.files[0]; // Get the first file from the list
    console.log("Image file selected:", image);
  }

  // Function to handle the cancel button click event
  function handleCancel() {
    image = null;
    fileInput.value = null; // Reset the file input
  }

  // Function to handle the save button click event
  function handleSave() {
    if (image) {
      const formData = new FormData(); // Create a new FormData object
      formData.append("image", image);

      axios
        .post("YOUR_API_ENDPOINT", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          console.log("Image uploaded successfully:", response.data);
        })
        .catch((error) => {
          console.error("Error uploading image:", error);
        });
    }
  }
</script>

<!--* QR -->
<div class="flex items-center justify-center min-h-screen m-5 overflow-x-auto">
  <!--* Container -->
  <div class="w-full p-12 m-2 bg-white rounded-md md:m-20 card">
    <!--* Title -->
    <h1
      class="text-xl md:text-4xl text-center mb-8 md:mb-12 font-semibold text-[#1f1f1f]"
    >
      Sube tu QR de Ath Movil aquí
    </h1>
    <!-- {#if image === null} -->
    <!--* Image input -->
    <input
      type="file"
      name="image"
      id="imageInput"
      bind:this={fileInput}
      on:change={handleFileChange}
      class="w-full px-8 py-12 text-[#1f1f1f] bg-[#f1f1f1] border-2 border-[#cc2936] border-dashed rounded-md"
      accept="image/*"
    />
    <!--* Action buttons -->
    <div class="flex w-full gap-2 mt-4">
      <!--* Save button -->
      <button
        class="flex-1 px-4 py-2 text-lg btn"
        class:opacity-50={!image}
        class:pointer-events-none={!image}
        on:click={handleSave}
      >
        <i class="mt-1 text-lg fa-solid fa-check"></i> Save
      </button>
      <!--* Cancel button -->
      <button
        class="flex-1 px-4 py-2 text-lg btn"
        class:opacity-50={!image}
        class:pointer-events-none={!image}
        on:click={handleCancel}
      >
        <i class="mt-1 text-lg fa-solid fa-xmark"></i> Cancel
      </button>
    </div>
    <!-- {/if} -->
  </div>
</div>

<style></style>
