<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
    index: number,
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
    <div :style="{ backgroundPositionX: backgroundOffsetX, backgroundPositionY: backgroundOffsetY }"
        class="region-card">
    </div>
</template>

<style scoped>
.region-card {
    background-image: url(/img/card_region.webp);
    user-select: none;
    height: 300px;
    width: 300px;
    aspect-ratio: 1;
    border-radius: 1.25rem;
}
</style>
