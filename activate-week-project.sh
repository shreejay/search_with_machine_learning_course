# Commands to activate weekly project
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

eval "$(pyenv activate search_with_ml_week1)"

export FLASK_ENV=development

export FLASK_APP=week1

flask run --port 3000

