.SILENT:
init:
	echo "init frames..."
	mkdir -p frames
	ffmpeg -i video/badApple.mp4 frames/%04d.png
	echo "init python..."
	python3 -m pip install -r requirements.txt

clean:
	echo "removing frames..."
	rm -rf frames/**
