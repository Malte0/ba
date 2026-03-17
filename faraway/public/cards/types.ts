
type SYMBOL = "Distel" | "Stein" | "Schimaere"
type COLOR = "red" | "blue" | "yellow" | "green"
type MULTIPLIER = SYMBOL | COLOR[] | "color-set" | "map" | "night"

export type REGION_CARD = {
    count: number,
    color: COLOR,
    night?: boolean,
    map?: boolean,
    symbols?: SYMBOL[],
    condition?: SYMBOL[],
    // points X number of MULTPLIER present, if MULTIPLIER is undefined multiply by 1
    points?: number,
    multiplier?: MULTIPLIER
}