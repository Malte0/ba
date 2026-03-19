<script setup lang="ts">
import { ref } from 'vue';
import { CardDeck, getCardPoints } from '../cards/cards';
import RegionCard from '../components/RegionCard.vue';
import { regions } from '../cards/regions/regions';
import type { REGION_CARD } from '../types';

const cardDeck = new CardDeck()
const randomCards = ref<number[]>([cardDeck.drawRegion(), cardDeck.drawRegion(), cardDeck.drawRegion()]);
const chosenCards = ref<number[]>([]);
const pointsRecieved = ref<number[]>([])

// refreshes the cards the player can choose from
function refreshCardChoice() {
    for (let i = 0; i < randomCards.value.length; i++) {
        randomCards.value[i] = cardDeck.drawRegion();
    }
}

function calculateScore(cardsToEvaluate: number[]) {
    cardsToEvaluate.reverse();
    let openCards: REGION_CARD[] = [];
    for (const card of cardsToEvaluate) {
        const currentCard = regions[card];
        openCards.push(currentCard);
        const cardPoints = getCardPoints(openCards, currentCard);
        pointsRecieved.value.push(cardPoints);
    }
}

// player chooses a card
function chooseCard(cardIndex: number) {
    console.log(`You have chosen card ${cardIndex}`)
    chosenCards.value.push(cardIndex)
    if (chosenCards.value.length == 8) {
        console.log("GAME OVER!!!!");
        randomCards.value = [];
        // use copy of array, just to be sure
        calculateScore(chosenCards.value.slice());
    }
    refreshCardChoice()
}

const chosenCardSize = 240;
</script>

<template>
    <div class="game-container">
        <div class="game-cards-to-choose">
            <div v-for="cardIndex in randomCards" @click="() => chooseCard(cardIndex)" class="game-card-wrapper" :style="{width: `${chosenCardSize}px`, height: `${chosenCardSize}px`}">
                <RegionCard :width="chosenCardSize" :index="cardIndex"></RegionCard>
            </div>
        </div>
        <div class="game-cards-chosen">
            <div v-for="cardIndex in chosenCards" class="game-card-wrapper" :style="{width: `${chosenCardSize}px`, height: `${chosenCardSize}px`}">
                <RegionCard :width="chosenCardSize" :index="cardIndex"></RegionCard>
            </div>
        </div>
        <div>
            <div v-for="points, index in pointsRecieved" class="game-points">Card {{ 8-index }}: {{ points }}</div>
            <div v-if="pointsRecieved.length > 0">Total: {{ pointsRecieved.reduce((prev, curr) => prev+curr, 0) }}</div>
        </div>
    </div>
</template>

<style scoped>
.game-cards-to-choose {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    padding: 1rem;
}

.game-cards-to-choose > div {
    cursor: pointer;
}

.game-cards-chosen {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    padding: 1rem;
    flex-wrap: wrap;
}

.game-card-wrapper {
    margin: 0.5rem;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
