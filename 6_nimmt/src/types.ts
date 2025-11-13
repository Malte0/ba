
export type Card = {
    value: number;
    points: number;
}

export type Strategy = {
    name: string,
    description: string,
    cardToPlay: (handCards: Card[]) => number
}