from bokeh.plotting import figure, output_file, show,save, ColumnDataSource
from bokeh.models.tools import HoverTool
import pandas


# read csv file     
df = pandas.read_csv('cars.csv')

# car = df['Car']
# hp = df['Horsepower']

# column data source from data frame
source = ColumnDataSource(df)


output_file('index.html')
# car list
car_list = source.data['Car'].tolist()
# add plots

p = figure(
    y_range = car_list,
    plot_width = 800,
    plot_height= 600,
    title = 'Car with Top HorsePower',
    x_axis_label = 'Horse Power'
)
# Render glyph
p.hbar(
    y = 'Car',
    right = 'Horsepower',
    left = 0,
    height = 0.4,
    color = 'blue',
    fill_alpha = 0.5,
    source = source,
)
# hover tools
hover = HoverTool()
hover.tooltips = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
<div class="">
    <h3>@Car</h3>
    <div><strong>Price:</strong>@Price</div>
    <div><strong>HP:</strong>@Horsepower</div>
    <div><img src="@Image" class="circle" alt = "" width="200"/></div>
</div>

"""
p.add_tools(hover)
# show result
# show(p)

# save file
save(p)