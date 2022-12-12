import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from . import app

@app.route('/plot.png')
def chartTest():
  lnprice=np.log(price)
  plt.plot(lnprice)   
  plt.savefig('/static/images/new_plot.png')
  return render_template('untitled1.html', name = 'new_plot', url ='/static/images/new_plot.png')


def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig