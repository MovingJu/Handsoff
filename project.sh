build(){
    rm -r .venv dist
    uv build
    uv sync --no-editable
}

run(){
    handsoff
}

clear(){
    rm -r src/handsoff.egg-info dist build .venv
}

push(){
    twine upload dist/*
}