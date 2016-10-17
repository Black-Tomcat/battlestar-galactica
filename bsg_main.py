from flask import *
import world_gen, math

app = Flask(__name__)

player_galaxy = world_gen.Galaxy()
player_galaxy.galaxy_generation()
player_galaxy.current_position = [10, 10]


def next_turn():
	current_chunk = [math.floor((player_galaxy.current_position[0] + 30) / 60), math.floor((player_galaxy.current_position[1] + 30) / 60)]
	if current_chunk != player_galaxy.current_chunk:
		player_galaxy.current_chunk = current_chunk
		player_galaxy.galaxy_segment_generation()


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		if request.form['submit'] == 'next_turn':
			# Execute the next turn.
			pass
	dict_player_galaxy = player_galaxy.dictionary_ify()
	return render_template('template.html', player_galaxy=dict_player_galaxy, trim_blocks=True, lstrip_blocks=True)


@app.route('/trial')
def trial():
	dict_player_galaxy = player_galaxy.dictionary_ify()
	return render_template('trial.html', player_galaxy=dict_player_galaxy, trim_blocks=True, lstrip_blocks=True)

if __name__ == '__main__':
	app.run(debug=True)
