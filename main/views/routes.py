from flask import (
	request,
	redirect,
	render_template,
	url_for
)
from . import bp


@bp.route("/")
@bp.route("/main")
def main():
	return render_template("main.html")