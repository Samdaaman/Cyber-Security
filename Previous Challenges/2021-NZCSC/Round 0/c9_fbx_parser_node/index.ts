import { FBXData, FBXReader, parseBinary, parseText } from 'fbx-parser'
import * as fs from 'fs'

const file = 'HiddenInPlaneSite.fbx'
let fbx: FBXData

try {
  // try binary file encoding
  fbx = parseBinary(fs.readFileSync(file))
} catch (e) {
  // try text file encoding
  fbx = parseText(fs.readFileSync(file, 'utf-8'))
}

const root = new FBXReader(fbx);

// const numbers: number[] = root.fbx[8].nodes[0].nodes[6].nodes[4].props[0] as number[];
// console.log(numbers.map(x => x % 2 === 0 ? '0' : '1').join(''))

let verticiesFormatted = [] as number[][];
let verticyFormatted = [] as number[];
const verticies = root.fbx[8].nodes[0].nodes[2].props[0] as number[];
for (let i = 0; i < verticies.length; i++) {
  if (i % 3 === 0) {
    verticyFormatted = [verticies[i]]
  } else if (i % 3 == 1) {
    verticyFormatted.push(verticies[i])
  } else {
    verticyFormatted.push(verticies[i])
    verticiesFormatted.push(verticyFormatted);
  }
}

console.log(verticiesFormatted.map(x => x.join(',')).join('\n'))
console.log('done');


