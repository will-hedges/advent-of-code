const fs = require("fs");
const data = fs.readFileSync("day_03_2015_input.txt", "utf-8");

const sleigh = {
  x: 0,
  y: 0,
  coords: [[0, 0]],
  move: function (arrow) {
    if (arrow === ">") {
      this.x += 1;
    } else if (arrow === "<") {
      this.x -= 1;
    } else if (arrow === "^") {
      this.y += 1;
    } else if (arrow === "v") {
      this.y -= 1;
    }
    this.coords.push([this.x, this.y]);
  },
};

// part one
const Sleigh = Object.create(sleigh);
for (let i = 0; i < data.length; i++) {
  Sleigh.move(data[i]);
}

let res = new Set(new Map(Sleigh.coords.map((c) => [c.join(), c])).values())
  .size;
console.log(res); // 2081
