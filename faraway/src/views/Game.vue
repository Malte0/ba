<script setup lang="ts">
import { ref } from 'vue';
import { CardDeck, countMaps, getCardPoints } from '../cards/cards';
import RegionCard from '../components/RegionCard.vue';
import SanctuaryCard from '../components/SanctuaryCard.vue';
import { regions } from '../cards/regions/regions';
import { sanctuaries } from '../cards/sanctuaries/sanctuaries';
import type { CARD } from '../types';

const cardDeck = new CardDeck()
const randomRegions = ref<number[]>([cardDeck.drawRegion(), cardDeck.drawRegion(), cardDeck.drawRegion()]);
const chosenRegions = ref<number[]>([]);
const pointsRecieved = ref<number[]>([]);
const pointsFromSanctuaries = ref<number>(0);
const openSanctuaryOverlay = ref<boolean>(false);
const drawnSanctuaries = ref<number[]>([]);
const chosenSanctuaries = ref<number[]>([]);
const hideSanctuaryOverlay = ref<boolean>(false);

// refreshes the cards the player can choose from
function refreshCardChoice() {
    for (let i = 0; i < randomRegions.value.length; i++) {
        randomRegions.value[i] = cardDeck.drawRegion();
    }
}

function calculateScore(regionsToEvaluate: number[], sanctuariesToEvaluate: number[]) {
    regionsToEvaluate.reverse();
    let openCards: CARD[] = sanctuariesToEvaluate.map(sanctuaryIndex => sanctuaries[sanctuaryIndex]);
    for (const region of regionsToEvaluate) {
        const currentRegion = regions[region];
        openCards.push(currentRegion);
        const cardPoints = getCardPoints(openCards, currentRegion);
        pointsRecieved.value.push(cardPoints);
    }
    let sanctuaryPoints = 0;
    for (const sanctuary of sanctuariesToEvaluate) {
        const currentSanctuary = sanctuaries[sanctuary];
        const cardPoints = getCardPoints(openCards, currentSanctuary);
        sanctuaryPoints += cardPoints;
        console.log(sanctuaryPoints);
    }
    pointsFromSanctuaries.value = sanctuaryPoints;
}

// player chooses a card
function chooseCard(cardIndex: number) {
    console.log(`You have chosen card ${cardIndex}`)
    const previousCardIndex = chosenRegions.value[chosenRegions.value.length - 1]
    chosenRegions.value.push(cardIndex)
    if (chosenRegions.value.length > 1 && cardIndex > previousCardIndex) {
        openSanctuaryOverlay.value = true;
        drawSanctuaries();
    }
    if (chosenRegions.value.length == 8) {
        console.log("GAME OVER!!!!");
        randomRegions.value = [];
        // use copy of array, just to be sure
        calculateScore(chosenRegions.value.slice(), chosenSanctuaries.value.slice());
    }
    refreshCardChoice()
}

function drawSanctuaries() {
    const openRegions: CARD[] = chosenRegions.value.map(cardIndex => regions[cardIndex]);
    const openSanctuaries: CARD[] = chosenSanctuaries.value.map(cardIndex => regions[cardIndex]);
    const amountOfSanctuariesToDraw = countMaps(openRegions.concat(openSanctuaries)) + 1;
    drawnSanctuaries.value = cardDeck.drawSanctuaries(amountOfSanctuariesToDraw)
}

function takeSanctuary(sanctuaryIndex: number) {
    openSanctuaryOverlay.value = false;
    chosenSanctuaries.value.push(sanctuaryIndex)
    drawnSanctuaries.value = [];
    hideSanctuaryOverlay.value = false;
}

function toggleSanctuarySelectionVisibiltiy(event: PointerEvent) {
    event.stopPropagation()
    hideSanctuaryOverlay.value = !hideSanctuaryOverlay.value
    console.log(hideSanctuaryOverlay.value)
}

const chosenCardSize = 240;
</script>

<template>
    <div class="game-container">
        <div class="game-cards-to-choose">
            <div v-for="cardIndex in randomRegions" @click="() => chooseCard(cardIndex)"
                class="game-card-region-wrapper"
                :style="{ width: `${chosenCardSize}px`, height: `${chosenCardSize}px` }">
                <RegionCard :width="chosenCardSize" :index="cardIndex"></RegionCard>
            </div>
        </div>
        <div class="game-cards-chosen">
            <div v-for="cardIndex in chosenRegions" class="game-card-region-wrapper"
                :style="{ width: `${chosenCardSize}px`, height: `${chosenCardSize}px` }">
                <RegionCard :width="chosenCardSize" :index="cardIndex"></RegionCard>
            </div>
        </div>
        <div class="game-cards-chosen">
            <div v-for="cardIndex in chosenSanctuaries" class="game-sanctuary-card-wrapper">
                <SanctuaryCard :width="189" :index="cardIndex"></SanctuaryCard>
            </div>
        </div>
        <div v-if="openSanctuaryOverlay" class="game-sanctuary-overlay">
            <div @click="() => hideSanctuaryOverlay = false" class="game-sanctuary-choice-wrapper" :class="{ 'game-sanctuary-choice-hidden': hideSanctuaryOverlay }">
                <div v-for="cardIndex in drawnSanctuaries" @click="() => takeSanctuary(cardIndex)"
                    class="game-sanctuary-card-wrapper">
                    <SanctuaryCard :width="189" :index="cardIndex"></SanctuaryCard>
                </div>
            </div>
            <div class="game-sanctuary-choice-visility">
                <div class="game-eye-button">
                    <img v-if="!hideSanctuaryOverlay" @click="toggleSanctuarySelectionVisibiltiy"
                        src="/img/visibility_off.svg" alt="-_-">
                    <img v-if="hideSanctuaryOverlay" @click="toggleSanctuarySelectionVisibiltiy"
                        src="/img/visibility_on.svg" alt="o_o">
                </div>
            </div>
        </div>
        <div>
            <div v-for="points, index in pointsRecieved" class="game-points">Card {{ 8 - index }}: {{ points }}</div>
            <div v-if="pointsRecieved.length > 0" class="game-points">Sanctuaries: {{ pointsFromSanctuaries }}</div>
            <div v-if="pointsRecieved.length > 0">Total: {{pointsRecieved.reduce((prev, curr) => prev + curr, 0)}}</div>
        </div>
    </div>
</template>

<style scoped>
.game-eye-button {
    pointer-events: all;
    user-select: none;
    cursor: pointer;
    position: absolute;
    top: 2.5rem;
    right: 3.5rem;
    width: 4rem;
    height: 2rem;
    border: 1px solid #e3e3e3;
    border-radius: 0.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: transparent;
}

.game-eye-button:hover {
    background-color: rgba(255, 255, 255, 0.103);
}

.game-sanctuary-choice-visility {
    pointer-events: none;
    cursor: default;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
}

.game-sanctuary-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
}

.game-sanctuary-choice-wrapper {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.171);
    backdrop-filter: blur(5px);
    display: flex;
    justify-content: center;
    align-items: center;
}

.game-sanctuary-choice-wrapper>div {
    cursor: pointer;
}

.game-sanctuary-choice-hidden {
    opacity: 0;
}

.game-cards-to-choose {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    padding: 1rem;
}

.game-cards-to-choose>div {
    cursor: pointer;
}

.game-cards-chosen {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    padding: 1rem;
    flex-wrap: wrap;
}

.game-card-region-wrapper {
    margin: 0.5rem;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
