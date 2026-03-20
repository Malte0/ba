<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
    index: number,
    width: number
}>()

// offset for the background image
const backgroundOffsetY = computed(() => {
    const newOffset = "-"+(Math.floor(props.index / 10) * 100).toString() + "%";
    return newOffset;
}
);
const backgroundOffsetX = computed(() => {
    const newOffset = "-"+((props.index % 10) * 100).toString() + "%";
    return newOffset;
});
</script>

<template>
    <div :style="{ backgroundPositionX: backgroundOffsetX, backgroundPositionY: backgroundOffsetY, scale: `${width / 189}` }"
        class="sanctuary-card">
    </div>
</template>

<style scoped>
.sanctuary-card {
    background-image: url(/img/card_sanctuary.webp);
    user-select: none;
    height: 291px;
    width: 189px;
    aspect-ratio: 1.5396825; 
    border-radius: 1.25rem;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}
</style>
