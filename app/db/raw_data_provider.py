from .pg import connect
from app.db import queries


class RawDataProvider:
    @staticmethod
    def create_survey(**kwargs):
        title, description, is_anonymous, created_by = kwargs.values()
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.CREATE_SURVEY,
                           (title, description, created_by, is_anonymous))
            survey = cursor.fetchone()
            conn.commit()
            return {
                'id': survey[0],
                'title': survey[1],
                'description': survey[2],
                'created_by': survey[3],
                'is_anonymous': survey[4]
            }

    @staticmethod
    def get_all_surveys():
        conn = connect()
        surveys = []
        with conn.cursor() as cursor:
            cursor.execute(queries.ALL_SURVEYS)
            raw_surveys = cursor.fetchall()
            for survey in raw_surveys:
                surveys.append({
                    'id': survey[0],
                    'title': survey[1],
                    'description': survey[2],
                    'created_by': survey[3],
                    'created_at': survey[4],
                    'is_anonymous': survey[5]
                })
        return surveys

    @staticmethod
    def get_survey(survey_id):
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.GET_SURVEY, (survey_id,))
            result = cursor.fetchone()
            if not result:
                return None
            return {
                'id': result[0],
                'title': result[1],
                'description': result[2],
                'created_by': result[3],
                'created_at': result[4],
                'is_anonymous': result[5],
                'user_name': result[6]
            }

    @staticmethod
    def is_already_voted(survey_id, user_id, user_ip):
        conn = connect()
        with conn.cursor() as cursor:
            if user_id:
                cursor.execute(queries.CHECK_USER_VOTED, (survey_id, user_id))
            else:
                cursor.execute(
                    queries.CHECK_ANONYMOUS_USER_VOTED, (survey_id, user_ip)
                )
            return cursor.fetchone() is not None

    @staticmethod
    def get_survey_options(survey_id):
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.GET_OPTIONS_FOR_SURVEY, (survey_id,))
            options = cursor.fetchall()
            return [{'id': opt[0], 'description': opt[1]} for opt in options]

    @staticmethod
    def create_vote(**kwargs):
        survey_id, user_id, voter_ip, option_id, option_ids = kwargs.values()
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.CREATE_VOTE, (survey_id, user_id, voter_ip))
            vote = cursor.fetchone()
            vote_id = vote[0]

            for opt_id in option_ids:
                cursor.execute(queries.CREATE_VOTE_OPTIONS, (vote_id, opt_id))

            conn.commit()
            return vote_id

    @staticmethod
    def get_user(user_name):
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.GET_USER_BY_USERNAME, (user_name,))
            result = cursor.fetchone()
            if not result:
                return None
            return {
                'id': result[0],
                'user_name': result[1],
                'password': result[2]
            }

    @staticmethod
    def delete_survey(survey_id):
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.DELETE_SURVEY, (survey_id,))
            result = cursor.fetchone()
            conn.commit()
            if not result:
                return None
            return {'id': result[0]}

    @staticmethod
    def get_votes_for_survey(survey_id):
        conn = connect()
        with conn.cursor() as cursor:
            cursor.execute(queries.GET_VOTES_FOR_SURVEY, (survey_id,))
            results = cursor.fetchall()
            print('------------')
            print(results)
            return [
                {'description': row[0], 'vote_count': row[1]}
                for row in results
            ]
