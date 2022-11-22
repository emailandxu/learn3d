install-env:
	pip install -r requirements.txt
run:
	SDL_VIDEODRIVER=x11 python main.py