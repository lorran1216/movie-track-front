<script setup>
let texto='';
</script>

<template>
    <div class="fixed flex flex-row w-full p-2 bg-black/70">
      <input @input="$emit('search', texto )" type="text" v-model="texto" class=" bg-white rounded-md pl-1 py-0.5 w-full" placeholder="Pesquisar">
  </div>
</template>
