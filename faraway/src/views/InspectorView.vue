<script setup lang="ts">
import { computed, ref } from 'vue';
import { regions } from '../cards/regions/regions';
import SanctuaryCard from '../components/SanctuaryCard.vue';
import RegionCard from '../components/RegionCard.vue';
import { sanctuaries } from '../cards/sanctuaries/sanctuaries';

const MIN_CARD_INDEX = 1;
const MAX_REGION_INDEX = 68;
const MAX_SANCTUARY_INDEX = 45;

const currentRegionIndex = ref<number>(1);
const computedRegionIndex = computed
    (() => {
        currentRegionIndex.value = clampIndex(currentRegionIndex.value, MAX_REGION_INDEX);
        return currentRegionIndex.value;
    })
const currentSanctuaryIndex = ref<number>(1);
const computedSanctuaryIndex = computed
    (() => {
        currentSanctuaryIndex.value = clampIndex(currentSanctuaryIndex.value, MAX_SANCTUARY_INDEX);
        return currentSanctuaryIndex.value;
    })

function clampIndex(index: number, maxIndex: number) {
    const newIndex = Math.max(MIN_CARD_INDEX, Math.min(index, maxIndex))
    return newIndex;
}

function onRegionIndexInputChange(event: Event) {
    currentRegionIndex.value = parseInt((event.target! as HTMLInputElement).value)
    console.log(currentRegionIndex.value)
}

function onSanctuaryIndexInputChange(event: Event) {
    currentSanctuaryIndex.value = parseInt((event.target! as HTMLInputElement).value)
    console.log(currentSanctuaryIndex.value)
}

</script>

<template>
    <div class="card-inspector">
        <div class="card-display">
            <RegionCard :index="currentRegionIndex" :width="300"></RegionCard>
            <div class="card-info">
                <h2>Info:</h2>
                <p>Color: {{ regions[computedRegionIndex].color }}</p>
                <p>{{ regions[computedRegionIndex].night ? "Night" : "" }}</p>
                <p>{{ regions[computedRegionIndex].map ? "Map" : "" }}</p>
                <p>Symbols: {{ regions[computedRegionIndex].symbols?.join(", ") }}</p>
                <p>Condition: {{ regions[computedRegionIndex].condition?.join(", ") }}</p>
                <p>Points: {{ regions[computedRegionIndex].points }}</p>
                <p>Multiplier: {{ regions[computedRegionIndex].multiplier }}</p>
            </div>
        </div>
        <div class="card-navigation">
            <button :class="{ 'button-inactive': currentRegionIndex == MIN_CARD_INDEX }" class="card-navigation-button"
                @click="() => currentRegionIndex--">prev</button>
            <input type="number" name="regionIndexInput" id="regionIndexInput" :value="computedRegionIndex" @change="onRegionIndexInputChange">
            <button :class="{ 'button-inactive': currentRegionIndex == MAX_REGION_INDEX }" class="card-navigation-button"
                @click="() => currentRegionIndex++">next</button>
        </div>
        <div class="card-display">
            <SanctuaryCard :index="currentSanctuaryIndex" :width="200"></SanctuaryCard>
            <div class="card-info">
                <h2>Info:</h2>
                <p>Color: {{ sanctuaries[computedSanctuaryIndex].color }}</p>
                <p>{{ sanctuaries[computedSanctuaryIndex].night ? "Night" : "" }}</p>
                <p>{{ sanctuaries[computedSanctuaryIndex].map ? "Map" : "" }}</p>
                <p>Symbols: {{ sanctuaries[computedSanctuaryIndex].symbols?.join(", ") }}</p>
                <p>Points: {{ sanctuaries[computedSanctuaryIndex].points }}</p>
                <p>Multiplier: {{ sanctuaries[computedSanctuaryIndex].multiplier }}</p>
            </div>
        </div>
        <div class="card-navigation">
            <button :class="{ 'button-inactive': currentSanctuaryIndex == MIN_CARD_INDEX }" class="card-navigation-button"
                @click="() => currentSanctuaryIndex--">prev</button>
            <input type="number" name="regionIndexInput" id="regionIndexInput" :value="computedSanctuaryIndex" @change="onSanctuaryIndexInputChange">
            <button :class="{ 'button-inactive': currentSanctuaryIndex == MAX_SANCTUARY_INDEX }" class="card-navigation-button"
                @click="() => currentSanctuaryIndex++">next</button>
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
    width: 600px
}

.card-navigation {
    display: flex;
}
</style>
