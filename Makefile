run:
	tmux new-session -d -s stock
	tmux send-keys "conda deactivate && conda activate stock && uvicorn main:app --reload" C-m
	tmux split-window -h -c "./frontend" "yarn start"
	tmux a -t stock
install:
	pip install -r requirements.txt
	pip install -r dev.txt
	cd frontend
	yarn
	cd ..
