import picasso
p = picasso.Picasso("hello_world")
p.draw_best_fitting_line = True

p.add_point(0,10)
p.add_point(1,20)
p.add_point(2,30)
p.add_point(3,40)
p.export()