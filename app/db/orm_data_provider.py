from werkzeug.security import generate_password_hash
from sqlalchemy import select, func, and_
from app.db.orm_pg import get_session
from app.db.models import User, Survey, Option, Vote, VoteOption


class OrmDataProvider:
    @staticmethod
    def create_survey(**kwargs):
        with get_session() as session:
            survey = Survey(**kwargs)
            session.add(survey)
            session.commit()
            session.refresh(survey)

            return {
                'id': survey.id,
                'title': survey.title,
                'description': survey.description,
                'created_by': survey.created_by,
                'is_anonymous': survey.is_anonymous
            }

    @staticmethod
    def get_all_surveys():
        with get_session() as session:
            stmt = select(
                Survey.id,
                Survey.title,
                Survey.description,
                Survey.created_by,
                Survey.created_at,
                Survey.is_anonymous
            )

            results = session.execute(stmt).all()

            surveys = []
            for survey in results:
                surveys.append({
                    'id': survey.id,
                    'title': survey.title,
                    'description': survey.description,
                    'created_by': survey.created_by,
                    'created_at': survey.created_at,
                    'is_anonymous': survey.is_anonymous
                })

            return surveys

    @staticmethod
    def get_survey(survey_id):
        with get_session() as session:
            stmt = (
                select(
                    Survey.id,
                    Survey.title,
                    Survey.description,
                    Survey.created_by,
                    Survey.created_at,
                    Survey.is_anonymous,
                    User.user_name
                )
                .outerjoin(User, Survey.created_by == User.id)
                .where(Survey.id == survey_id)
            )
            result = session.execute(stmt).first()

            if not result:
                return None

            return {
                'id': result.id,
                'title': result.title,
                'description': result.description,
                'created_by': result.created_by,
                'created_at': result.created_at,
                'is_anonymous': result.is_anonymous,
                'user_name': result.user_name
            }

    @staticmethod
    def is_already_voted(survey_id, user_id, user_ip):
        with get_session() as session:
            if user_id:
                stmt = select(Vote.id).where(
                    and_(Vote.survey_id == survey_id, Vote.user_id == user_id)
                )
            else:
                stmt = select(Vote.id).where(
                    and_(Vote.survey_id == survey_id, Vote.voter_ip == user_ip)
                )

            result = session.execute(stmt).first()
            return bool(result)

    @staticmethod
    def get_survey_options(survey_id):
        with get_session() as session:
            stmt = (
                select(Option.id, Option.description)
                .where(Option.survey_id == survey_id)
            )
            results = session.execute(stmt).all()

            return [
                {
                    'id': option.id,
                    'description': option.description
                }
                for option in results
            ]

    @staticmethod
    def create_vote(**kwargs):
        survey_id, user_id, voter_ip, option_id, option_ids = kwargs.values()
        with get_session() as session:
            # Создаем запись голоса
            vote = Vote(
                survey_id=survey_id,
                user_id=user_id,
                voter_ip=voter_ip
            )
            session.add(vote)
            session.flush()  # Получаем vote_id без коммита

            # Создаем связи с опциями
            for opt_id in option_ids:
                vote_option = VoteOption(
                    vote_id=vote.id,
                    option_id=opt_id
                )
                session.add(vote_option)

            session.commit()
            return vote.id

    @staticmethod
    def create_user(user_name, password):
        hashed_password = generate_password_hash(password)
        with get_session() as session:
            user = User(user_name=user_name, password=hashed_password)
            session.add(user)
            session.commit()
            session.refresh(user)
            return {
                'id': user.id,
                'user_name': user.user_name
            }

    @staticmethod
    def get_user(user_name):
        with get_session() as session:
            user = session.query(User).filter_by(user_name=user_name).first()
            if not user:
                return None
            return {
                'id': user.id,
                'user_name': user.user_name,
                'password': user.password
            }

    @staticmethod
    def get_votes_for_survey(survey_id):
        with get_session() as session:
            stmt_votes = (
                select(
                    Option.description,
                    func.count(VoteOption.id).label("vote_count")
                )
                .join(VoteOption, VoteOption.option_id == Option.id)
                .join(Vote, Vote.id == VoteOption.vote_id)
                .where(Vote.survey_id == survey_id)
                .group_by(Option.description)
            )
            votes = session.execute(stmt_votes).mappings().all()

            stmt_survey = (
                select(
                    Survey.id,
                    Survey.title,
                    Survey.description,
                    Survey.created_by,
                    Survey.created_at,
                    Survey.is_anonymous,
                    User.user_name
                )
                .outerjoin(User, Survey.created_by == User.id)
                .where(Survey.id == survey_id)
            )
            survey = session.execute(stmt_survey).first()

            return {
                'votes': votes,
                'survey': {
                    'id': survey.id,
                    'title': survey.title,
                    'description': survey.description,
                    'created_by': survey.created_by,
                    'created_at': survey.created_at,
                    'is_anonymous': survey.is_anonymous,
                    'user_name': survey.user_name
                } if survey else None
            }

    @staticmethod
    def add_option(survey_id, description):
        with get_session() as session:
            option = Option(survey_id=survey_id, description=description)
            session.add(option)
            session.commit()
            session.refresh(option)
            return {
                'id': option.id,
                'survey_id': option.survey_id,
                'description': option.description
            }

    def delete_survey(survey_id):
        with get_session() as session:
            survey = session.query(Survey).filter_by(id=survey_id).first()
            if not survey:
                return False  # или выбросить исключение

            session.delete(survey)
            session.commit()
            return True
