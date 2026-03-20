<script setup lang="ts">
import { computed, ref } from 'vue';
import { CardDeck, countMaps, getCardPoints } from '../cards/cards';
import RegionCard from '../components/RegionCard.vue';
import SanctuaryCard from '../components/SanctuaryCard.vue';
import { regions } from '../cards/regions/regions';
import { sanctuaries } from '../cards/sanctuaries/sanctuaries';
import type { CARD } from '../types';

const cardDeck = new CardDeck()
const publicRegions = ref<number[]>([cardDeck.drawRegion(), cardDeck.drawRegion(), cardDeck.drawRegion()]);
const handCards = ref<number[]>([cardDeck.drawRegion(), cardDeck.drawRegion(), cardDeck.drawRegion()])

const chosenRegions = ref<number[]>([5, 6, 7, 8]);
const pointsRecieved = ref<number[]>([]);
const pointsFromSanctuaries = ref<number>(0);
const openSanctuaryOverlay = ref<boolean>(false);
const drawnSanctuaries = ref<number[]>([]);
const chosenSanctuaries = ref<number[]>([]);
const hideSanctuaryOverlay = ref<boolean>(false);

// refreshes the cards the public cards
function refreshCardChoice() {
    for (let i = 0; i < publicRegions.value.length; i++) {
        publicRegions.value[i] = cardDeck.drawRegion();
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
function takePublicCard(cardIndex: number) {
    console.log(`You have chosen public card ${cardIndex}`)
    handCards.value.push(cardIndex);
    refreshCardChoice()
}

function playHandCard(cardIndex: number) {
    console.log(`You have played hand card ${cardIndex}`)
    const previousCardIndex = chosenRegions.value[chosenRegions.value.length - 1]
    chosenRegions.value.push(cardIndex)
    if (chosenRegions.value.length > 1 && cardIndex > previousCardIndex) {
        openSanctuaryOverlay.value = true;
        drawSanctuaries();
    }
    if (chosenRegions.value.length == 8) {
        console.log("GAME OVER!!!!");
        publicRegions.value = [];
        // use copy of array, just to be sure
        calculateScore(chosenRegions.value.slice(), chosenSanctuaries.value.slice());
        return;
    }
    // remove card from hand
    handCards.value = handCards.value.filter(card => card !== cardIndex);
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

const cardSize = computed(() => chosenRegions.value.length < 5 ? window.innerHeight / 5 : window.innerHeight / 5)
</script>

<template>
    <div class="game-container">
        <!-- TODO: put points beneath the cards and total points below all the cards -->
        <div class="game-final-scores">
            <div v-for="points, index in pointsRecieved" class="game-points">Card {{ 8 - index }}: {{ points }}</div>
            <div v-if="pointsRecieved.length > 0" class="game-points">Sanctuaries: {{ pointsFromSanctuaries }}</div>
            <dpiv v-if="pointsRecieved.length > 0">Total: {{pointsRecieved.reduce((prev, curr) => prev + curr,
                0) + pointsFromSanctuaries}}</dpiv>
        </div>
        <div v-if="publicRegions.length > 0" class="game-cards-to-choose">
            <div class="game-cards-hint">
                <h1>Public</h1>
                <img src="/img/public_cards.svg" alt="public">
            </div>
            <div v-for="cardIndex in publicRegions" @click="() => takePublicCard(cardIndex)"
                class="game-card-region-wrapper" :class="{ 'game-card-pickable': handCards.length < 3 }"
                :style="{ width: `${cardSize}px`, height: `${cardSize}px` }">
                <RegionCard :width="cardSize" :index="cardIndex"></RegionCard>
            </div>
            <div class="game-cards-hint">
            </div>
        </div>
        <div style="height: 0.5rem; width: 100%; background-color: #e3e3e3;"></div>
        <div class="game-cards-in-hand">
            <div class="game-cards-hint">
                <h1>Hand</h1>
                <img src="/img/hand_cards.svg" alt="public">
            </div>
            <div v-for="cardIndex in handCards" @click="() => playHandCard(cardIndex)" class="game-card-region-wrapper"
                :class="{ 'game-card-pickable': handCards.length === 3 }"
                :style="{ width: `${cardSize}px`, height: `${cardSize}px` }">
                <RegionCard :width="cardSize" :index="cardIndex"></RegionCard>
            </div>
            <div class="game-cards-hint">
            </div>
        </div>
        <div class="game-cards-chosen">
            <div class="game-cards-hint">
                <h1>Explored</h1>
            </div>
            <div class="game-region-cards-chosen">
                <div v-for="cardIndex in chosenRegions" class="game-card-region-wrapper"
                    :style="{ width: `${cardSize}px`, height: `${cardSize}px` }">
                    <RegionCard :width="cardSize" :index="cardIndex"></RegionCard>
                </div>
            </div>
            <div class="game-region-cards-chosen">

                <div v-for="cardIndex in chosenSanctuaries" class="game-sanctuary-card-wrapper"
                    :style="{ width: `${cardSize}px`, height: `${cardSize}px` }">
                    <SanctuaryCard :width="cardSize" :index="cardIndex"></SanctuaryCard>
                </div>
            </div>
        </div>
        <div v-if="openSanctuaryOverlay" class="game-sanctuary-overlay">
            <div @click="() => hideSanctuaryOverlay = false" class="game-sanctuary-choice-wrapper"
                :class="{ 'game-sanctuary-choice-hidden': hideSanctuaryOverlay }">
                <div v-for="cardIndex in drawnSanctuaries" @click="() => takeSanctuary(cardIndex)"
                    class="game-sanctuary-card-wrapper">
                    <SanctuaryCard :width="189" :index="cardIndex"></SanctuaryCard>
                </div>
            </div>
            <div class="game-sanctuary-choice-visility">
                <h1 v-if="!hideSanctuaryOverlay" style="color: #ffffff; position: relative; top: 2rem">Choose Sanctuary
                </h1>
                <div class="game-eye-button">
                    <img v-if="!hideSanctuaryOverlay" @click="toggleSanctuarySelectionVisibiltiy"
                        src="/img/visibility_off.svg" alt="-_-">
                    <img v-if="hideSanctuaryOverlay" @click="toggleSanctuarySelectionVisibiltiy"
                        src="/img/visibility_on.svg" alt="o_o">
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.game-points {
    line-height: 1.25rem;
}

.game-sanctuary-card-wrapper {
    margin: 0.5rem;
}

.game-cards-hint {
    align-self: flex-start;
    justify-self: flex-start;
    height: 100%;
    width: 16%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    font-weight: 500;
    color: #e3e3e3;
}

.game-cards-hint>img {
    height: 40%;
}

.game-card-region-wrapper {
    cursor: default;
    pointer-events: none;
    margin: 0.5rem;
    display: flex;
    justify-content: center;
    align-items: center;
}

.game-card-pickable {
    cursor: pointer;
    pointer-events: all;
}

.game-container {
    height: 100vh;
    background-color: #555555;
}

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
    background-color: rgba(0, 0, 0, 0.5);
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

.game-cards-in-hand {
    height: 20%;
    min-height: fit-content;
    display: flex;
    flex-direction: row;
    justify-content: center;
    padding: 1rem;
    background-color: #414141;
}

.game-cards-to-choose {
    height: 20%;
    min-height: fit-content;
    display: flex;
    flex-direction: row;
    justify-content: center;
    padding: 1rem;
    background-color: #2F2F2F;
}

.game-cards-in-hand>div {
    cursor: pointer;
}

.game-cards-chosen {
    display: flex;
    flex-direction: row;
    justify-content: center;
    background-color: #555555;
}

.game-region-cards-chosen {
    display: flex;
    flex-direction: row;
    justify-content: center;
    padding: 1rem;
    flex-wrap: wrap;
}
</style>
