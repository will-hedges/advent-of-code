const fs = require("fs");
const data = fs.readFileSync("day_02_2015_input.txt", "utf-8").split("\r\n");

let totalPaper = 0;
let totalRibbon = 0;

const paperAndRibbon = (dims) => {
  dims = dims.split("x");
  dims = [Number(dims[0]), Number(dims[1]), Number(dims[2])];
  let [l, w, h] = dims.sort(function (x, y) {
    return x - y;
  });
  let [a, b, c] = [l * w, w * h, h * l];

  let surfaceArea = 2 * a + 2 * b + 2 * c;
  let paper = surfaceArea + Math.min(a, b, c);

  let wrap = 2 * l + 2 * w;
  let bow = l * w * h;
  let ribbon = wrap + bow;

  totalPaper += paper;
  totalRibbon += ribbon;

  return;
};

for (let i = 0; i < data.length; i++) {
  // last array elem is a blank string
  if (data[i]) {
    paperAndRibbon(data[i]);
  }
}

console.log(totalPaper); // 1588178
console.log(totalRibbon); // 3783758
