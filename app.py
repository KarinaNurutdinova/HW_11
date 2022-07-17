from flask import Flask, request, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill


def main():
    app = Flask(__name__)

    @app.route("/")
    def get_candidates():
        data = load_candidates_from_json("candidates.json")
        return render_template('list.html', candidates=data)

    app.add_url_rule('/', view_func=get_candidates)

    @app.route("/candidates/<x>")
    def page_candidates(x):
        data = get_candidate(x)
        return render_template("card.html", candidate=data)

    @app.route("/search/<candidate_name>")
    def page_search(candidate_name):
        data = get_candidates_by_name(candidate_name)
        return render_template("search.html", candidates=data)

    @app.route("/skills/<skill_name>")
    def candidates_with_skills(skill_name):
        data = get_candidates_by_skill(skill_name)
        return render_template("skill.html", candidates=data)

    app.run()


if __name__ == '__main__':
    main()


