
export type SYMBOL = "Distel" | "Stein" | "Schimaere"
export type COLOR = "red" | "blue" | "yellow" | "green" | "none"
type MULTIPLIER = SYMBOL | COLOR[] | "color-set" | "map" | "night"

export type CARD = {
    index: number,
    color: COLOR,
    night?: boolean,
    map?: boolean,
    symbols?: SYMBOL[],
    condition?: SYMBOL[],
    points?: number,
    multiplier?: MULTIPLIER
}
