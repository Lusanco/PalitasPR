<script>
  import axios from "axios";

  let imageFile;
  let errorMessage;

  async function handleUpload() {
    if (!imageFile) {
      errorMessage = "Please select an image file";
      return;
    }

    const formData = new FormData();
    formData.append("image", imageFile);

    try {
      const response = await axios.post("/upload-image", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      console.log("Image uploaded successfully:", response.data);
    } catch (error) {
      console.error("Error uploading image:", error);
      errorMessage = "An error occurred while uploading the image";
    }
  }
</script>

<div class="flex flex-col min-h-screen">
  <div
    class="flex flex-col items-center justify-center w-full h-full min-h-screen m-auto space-y-1 text-gray-800"
  >
    <label for="imageInput" class="block text-sm font-medium">Attachments</label
    >
    <div class="flex">
      <input
        type="file"
        name="image"
        id="imageInput"
        bind:files={imageFile}
        class="px-8 py-12 text-gray-600 bg-gray-100 border-2 border-gray-300 border-dashed rounded-md"
        accept="image/*"
      />
      <button
        class="px-8 py-12 bg-teal-800 border-2 border-gray-300 rounded-md shadow-lg text-teal-50"
        on:click={handleUpload}
      >
        Upload
      </button>
    </div>
    {#if errorMessage}
      <p class="text-red-500">{errorMessage}</p>
    {/if}
  </div>
</div>
