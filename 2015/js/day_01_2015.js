const fs = require("fs");
const data = fs.readFileSync("day_01_2015_input.txt", "utf-8");

const floors = (data) => {
  let floor = 0;

  for (let i = 0; i < data.length; i++) {
    if (data[i] === "(") {
      floor++;
    } else {
      floor--;

      if (floor < 0) {
        return i + 1;
      }
    }
  }
  return floor;
};

console.log(floors(data)); // 1783
