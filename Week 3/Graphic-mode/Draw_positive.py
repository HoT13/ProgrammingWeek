def setup():
  size(500,500)

draw_positive():
  r = random(0 ,255);
  g = random(0 ,255);
  b = random(0 ,255);
  background(200)

  fill(r,g,b)
  stroke(2)
  rect(mouseX+100, mouseY+100, 50, 50);
  rect(mouseX+100, mouseY+150, 50, 50);
  rect(mouseX+100, mouseY+200, 50, 50);
  rect(mouseX+150, mouseY+150, 50, 50);
  rect(mouseX+50, mouseY+150, 50, 50);