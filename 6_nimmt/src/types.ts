
export type Card = {
    value: number;
    points: number;
}

export type Strategy = {
    name: string,
    description: string,
    cardToPlay: (handCards: Card[], cardsOnBoard: Card[][], cardsLeft: number[], numberOfPlayers: number) => number
}