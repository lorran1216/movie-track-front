<template>
    <div class="container rounded-xl">
        <img :src="cover" class="w-20 h-20 rounded-s-xl" />
        <div class="flex flex-col space-y-5 max-h-[112px]">
            <p class="text-sm font-bold">{{ title }}</p>
            <p class="text-xs">{{ duration }} Min</p>
        </div>
    </div>
</template>


<script setup>

//todo: truncate text with computed

defineProps({
    title: {
        type: String,
        default: "Mock Title"
    },
    duration: Number,
    cover: String
})

/*flex flex-row w-full gap-2 bg-[#EBF8F8] rounded-xl overflow-hidden*/ 
</script>

<style scoped>
    .container{
        display:flex;
        flex-direction: row;
        width: 250px;
        background-color: #EBF8F8;
        border-radius: 5px;
    }
</style>