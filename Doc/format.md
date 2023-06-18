# Save format
<chunk coord exa>{<hexa value for a block><hexa value for a block><hexa value for a block>...}
--> example :
a5;2b;10{00;00;00;00;00;00;00;00;01;01;01;01;01;02;03...};g2;00;23{40;60;65;01;v5...}
--> blocks starts from upside x=0 y=0 z=0

# Python world memory
[({"x":0, "y":0, "z":0}, [b1, b2, b3...]), 
{"x":1, "y":0, "z":0}, [b1, b2, b3...]), ...]

# Blocks id
- air : 0
- grass_block : 1
- dirt : 2
- stone : 3
- cobble_stone : 4
