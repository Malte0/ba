<script setup lang="ts">
import { computed, ref } from 'vue';
import { regions } from '../cards/regions/regions';

const MIN_CARD_INDEX = 1;
const MAX_CARD_INDEX = 68;

const currentCardIndex = ref<number>(1);
const computedIndex = computed
    (() => {
        clampIndex(currentCardIndex.value);
        return currentCardIndex.value;
    })

function clampIndex(index: number) {
    currentCardIndex.value = Math.max(MIN_CARD_INDEX, Math.min(index, MAX_CARD_INDEX))
}

function onIndexInputChange(event: Event) {
    currentCardIndex.value = parseInt((event.target! as HTMLInputElement).value)
    console.log(currentCardIndex.value)
}

</script>

<template>
    <div class="card-inspector">
        <div class="card-display">
            <RegionCard :index="currentCardIndex"></RegionCard>
            <div class="card-info">
                <h2>Info:</h2>
                <p>Color: {{ regions[computedIndex].color }}</p>
                <p>{{ regions[computedIndex].night ? "Night" : "" }}</p>
                <p>{{ regions[computedIndex].map ? "Map" : "" }}</p>
                <p>Symbols: {{ regions[computedIndex].symbols?.join(", ") }}</p>
                <p>Condition: {{ regions[computedIndex].condition?.join(", ") }}</p>
                <p>Points: {{ regions[computedIndex].points }}</p>
                <p>Multiplier: {{ regions[computedIndex].multiplier }}</p>
            </div>
        </div>
        <div class="card-navigation">
            <button :class="{'button-inactive': currentCardIndex == MIN_CARD_INDEX }" class="card-navigation-button" @click="() => currentCardIndex--">prev</button>
            <input type="number" name="indexInput" id="indexInput" :value="computedIndex"
                @change="onIndexInputChange">
            <button :class="{'button-inactive': currentCardIndex == MAX_CARD_INDEX }" class="card-navigation-button" @click="() => currentCardIndex++">next</button>
        </div>
    </div>
</template>

<style scoped>
.card-info {
    margin-left: 2rem;
    font-weight: bold;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.card-navigation-button {
    user-select: none;
    padding: 0.5rem 1rem;
    margin: 0 0.5rem;
    border: none;
    border-radius: 0.25rem;
    background-color: #0969da;
    color: white;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.2s;
}

.button-inactive {
    background-color: hsl(213, 14%, 40%);
    cursor: default;
}

.card-inspector {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.card-display {
    margin: 2rem;
    display: flex;
    flex-direction: row;
}

.card-navigation {
    display: flex;
}
</style>
