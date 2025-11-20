import * as fs from "fs";

export function writeResultToFile(
  results: {
    [key: string]: number;
  },
  testValue: number,
  iteration: number,
  playerToTrack: string,
  outputFileName: string
) {
  const file = `./${outputFileName}`;
  let content = fs.readFileSync(file, "utf-8");
  const testValues = content.split("\n");
  let outPerforms = results[playerToTrack];
  if (testValues.length > iteration+1) {
    const currentValue = Number(testValues[iteration]);
    testValues[iteration] = `${Math.round(((currentValue + outPerforms) / 2) * 100) / 100}`;
    // console.log(`Writing ${testValues[iteration]}`)
    fs.writeFileSync(file, testValues.join("\n"), "utf-8");
  } else {
    fs.writeFileSync(file, content+`${Math.round(outPerforms * 100) / 100}\n`, "utf-8")
  }

}