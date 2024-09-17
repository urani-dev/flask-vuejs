<script setup lang="ts">
import { ref } from "vue";

defineProps({
  msg: String,
});

const count = ref(0);
const isProcessing = ref(false);

const incrementCount = () => {
  isProcessing.value = true;
  fetch(`/increment/${count.value}`)
    .then((response) => {
      if (response.ok) {
        return response.text();
      } else {
        console.error(`${response.status} ${response.statusText}`);
        isProcessing.value = false;
      }
    })
    .then((val: any) => {
      count.value = parseInt(val);
      isProcessing.value = false;
    })
    .catch((error) => {
      console.error(`Error: ${error.message}`);
      isProcessing.value = false;
    });
};
</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <button type="button" :disabled="isProcessing" @click="incrementCount">
      Count {{ count }}
    </button>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test HMR
    </p>
  </div>

  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
      >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Install
    <a href="https://github.com/johnsoncodehk/volar" target="_blank">Volar</a>
    in your IDE for a better DX
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
