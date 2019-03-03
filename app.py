from bokeh.plotting import figure, output_file, show,save

x = [1,2,3,4,5]
y = [4,3,56,8,5]

output_file('index1.html')

# add plots

p = figure(
    title = 'Example Plot',
    x_axis_label = 'x',
    y_axis_label = 'y'

)
# Render glyph
p.line(x, y, legend = 'test', line_width = 2)

# show result
# show(p)
# save file
save(p)