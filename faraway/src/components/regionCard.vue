<script setup lang="ts">
const props = defineProps<{
    count: number,
    color: string,
}>()

</script>

<template>
    <div class="region-card">
        <div class="region-card-count">{{ count }}</div>
    </div>
</template>

<style scoped>
.region-card {
    height: 400px;
    width: 400px;
    aspect-ratio: 1;
    border-radius: 1rem;
    background-color: red;
    display: flex;
    flex-direction: column;
    align-items: start;
}

.region-card-count {
    position: relative;
    top: 0;
    left: 0;
    color: white;
    padding: 1rem;
    font-size: 2rem;
}
</style>
