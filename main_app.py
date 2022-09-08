"""This is a main python file there Flask app works"""
from flask import Flask, render_template
from utils import load_json_data, get_candidates_by_skill, get_candidate_by_id,\
    get_candidates_by_name
# -------------------------------------------------------------------------


def main():
    """The main Flask app function. The function contains all necessary views
     and routes"""

    FILE_NAME = 'candidates.json'
    app = Flask(__name__)

    candidates = load_json_data(FILE_NAME)

    @app.route('/')
    def index_page():
        """This is the main page view serving to show all
        available candidates

        Returns:
            render_template string with html markdown

        """
        return render_template('list.html', candidates_data=candidates)

    @app.route('/candidates/<int:id_user>')
    def candidate_page(id_user: int):
        """This view needed to show a single candidate found by his id

        :param id_user: An integer type number of candidate

        Returns:
            render_template string with html markdown
        """
        candidate = get_candidate_by_id(id_user, candidates)
        return render_template('single.html', candidate=candidate)

    @app.route('/search/<name>')
    def search(name: str):
        """This is the search view that allows to show all candidates found
        by inputted name

        :param name: A full name or a part of it of
        candidate you're looking for

        Returns:
            render_template string with html markdown
        """
        found_candidates = get_candidates_by_name(name, candidates)
        count = len(found_candidates)

        return render_template('search.html', found=found_candidates,
                               count=count)

    @app.route('/skill/<skill_name>')
    def search_by_skill(skill_name: str):
        """This Flask view allows to find and show candidates by desired
        skill

        :param skill_name: A skill of candidate you're looking for

        Returns:
            render_template string with html markdown
        """
        found_candidates = get_candidates_by_skill(skill_name, candidates)
        count = len(found_candidates)

        return render_template('skill.html', found=found_candidates,
                               count=count, skill=skill_name)

    app.run()
# -------------------------------------------------------------------------


main()
