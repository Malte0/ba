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

const chosenRegions = ref<number[]>([]);
const pointsRecieved = ref<{ [key: number]: number }>([]);
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
        pointsRecieved.value[region] = cardPoints;
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

function endGame() {
    console.log("GAME OVER!!!!");
    publicRegions.value = [];
    // use copy of array, just to be sure
    calculateScore(chosenRegions.value.slice(), chosenSanctuaries.value.slice());
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
        endGame();
        return;
    }
    // remove card from hand
    handCards.value = handCards.value.filter(card => card !== cardIndex);
}

function drawSanctuaries() {
    const openRegions: CARD[] = chosenRegions.value.map(cardIndex => regions[cardIndex]);
    const openSanctuaries: CARD[] = chosenSanctuaries.value.map(cardIndex => sanctuaries[cardIndex]);
    console.log(openRegions)
    console.log(openSanctuaries)
    const amountOfSanctuariesToDraw = countMaps(openRegions.concat(openSanctuaries)) + 1;
    drawnSanctuaries.value = cardDeck.drawSanctuaries(amountOfSanctuariesToDraw)
}

function takeSanctuary(sanctuaryIndex: number) {
    openSanctuaryOverlay.value = false;
    chosenSanctuaries.value.push(sanctuaryIndex)
    drawnSanctuaries.value = [];
    hideSanctuaryOverlay.value = false;
    if (chosenRegions.value.length == 8) {
        endGame();
    }
}

function toggleSanctuarySelectionVisibiltiy(event: PointerEvent) {
    event.stopPropagation()
    hideSanctuaryOverlay.value = !hideSanctuaryOverlay.value
}

const cardSize = computed(() => chosenRegions.value.length < 5 ? window.innerHeight / 5 : window.innerHeight / 5)
</script>

<template>
    <div class="game-container">
        <!-- TODO: put points beneath the cards and total points below all the cards -->
        <div class="game-final-scores">
            <div v-if="chosenRegions.length === 8">Total Points: {{Object.values(pointsRecieved).reduce((prev, curr) =>
                prev + curr,
                0) + pointsFromSanctuaries}}</div>
        </div>
        <!-- Don't show public cards if there is only one card left to play -->
        <div v-if="chosenRegions.length < 8" class="game-cards-to-choose">
            <div class="game-hint">
                <h1>Public</h1>
                <!-- <img src="/img/public_cards.svg" alt="public"> -->
            </div>
            <div class="game-card-wrapper">
                <div v-for="cardIndex in publicRegions" @click="() => takePublicCard(cardIndex)"
                    class="game-card-region-wrapper" :class="{ 'game-card-pickable': handCards.length < 3 }"
                    :style="{ width: `${cardSize}px`, height: `${cardSize}px` }">
                    <RegionCard :width="cardSize" :index="cardIndex"></RegionCard>
                </div>
            </div>
            <!-- Mirror hint to put cards in the middle -->
            <div class="game-hint" style="opacity: 0;">
                <h1>Public</h1>
            </div>
        </div>
        <div style="height: 0.25rem; width: 100%; background-color: #e3e3e3;"></div>
        <div class="game-cards-in-hand">
            <div class="game-hint">
                <h1>Hand</h1>
                <!-- <img src="/img/hand_cards.svg" alt="public"> -->
            </div>
            <div class="game-card-wrapper">
                <div v-for="cardIndex in handCards" @click="() => playHandCard(cardIndex)"
                    class="game-card-region-wrapper" :class="{ 'game-card-pickable': handCards.length === 3 }"
                    :style="{ width: `${cardSize}px`, height: `${cardSize}px` }">
                    <RegionCard :width="cardSize" :index="cardIndex"></RegionCard>
                </div>
            </div>
            <div class="game-hint" style="opacity: 0;">
                <h1>Hand</h1>
            </div>
        </div>
        <div class="game-cards-chosen">
            <div class="game-hint">
                <h1>Explored</h1>
            </div>
            <div class="game-region-cards-chosen" :style="{ width: `calc(4px * (${cardSize} + 0.5rem))` }">
                <div v-for="cardIndex in chosenRegions">
                    <div class="game-card-region-wrapper" :style="{ width: `${cardSize}px`, height: `${cardSize}px` }">
                        <RegionCard :width="cardSize" :index="cardIndex"></RegionCard>
                    </div>
                    <!-- TODO: Life Punkteanzeige / not fullfilled -->
                    <p v-if="chosenRegions.length === 8">points: {{ pointsRecieved[cardIndex] }}</p>
                </div>
            </div>
            <div class="game-region-cards-chosen">
                <div v-for="cardIndex in chosenSanctuaries" class="game-sanctuary-card-wrapper"
                    :style="{ width: `${cardSize * (3 / 5)}px`, height: `${cardSize}px` }">
                    <SanctuaryCard :width="cardSize * (3 / 5)" :index="cardIndex"></SanctuaryCard>
                </div>
                <div v-if="chosenRegions.length === 8" class="game-points">Sanctuaries: {{ pointsFromSanctuaries }}
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
                <h1 v-if="!hideSanctuaryOverlay" style="color: #ffffff;">Choose Sanctuary</h1>
                <div class="game-eye-button" @click="toggleSanctuarySelectionVisibiltiy">
                    <img v-if="!hideSanctuaryOverlay" src="/img/visibility_off.svg" alt="-_-">
                    <img v-if="hideSanctuaryOverlay" src="/img/visibility_on.svg" alt="o_o">
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.game-cards-to-choose {
    min-height: fit-content;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 0.75rem;
    background-color: #2F2F2F;
}

.game-card-wrapper {
    display: flex;
    flex-direction: row;
    justify-content: center;
    justify-self: center;
}

.game-hint {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    font-weight: 500;
    color: #e3e3e3;
}

.game-hint>h1 {
    margin: 0.5rem 0 1rem 0;
}

.game-hint>img {
    height: 80px;
}

.game-sanctuary-card-wrapper {
    margin: 0 0.5rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.game-card-region-wrapper {
    cursor: default;
    pointer-events: none;
    margin: 0.5rem;
    display: flex;
    flex-direction: column;
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
    min-height: fit-content;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 0.75rem;
    background-color: #414141;
}

.game-cards-in-hand>div {
    cursor: pointer;
}

.game-cards-chosen {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    background-color: #555555;
    padding: 0.75rem;
}

.game-region-cards-chosen {
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    flex-wrap: wrap;
}

.game-final-scores {
    color: white;
    padding: 1rem;
    font-size: 2rem;
    min-height: fit-content;
    line-height: 2.5rem;
}
</style>
