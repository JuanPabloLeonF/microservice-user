from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.future import select
from app.configuration.exceptions_personalities import IntegrityErrorDatabase
from app.src.infrastructure.outputs.mysql.repositories.i_repository_user import IUserRepository
from app.src.infrastructure.outputs.mysql.entities.entity_user import UserEntity
from app.src.infrastructure.outputs.mysql.settings.database_config import DatabaseConfiguration

class ImplementationUserRepository(IUserRepository):

    async def create(self, userEntity: UserEntity) -> UserEntity:
        async with DatabaseConfiguration.getSession() as session:
            try:
                session.add(userEntity)
                await session.commit()
                await session.refresh(userEntity)
                return userEntity
            except IntegrityError:
                await session.rollback()
                raise IntegrityErrorDatabase("El correo ya está en uso.")
            except SQLAlchemyError as error:
                await session.rollback()
                raise RuntimeError(str(error))

    async def getById(self, id: str) -> UserEntity:
        async with DatabaseConfiguration.getSession() as session:
            result = await session.get(UserEntity, id)
            if not result:
                raise ValueError(f"User not found with the id: {id}")
            return result

    async def getByEmail(self, email: str) -> UserEntity:
        async with DatabaseConfiguration.getSession() as session:
            stmt = select(UserEntity).where(UserEntity.email == email)
            result = await session.execute(stmt)
            userFound = result.scalars().first()
            if not userFound:
                raise ValueError(f"User not found with the email: {email}")
            return userFound

    async def getAll(self, page: int, limit: int) -> list[UserEntity]:
        async with DatabaseConfiguration.getSession() as session:
            result = await session.execute(
                select(UserEntity).
                limit(limit).
                offset((page - 1) * limit)
            )
            return result.scalars().all()

    async def updateById(self, userEntity: UserEntity, id: str) -> UserEntity:
        async with DatabaseConfiguration.getSession() as session:
            try:
                userFound = await session.get(UserEntity, id)
                if not userFound:
                    raise ValueError(f"User not found with the id: {id}")

                userFound.name = userEntity.name
                userFound.email = userEntity.email
                userFound.password = userEntity.password
                userFound.roles = userEntity.roles

                await session.commit()
                await session.refresh(userFound)
                return userFound
            except IntegrityError:
                await session.rollback()
                raise IntegrityErrorDatabase("El correo ya está en uso.")
            except SQLAlchemyError as error:
                await session.rollback()
                raise RuntimeError(str(error))

    async def deleteById(self, id: str) -> str:
        async with DatabaseConfiguration.getSession() as session:
            try:
                userFound = await session.get(UserEntity, id)
                if not userFound:
                    raise ValueError(f"User not found with the id: {id}")

                await session.delete(userFound)
                await session.commit()
                return f"User deleted successfully with the id: {id}"
            except SQLAlchemyError as error:
                await session.rollback()
                raise RuntimeError(str(error))